"""
Datu bāzes inicializācija
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.reflect()
        print(db.Model.metadata.tables.keys())

    return app
