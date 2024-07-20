from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(_name_)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)
        
        from .error import error as error_blueprint
        app.register_blueprint(error_blueprint)
        
        # Import models so that they are registered with SQLAlchemy
        from . import models

        return app