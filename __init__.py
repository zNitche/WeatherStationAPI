from flask import Flask
from models import db
import os


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.secret_key = os.urandom(25)

    db.init_app(app)

    with app.app_context():
        db.create_all()

        from routes import api, errors

        app.register_blueprint(api.api_)
        app.register_blueprint(errors.errors_)

        return app
