from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name):
    """
    creating the app instance while taking in the config
    :param config_name:
    :return:
    """

    app = Flask(__name__)

    # creatinmg from config

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
