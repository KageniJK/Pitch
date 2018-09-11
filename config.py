import os


class Config:
    """
    class that set the general config
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/profile_pics'

    # email configurations

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    """
    class that sets up production config
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


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