import dotenv
import os


dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env"))


class AppConfig:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    DATABASE_PATH = os.path.join(CURRENT_DIR, "data", "database.db")
    MIGRATIONS_DIR_PATH = os.path.join(CURRENT_DIR, "data", "migrations")

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_PORT = 8080
    APP_HOST = "0.0.0.0"

    API_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
