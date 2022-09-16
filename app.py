
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
    password = db.Column(db.Boolean, nullable=False, default=False)
    cash = db.Column(db.Integer, nullable=False,default=0)
    def __repr__(self):
        return f'User: id={self.id}, name={self.name}, password={self.password}, cash={self.cash}'
        

class Apuesta(db.Model):
    __tablename__ = 'apuestas'
    codigo = db.Column(db.Integer, primary_key=True)
    name_equipo = db.Column(db.String(), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    ganancia = db.Column(db.Float, nullable=False)
    result = db.Column(db.Boolean, nullable=False, default=False)
    def __repr__(self):
        return f'Apuesta: codigo={self.codigo}, name_equipo={self.name_equipo},monto={self.monto}, ganancia={self.ganancia}, result={self.result}'
        

db.create_all()

#Controllers
@app.route('/', methods=['GET'])
def index():
    return "hola"

if __name__ == '__main__':
    app.run(debug=True)


