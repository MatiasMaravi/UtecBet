from models import (
    setup_db,
    Bet, 
    User,
    Team,
    Match,
    Admin_Account,
    db)
from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
import jwt
import datetime
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'utecuniversity'
    setup_db(app)
    CORS(app, origins=['http://127.0.0.1:8080', 'http://localhost:8080'], max_age=10)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PATCH, PUT, DELETE')
        response.headers.add('Access-Control-Max-Age', 10)
        return response

    @app.route('/register', methods=['POST'])
    def register():
        body = request.get_json()
        id = body.get('id',None)
        username = body.get('username', None)
        password = body.get('password', None)

        if  username is None or password is None:
            abort(422)

        #Search
        db_user = User.query.filter(User.username==username).first()
        errors_to_send = []
        if db_user is not None:
            if db_user.username == username:
                errors_to_send.append('An account with this username already exists')

        if len(password) < 4:
            errors_to_send.append('The length of the password is too short')

        if len(errors_to_send) > 0:
            return jsonify({
                'success': False,
                'code': 422,
                'messages': errors_to_send
            }), 422
        if id == None:
            user = User(username=username, password=password)
            new_user_id = user.insert()
        else:
            user = User(id=id,  username=username, password=password)
            new_user_id = user.insert()
        token = jwt.encode({
            'id': new_user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return jsonify({
            'success': True,
            'token': str(token),
            'user_id': new_user_id
        })
    @app.route('/login', methods=['POST'])
    def login():
        body = request.get_json()
        username = body.get('username', None)
        password = body.get('password', None)

        user = User.query.filter(User.username==username).one_or_none()
        is_logged = user is not None and user.verify_password(password)
        if not is_logged:
            abort(401)
        else:
            token = jwt.encode({
                'id': str(user.get_user_id()),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, app.config['SECRET_KEY'])
            return jsonify({
                'success': True,
                'token': token,
                'username':username
            })

    @app.route('/users/<id>',methods=['DELETE'])
    def delete_user(id):
        status = 500
        try:
            user = User.query.get(id)
            if user == None:
                status = 404
                abort(status)
            
            user.delete()
            return jsonify({
                'success': True,
                'delete_user':int(id)
            })
        except Exception as e:
            print(e)
            abort(status)


    @app.route('/users/<id>',methods=['PATCH'])
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
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'server error'
        }), 500

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'unprocessable entity'
        }), 422

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'code': 405,
            'message': 'method not allowed'
        }), 405


    @app.errorhandler(409)
    def conflict(error):
        return jsonify({
            'success': False,
            'code': 409,
            'message': 'resource already exist'
        }), 409

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'code': 401,
            'message': 'Invalid login. Please try again'
        }), 401
    return app