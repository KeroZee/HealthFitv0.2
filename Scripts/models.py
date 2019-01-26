from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from Scripts import db, login_manager, app
from flask_login import UserMixin
app.config['WHOOSH_BASE'] = 'path/to/whoosh/base'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(20), unique=True, nullable=False )
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    schedule = db.relationship('Schedule', backref='name', lazy=True)
    breakfast = db.relationship('Breakfast', backref='name', lazy=True)
    lunch = db.relationship('Lunch', backref='name', lazy=True)
    dinner = db.relationship('Dinner', backref='name', lazy=True)
    exercise = db.relationship('Fitness', backref='name', lazy=True)
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    HeartRate = db.Column(db.Integer)
    Glucose_Level = db.Column(db.Integer)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__(self): #How objects are printed
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    description = db.Column(db.String(500), nullable=False)
    remarks = db.Column(db.String(500), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self): #How objects are printed
        return f"User('{self.date_posted}', '{self.description}', '{self.remarks}')"

class Food(db.Model):
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.Integer(), nullable=False)
    calories = db.Column(db.Integer(), nullable=False)
    protein = db.Column(db.Integer(), nullable=False)
    carbohydrates = db.Column(db.Integer(), nullable=False)
    fats = db.Column(db.Integer(), nullable=False)

    def __repr__(self): #How objects are printed
        return f"Food('{self.name}', '{self.mass}')"

class Fitness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercisename = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer(), nullable=False)
    intensity = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self): #How objects are printed
        return f"Fitness('{self.name}', '{self.duration}')"

class Breakfast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodname = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.Integer(), nullable=False)
    calories = db.Column(db.Integer(), nullable=False)
    protein = db.Column(db.Integer(), nullable=False)
    carbohydrates = db.Column(db.Integer(), nullable=False)
    fats = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Lunch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodname = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.Integer(), nullable=False)
    calories = db.Column(db.Integer(), nullable=False)
    protein = db.Column(db.Integer(), nullable=False)
    carbohydrates = db.Column(db.Integer(), nullable=False)
    fats = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Dinner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodname = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.Integer(), nullable=False)
    calories = db.Column(db.Integer(), nullable=False)
    protein = db.Column(db.Integer(), nullable=False)
    carbohydrates = db.Column(db.Integer(), nullable=False)
    fats = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class HealthTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    heartrate = db.Column(db.Integer(), nullable=False)
