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


class ModulesConfig:
    MODULE_CDN_KEY = "cdn"
    MODULE_LOCAL_KEY = "local"
    MODULE_LOCAL_STATIC_KEY = "static"

    CHART_JS_NAME = "ChartJS"
    CHART_JS_LOCAL_STATIC_PATH = os.path.join("js", "libs", "chart.js")
    CHART_JS_LOCAL_PATH = os.path.join(AppConfig.CURRENT_DIR,
                                       "weather_station_api", "static", CHART_JS_LOCAL_STATIC_PATH)

    CHART_JS_CDN_ADDRESS = "https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"

    MODULES_CONFIG = {
        CHART_JS_NAME: {
            MODULE_LOCAL_KEY: CHART_JS_LOCAL_PATH,
            MODULE_CDN_KEY: CHART_JS_CDN_ADDRESS,
            MODULE_LOCAL_STATIC_KEY: CHART_JS_LOCAL_STATIC_PATH
        }
    }
