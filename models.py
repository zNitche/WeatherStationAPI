from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    weather_data = db.relationship("WeatherData", backref="day", lazy=True)


class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    day_id = db.Column(db.Integer, db.ForeignKey("day.id"), nullable=False)
