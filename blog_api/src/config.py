# /src/config.py

import os


def set_environment_variable():
    os.environ["FLASK_ENV"] = "development"
    os.environ["DATABASE_URL"] = 'postgres://name:password@houst:port/blog_api_db'
    os.environ["JWT_SECRET_KEY"] = 'hhgaghhgsdhdhdd'


class Development(object):
    """
    Development environment configuration
    """
    set_environment_variable()
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'  # os.getenv('JWT_SECRET_KEY')
    SQLAlchemy_DATABASE_URI = 'postgres://name:password@houst:port/blog_api_db'  # os.getenv('DATABASE_URL')


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLAlchemy_DATABASE_URI = 'postgres://name:password@houst:port/blog_api_db'  # os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'   # os.getenv('JWT_SECRET_KEY')


app_config = {
    'development': Development,
    'production': Production,
}