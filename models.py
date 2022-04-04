from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
