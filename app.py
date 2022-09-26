
from curses.ascii import US
from unittest import result
from flask import (
    Flask, 
    render_template,
    request,
    jsonify,
    abort
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jerimy:12345@localhost:5432/utecbet2022'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    cash = db.Column(db.Integer, nullable=False,default=5000)
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

@app.route('/', methods=['GET'])
def greetings():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        name = request.args.get('name')
        password = request.args.get('password')
    else:
        name = request.form.get('name')
        password = request.form.get('password')

    user = User(name=name, password=password)
    db.session.add(user)
    db.session.commit()
    
    return_str = '{} {}'.format(name, "********")
    return render_template('thankyou.html', data=return_str)

if __name__ == '__main__':
    app.run(debug=True)


