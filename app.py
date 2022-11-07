from weather_station_api import create_app


app = create_app()


if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]

    app.run(host=APP_HOST, port=APP_PORT, threaded=True)
