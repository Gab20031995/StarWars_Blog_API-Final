from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
  

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class People(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    birth = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    skin_color= db.Column(db.String(250), nullable=False)
    image_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Vehicles(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    capacity = db.Column(db.String(250), nullable=False)
    image_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }   
                    
class Favorites(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(250), nullable=False)
    peopler_id = db.Column(db.Integer, nullable=False)
    planets_id = db.Column(db.Integer, nullable=False)
    vehicles_id = db.Column(db.Integer, nullable=False)
    # user_id = db.Column(db.Integer, "ForeignKey('user.id'))"
    # user = relationship(user)
    # people_id = db.Column(db.Integer, "ForeignKey('people.id'))"
    # people = relationship(People)
    # planets_id = db.Column(db.Integer, "ForeignKey('planets.id'))"
    # planets = relationship(Planets)
    # vehicles_id = db.Column(db.Integer, "ForeignKey('vehicles.id'))""
    # vehicles = relationship(Vehicles)

    def __repr__(self):
        return '<Favorites %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
