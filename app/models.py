from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.model):
    """
    class that describes the users on the app
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(255), index=True)
    email = db.Column(db.String(255), index=True)
    password_hashed = db.Column(db.String(255))
    avatar = db.Column(db.String)

    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hashed = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hashed, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.model):
    """
    class that defines the pitches
    """

    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key=True)
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.String(255))
    pitch_actual = db.Column(db.String)




    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category_id).all()
        return pitches

class Categeory(db.model):
    """
    class that defines the categories of the pitches
    """

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='category', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
