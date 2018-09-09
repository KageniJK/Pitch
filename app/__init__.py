from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    """
    creating the app instance while taking in the config
    :param config_name:
    :return:
    """

    app = Flask(__name__)



    # creating from config

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # initialising the app
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app