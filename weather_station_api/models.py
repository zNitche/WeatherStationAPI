from datetime import datetime
from weather_station_api.consts import DataConsts
from weather_station_api import db


class LogBase:
    @staticmethod
    def get_type():
        return None

    @staticmethod
    def get_subclass_by_type(log_type):
        subclass_by_type = None

        for subclass in LogBase.__subclasses__():
            if subclass.get_type() == log_type:
                subclass_by_type = subclass

                break

        return subclass_by_type


class TempLog(db.Model, LogBase):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    value = db.Column(db.Float, nullable=False)

    @staticmethod
    def get_type():
        return DataConsts.TEMPERATURE_TYPE


class HumidityLog(db.Model, LogBase):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    value = db.Column(db.Float, nullable=False)

    @staticmethod
    def get_type():
        return DataConsts.HUMIDITY_TYPE


class BatteryVoltageLog(db.Model, LogBase):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    value = db.Column(db.Float, nullable=False)

    @staticmethod
    def get_type():
        return DataConsts.BATTER_VOLTAGE_TYPE_NAME
