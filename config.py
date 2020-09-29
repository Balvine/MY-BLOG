
import os


class Config:
        """
        General configuration parent class
        """
        SECRET_KEY = 'barl'
        #SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/pitches'
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guesss'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        UPLOADED_PHOTOS_DEST = 'app/static/photos'
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
        
        MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
        print(MAIL_PASSWORD)

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog'
    DEGUG = True
class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with General
        configuration settings
    """
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """
    Development configuration child class
    Args:
    Config: The parent configuration class with General
    configuration settings
    """
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog'
    # SECRET_KEY = os.urandom(38)
    DEBUG = True
    
    
    

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 