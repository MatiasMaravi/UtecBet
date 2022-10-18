from flask import Flask, render_template, redirect, url_for, abort,request, jsonify
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from sqlalchemy import asc 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.sql import func
#Modelos
app = Flask(__name__)
user = "jerimy:12345"
data_base = "utecbet2022"
conection = "localhost:5432"
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}@{conection}/{data_base}'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Admin_Account(db.Model):
    __tablename__ = 'admin_accounts'
    id = db.Column(db.Integer, primary_key=True)
    money = db.Column(db.Integer, default = 0, nullable=False)
    
    def __repr__(self):
        return f'Admin_Account: id={self.id}, money={self.money}'
    
    def format(self):
        return {
            'id': self.id,
            'money':self.money
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

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    cash = db.Column(db.Float, default=5000, nullable=False)
    bets = db.relationship("Bet",backref="bets",lazy=True)
    created_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    is_admin= db.Column(db.Boolean,default=False)
    
    def __repr__(self):
        return f'Team: id={self.id}, username={self.username}, cash={self.cash}'
    
    def format(self):
        return {
            'id': self.id,
            'username':self.username,
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
            return self.format()
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

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

    
class Team(db.Model):
    __tablename__ = 'teams'
    name = db.Column(db.String(),primary_key = True)
    winrate = db.Column(db.Float,nullable = False,default = 0)
    coach = db.Column(db.String(),nullable = False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
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
    visit = db.Column(db.String(),nullable = False)
    local = db.Column(db.String(),nullable = False)
    winner = db.Column(db.String(), server_default = "Unknown")
    date = db.Column(db.String(),nullable = False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    bets = db.relationship('Bet',backref='bets_',lazy=True)
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
    created_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
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
            return self.format()
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

class AdminView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.is_admin == True:
                return current_user.is_authenticated
            else:
                return abort(404)
        #return current_user.is_authenticated

    def not_auth(self):
        return "you are not authorized to use the admin dasboard"

admin = Admin(app, name='super_user', template_mode="bootstrap4")
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Team, db.session))
admin.add_view(AdminView(Match, db.session))
admin.add_view(AdminView(Bet, db.session))
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
        try:
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    app.logger.info('%s logged in successfully', user.username)
                    return redirect(url_for('dashboard'))

            else:
                app.logger.info('%s failed to log in', user.username)
                return render_template('index.html')
        except Exception as e:
            print(e)
            abort(404)


    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    try:
        form = RegisterForm()
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('user_create.html')
        return render_template('signup.html', form=form)
    except Exception as e:
        print(e)
        db.session.rollback()
        abort(409)
@app.route('/creat_admin', methods=['GET','POST'])
def creat_admin():
    try:
        if request.method == 'POST':
            password=request.form['password']
            hashed_password = generate_password_hash(password, method='sha256')
            variable = request.form['secret_key']
            if variable == "ut3cb3t":
                new_user=User(username=request.form['username'], password=hashed_password,is_admin=True)
                db.session.add(new_user)
                db.session.commit()
                return render_template('user_create.html')
        return render_template('create_admin.html')
    except Exception as e:
        print(e)
        db.session.rollback()
        abort(409)

#pagina principal de utecbet
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', 
    name=current_user.username,
    matches = Match.query.order_by('code').all(),
    id_=current_user.id)

#regreso al menu principal
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

#No usado actualemte
@app.route('/matches',methods=['GET'])
def get_matches():
    return render_template("matches.html",matches = Match.query.order_by('code').all())

@app.route('/update_user/<id>',methods=['PATCH'])
def update_user(id):
    status = 500
    try:
        args = request.get_json()
        username = args.get('username',None)
        cash = args.get('cash',None)
        user = User.query.filter_by(id=id).one_or_none()

        if user == None:
            status = 404
            abort(status)

        if username != None:
            user.nombre=username
        if cash != None:
            user.cash-= float(cash)

        user=user.update()

        return jsonify({
            'success': True,
            'user':user
        })

    except Exception as e:
        print(e)
        abort(status)

@app.route('/create_bet',methods = ['POST'] )
def create_bet():
    status = 500
    try:
        args = request.get_json()
        id_ = args.get('id',None) 
        quota = args.get('quota',None)
        bet_amount = args.get('bet_amount',None)
        result = args.get('result',None)
        id_user = args.get('id_user',None)
        match_code = args.get('match_code',None)
        Apuesta = Bet.query.filter_by(id=id_).one_or_none()
        
        if Apuesta != None:
            status = 409
            abort(status)

        if  quota == None or bet_amount == None or result == None or id_user == None or match_code == None:
            status = 400
            abort(status)

        Apuesta = Bet(id=id_,quota=quota,bet_amount=bet_amount,result=result,id_user=id_user,match_code=match_code)

        Apuesta = Apuesta.insert()
        response = {
            'success': True,
            'persona': Apuesta,
            'total_apuestas': len(Bet.query.all())
        }
        Cuenta = Admin_Account.query.filter_by(id=1).one_or_none()
        Cuenta.money += 5; #Ganancia
        Cuenta.update()
        return jsonify(response)

    except Exception as e:
        print(e)
        abort(status)

@app.route('/bets/<bet_id>', methods=['DELETE'])
def delete_bet(bet_id):
    response = {}
    Apuesta = Bet.query.get(bet_id)
    Apuesta.delete()
    response['success'] = True
    return jsonify(response)

@app.errorhandler(404)
def not_found(error):
    return render_template('error_404.html')

@app.errorhandler(409)
def not_found(error):
    return render_template('error_409.html')

if __name__ == '__main__':
    app.run(debug=True)
