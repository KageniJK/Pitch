from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """
    class that defines the users
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index = True)
    avatar = db.Column(db.String())
    password_hashed = db.Column(db.String(255))

    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hashed= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hashed, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    """
    class that defines the pitches
    """

    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    pitch_actual = db.Column(db.String)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category=id).all()
        return pitches


class Comment(db.Model):
    """
    class that defines the comments on pitches
    """

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        comments = Pitch.query.filter_by(pitch_id=id).all()
        return comments
