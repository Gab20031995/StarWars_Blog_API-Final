"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Vehicles, Favorites
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/register', methods=['POST'])
def register_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # valida si estan vacios los ingresos
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400
    
    # busca usuario en BBDD
    user = User.query.filter_by(email=email).first()
    if user:
        # the user was not found on the database
        return jsonify({"msg": "User already exists"}), 401
    else:
        # crea usuario nuevo
        new_user = User()
        new_user.email = email
        new_user.password = password
        # crea registro nuevo en BBDD de 
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "User created successfully"}), 200


@app.route('/login', methods=['POST']) 
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # valida si estan vacios los ingresos
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400

    # para proteger contrase??as usen hashed_password
    # busca usuario en BBDD
    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Invalid username or password"}), 401
    else:
        # crear token
        my_token = create_access_token(identity=user.id)
        return jsonify({"token": my_token})

@app.route("/protected", methods=['GET', 'POST'])
    # protege ruta con esta funcion
@jwt_required()
def protected():
    # busca la identidad del token
    current_id = get_jwt_identity()
    # busca usuarios en base de datos
    user = User.query.get(current_id)
    print(user)
    return jsonify({"id": user.id, "email": user.email}), 200

@app.route('/people', methods=['GET'])
def getPeople():
    persona = People.query.all()
    request = list(map(lambda persona:persona.serialize(),persona))    
    return jsonify(request), 200

@app.route('/planets', methods=['GET'])
def getPlanets():
    planeta = Planets.query.all()
    request = list(map(lambda planeta:planeta.serialize(),planeta))    
    return jsonify(request), 200
    
@app.route('/vehicles', methods=['GET'])
def getVehicles():
    nave = Vehicles.query.all()
    request = list(map(lambda nave:nave.serialize(),nave))    
    return jsonify(request), 200    

@app.route('/favorites', methods=['GET', 'POST','DELETE'])
def getFavorites():
    if (request.method == "GET"):
        fav1 = Favorites.query.all()
        favoritos = list(map(lambda favoritos:favoritos.serialize(),fav1)) 
        return jsonify(favoritos), 200

    if (request.method == "POST"):
        post_fav1 = request.json.get() 
        post_fav1 = list(map(lambda favoritos:favoritos.serialize(),post_fav1))
        post_fav1.user_id = "user_id"
        db.session.commit()
        return jsonify({"msg": "Favorite are included"}), 200
    
    if (request.method == "DELETE"):
        delete_fav1 = Favorites.query.get()
        delete_fav1 = list(map(lambda favoritos: favoritos.serialize(),delete_fav1))
        favorites.delete()
        db.session.commit()
        return jsonify({"msg": "Favorite are deleted"}), 200 



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
