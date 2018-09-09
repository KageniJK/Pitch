from . import db
from flask_login import UserMixin


class User(UserMixin, db.model):
    """
    class that describes the users on the app
    """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(255), index=True)
    email = db.Column(db.String(255), index=True)
    password_hashed = db.Column(db.String(255))
    avatar = db.Column(db.String)

    # toDo add the relationships between tables

class Pitch(db.model):
    """
    class that defines the pitches
    """

    __tablename__='pitches'

    pitch_id = db.Column(db.Integer, primary_key=True)
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
