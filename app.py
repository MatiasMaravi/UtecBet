
from curses.ascii import US
from tabnanny import check
from unittest import result
from flask import (
    Flask, 
    render_template,
    request
)
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import check_password_hash,generate_password_hash

from config import config
from flask_wtf import CSRFProtect
import os

#Configuration
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jerimy:12345@localhost:5432/utecbet2022'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@classmethod
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    cash = db.Column(db.Integer, default=5000,nullable=False)
    def check_password(self, hashed_password,password):
        return check_password_hash(hashed_password,password)
    def __repr__(self):
        return f'User: id={self.id}, name={self.name}, password={self.password}, cash={self.cash}'
        
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

#Controllers

@app.route('/')
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)
    csrf = CSRFProtect(app)


