import os


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    SQLALCHEMY_DATABASE_URI = f"sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = False
