from datetime import datetime
from weather_station_api.consts import DataConsts
from weather_station_api import db


class LoggedDay(db.Model):
    __tablename__ = "logged_days"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now)

    logs = db.relationship("Log", backref="day", lazy=True)

    def get_logs_by_type(self, type):
        logs = Log.query.filter_by(day_id=self.id, log_type=type).all()

        return logs


class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    log_type = db.Column(db.String(64), nullable=False)
    value = db.Column(db.Float, nullable=False)

    day_id = db.Column(db.Integer, db.ForeignKey("logged_days.id"), nullable=False)

    __mapper_args__ = {'polymorphic_on': log_type}

    @staticmethod
    def get_type():
        return None

    @staticmethod
    def get_display_name():
        return None

    @staticmethod
    def get_subclass_by_type(log_type):
        subclass_by_type = None

        for subclass in Log.__subclasses__():
            if subclass.get_type() == log_type:
                subclass_by_type = subclass

                break

        return subclass_by_type

    @staticmethod
    def create_from_struct(struct, day_id):
        return None


class TempLog(Log):
    __tablename__ = "temperature_logs"

    id = db.Column(db.Integer, db.ForeignKey("logs.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": DataConsts.TEMPERATURE_TYPE,
    }

    @staticmethod
    def get_type():
        return DataConsts.TEMPERATURE_TYPE

    @staticmethod
    def get_display_name():
        return DataConsts.TEMPERATURE_DISPLAY_NAME

    @staticmethod
    def create_from_struct(struct, day_id):
        model = None
        value = struct.get(DataConsts.VALUE_KEY_NAME)

        if value:
            model = TempLog(value=value, day_id=day_id)

        return model


class HumidityLog(Log):
    __tablename__ = "humidity_logs"

    id = db.Column(db.Integer, db.ForeignKey("logs.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": DataConsts.HUMIDITY_TYPE,
    }

    @staticmethod
    def get_type():
        return DataConsts.HUMIDITY_TYPE

    @staticmethod
    def get_display_name():
        return DataConsts.HUMIDITY_DISPLAY_NAME

    @staticmethod
    def create_from_struct(struct, day_id):
        model = None
        value = struct.get(DataConsts.VALUE_KEY_NAME)

        if value:
            model = HumidityLog(value=value, day_id=day_id)

        return model


class BatteryVoltageLog(Log):
    __tablename__ = "battery_voltage_logs"

    id = db.Column(db.Integer, db.ForeignKey("logs.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": DataConsts.BATTER_VOLTAGE_TYPE_NAME,
    }

    @staticmethod
    def get_type():
        return DataConsts.BATTER_VOLTAGE_TYPE_NAME

    @staticmethod
    def get_display_name():
        return DataConsts.BATTER_VOLTAGE_DISPLAY_NAME

    @staticmethod
    def create_from_struct(struct, day_id):
        model = None
        value = struct.get(DataConsts.VALUE_KEY_NAME)

        if value:
            model = BatteryVoltageLog(value=value, day_id=day_id)

        return model
