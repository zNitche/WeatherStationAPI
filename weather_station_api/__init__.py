from flask import Flask
from weather_station_api.models import db
from config import AppConfig
import os


def register_blueprints(app):
    from weather_station_api.blueprints.api.routes import api
    from weather_station_api.blueprints.errors.routes import errors

    app.register_blueprint(api)
    app.register_blueprint(errors)


def create_app(app_config=AppConfig):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_config)
    app.secret_key = os.urandom(25)

    db.init_app(app)

    with app.app_context():
        db.create_all()

        register_blueprints(app)

        return app
