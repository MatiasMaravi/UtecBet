
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/utecbet2022'
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
        

class  Team(db.Model):
    __tablename__ = 'teams'
    name = db.Column(db.String(),primary_key = True)
    winrate = db.Column(db.Float,nullable = False,default = 0)
    coach = db.Column(db.String(),nullable = False)
    def __repr__(self):
        return f'Team: name={self.name}, winrate={self.winrate}, coach={self.coach}'
db.create_all()

#Controllers
@app.route('/', methods=['GET'])
def index():
    return "hola"

if __name__ == '__main__':
    app.run(debug=True)


