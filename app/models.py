from . import db

class User(UserMixin, db.model):
    """
    class that describes the users on the app
    """

    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key= True)
    username = db.column(db.string(255)index=True)
    email = db.Column(db.string(255)index=True)
    password_hashed = db.Column(db.string(255))
    avatar = db.Column(db.string)

    # toDo add the relationships between tables