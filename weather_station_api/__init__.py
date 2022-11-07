from flask import Flask
import flask_migrate
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import AppConfig
import os


db = SQLAlchemy()
migrate = Migrate(compare_type=True)


def init_migrations(app):
    migrations_dir_path = app.config["MIGRATIONS_DIR_PATH"]

    migrate.init_app(app, db, directory=migrations_dir_path)

    if not os.path.exists(migrations_dir_path):
        flask_migrate.init(migrations_dir_path)

    flask_migrate.migrate(migrations_dir_path)
    flask_migrate.upgrade(migrations_dir_path)


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

    from weather_station_api import models

    with app.app_context():
        db.create_all()

        if not app.config["TESTING"]:
            init_migrations(app)

        register_blueprints(app)

        return app
