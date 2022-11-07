import os


class AppConfig:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    DATABASE_PATH = os.environ.get("DATABASE_PATH", default=os.path.join(CURRENT_DIR, "data", "database.db"))

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
