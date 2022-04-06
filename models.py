from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class WeatherLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
