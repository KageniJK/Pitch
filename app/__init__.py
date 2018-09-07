from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()


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

    db.init_app(app)

    from .main import main as main_blueprint

