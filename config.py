"""
Konfigurācija
"""

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    FLASK_ENV = environ.get('FLASK_ENV')

    SECRET_KEY = "4fd94ac7-c66f-4624-801e-25681c5383d8"
    STATIC_FOLDER = 'static'
    STATIC_URL_PATH = '/static'

    POSTGRES_URL = environ.get('POSTGRES_URL')
    POSTGRES_USER = environ.get('POSTGRES_USER')
    POSTGRES_PW = environ.get('POSTGRES_PW')
    POSTGRES_DB = environ.get('POSTGRES_DB')
    POSTGRES_PORT = environ.get('POSTGRES_PORT')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}:{POSTGRES_PORT}/{POSTGRES_DB}"

