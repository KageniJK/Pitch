import os


class Config:
    """
    class that set the general config
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    """
    class that sets up production config
    """

    pass


class DevConfig(Config):
    """
    class that sets up the development config
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qagz:password@localhost/pitch'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}