from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    weather_data = db.relationship("WeatherData", backref="log", lazy=True)


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    station_log_id = db.Column(db.Integer, db.ForeignKey("log.id"), nullable=False)
