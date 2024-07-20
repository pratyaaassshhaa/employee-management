from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(_name_)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

        # Import models so that they are registered with SQLAlchemy
        from . import models
        return app