from flask_migrate import Migrate
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
#Modelos
user = "postgres:123"
data_base = "utecbet2022"
conection = "localhost:5432"

database_path = f'postgresql://{user}@{conection}/{data_base}'
db = SQLAlchemy()
def setup_db(app, database_path=database_path):
    app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app=app

    with app.app_context():
        db.init_app(app)
        db.create_all()

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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    cash = db.Column(db.Float, default=5000, nullable=False)
    bets = db.relationship("Bet",backref="bets",lazy=True)
    created_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    is_admin= db.Column(db.Boolean,default=False)
    
    def get_user_id(self):
        return self.id
    @property
    def password(self):
        raise AttributeError('Password is not defined')

    @password.setter
    def password(self, password):    
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

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
            return self.id
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
            'name': self.name,
            'winrate':self.winrate,
            'coach':self.coach
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
            'code': self.code,
            'visit': self.visit,
            'local': self.local,
            'winner': self.winner,
            'date':self.date
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

