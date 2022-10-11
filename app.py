from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

##Modelos
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jerimy:12345@localhost:5432/utecbet2022'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    cash = db.Column(db.Integer, default=5000,nullable=False)

#login_manager
@login_manager.user_loader
def load_user(user_id):
    #retorna el usuario a traves del id
    return User.query.get(int(user_id))

#ayuda de flaskform para el logueo y creacion de usuario
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

    
class Team(db.Model):
    __tablename__ = 'teams'
    name = db.Column(db.String(),primary_key = True)
    winrate = db.Column(db.Float,nullable = False,default = 0)
    coach = db.Column(db.String(),nullable = False)
    def __repr__(self):
        return f'Team: name={self.name}, winrate={self.winrate}, coach={self.coach}'

class BET(db.Model):
    __tablename__ = 'bet'
    posible_ganador = db.Column(db.String(), nullable=False)
    cuota = db.Column(db.Float, nullable=False, default=1.00)
    resultado = db.Column(db.String(), nullable=False)
    monto_apuesta = db.Column(db.Integer, nullable=False)
    M_codigo= db.Column(db.Integer, primary_key = True)
    C_transaccion= db.Column(db.Integer, db.ForeignKey('transaccion.id'), nullable=False)
    def __repr__(self):
        return f'BET: posible_ganador={self.posible_ganador}, cuota={self.cuota}, resultado={self.resultado}, monto_apuesta={self.monto_apuesta}, M_codigo={self.M_codigo}'

class Transaccion(db.Model):
    __tablename__ = 'transaccion'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    cash = db.Column(db.Integer, nullable=False,default=5000)
    id_transaccion=db.relationship('BET', backref='transaccion',lazy=True)
    def __repr__(self):
        return f'Transaccion: id={self.id}, name={self.name}, password={self.password}, cash={self.cash}, id_transaccion={self.id_transaccion}'
db.create_all()


##Endpoints

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                ##retornar a UtecBEt
                return redirect(url_for('dashboard'))

        else:
            #Invalido usuario o contraseña
            return render_template('index.html')
       

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created!</h1>'
        
    return render_template('signup.html', form=form)



#pagina principal de utecbet
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

#regreso al menu principal
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)