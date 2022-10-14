
from email.policy import default
from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#Modelos
app = Flask(__name__)
user = "postgres:123"
data_base = "utecbet2022"
conection = "localhost:5432"
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}@{conection}/{data_base}'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    cash = db.Column(db.Float, default=5000,nullable=False)

    def __repr__(self):
        return f'Team: id={self.id}, username={self.username}, password={self.password}'
    
    def format(self):
        return {
            'id': self.id,
            'username':self.username,
            'password':self.password,
            'cash':self.cash
        }

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
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
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

    
class Team(db.Model):
    __tablename__ = 'teams'
    name = db.Column(db.String(),primary_key = True)
    winrate = db.Column(db.Float,nullable = False,default = 0)
    coach = db.Column(db.String(),nullable = False)
    matches = db.relationship('Matches',backref='matches',lazy=True)
    bets = db.relationship('Bets',backref='bets',lazy = True)
    def __repr__(self):
        return f'Team: name={self.name}, winrate={self.winrate}, coach={self.coach}'
    
    def format(self):
        return {
            'name': self.id,
            'winrate':self.winrate,
            'coach':self.coach
        }

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
class Match(db.Model):
    __tablename__ = "matches"
    code = db.Column(db.Integer, primary_key=True)
    visit = db.Column(db.String(), db.ForeignKey('teams.name'),nullable = False)
    local = db.Column(db.String(), db.ForeignKey('teams.name'),nullable = False)
    winner = db.Column(db.String(), default = "Unknown")
    date = db.Column(db.String(),nullable = False)
    bets = db.relationship('Bets',backref='bets',lazy=True)
    def __repr__(self):
        return f'Match: code={self.code}, visit={self.visit}, local={self.local}, winner={self.winner}, date={self.date}'

    def format(self):
        return {
            'code': self.id,
            'visit': self.visit,
            'local': self.local,
            'winner': self.winner,
            'date':self.date
        }

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
class Bet(db.Model):
    __tablename__ = 'bets'
    id = db.Column(db.Integer, primary_key=True)
    quota = db.Column(db.Float, nullable=False, default=1.00)
    bet_amount = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(), nullable=False)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    match_code= db.Column(db.Integer, db.ForeignKey('matches.code'), nullable=False)
    def __repr__(self):
        return f'Bet: id={self.id}, quota={self.quota}, result={self.result}, bet_amount={self.bet_amount},id_user={self.id_user} ,match_code={self.match_code}'

    def format(self):
        return {
            'id': self.id,
            'quota':self.quota,
            'result':self.result,
            'bet_amount':self.bet_amount,
            'id_user':self.id_user,
            'match_code':self.match_code
        }


    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        

with app.app_context():
    db.init_app(app)
    migrate.init_app(app, db)

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
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('user_create.html')
        
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


