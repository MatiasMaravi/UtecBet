from flask_login import (login_user, 
    login_required, 
    current_user, 
    logout_user)
from models import (
    setup_db,
    Bet, 
    User,
    Team,
    Match,
    LoginForm,
    Admin_Account,
    Admin,
    RegisterForm,
    AdminView,
    db)
from flask import (
    Flask,
    abort,
    jsonify,
    request,
    url_for,
    render_template,
    redirect
)
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash


def create_app(test_config=None):
    app = Flask(__name__,template_folder='templates')
    bootstrap = Bootstrap(app)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PATCH, PUT, DELETE')
        return response

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
    return app