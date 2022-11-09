from weather_station_api.consts import DateConsts
from weather_station_api import models
from weather_station_api.utils import db_utils


def get_logged_day(day_date):
    log_day = [logged_day for logged_day in models.LoggedDay.query.all()
               if logged_day.date.strftime(DateConsts.DAY_FORMATTING) == day_date]

    log_day = log_day[0] if len(log_day) > 0 else None

    if log_day is None:
        log_day = models.LoggedDay()
        db_utils.add_object_to_db(log_day)

    return log_day


def get_logged_days(model):
    days = []

    for day in [log.date for log in model.query.all()]:
        day_str = day.strftime(DateConsts.DAY_FORMATTING)

        if day_str not in days:
            days.append(day_str)

    return days


def get_logged_data_struct(model):
    struct = {log.date: log.value for log in model.query.all()}

    return struct


def get_daily_logs_struct(logged_days, log_type):
    struct = {}

    for log_day in logged_days:
        logs_by_type = log_day.get_logs_by_type(log_type)

        for log in logs_by_type:
            log_day_date = log.date.strftime(DateConsts.DAY_FORMATTING)

            if log_day_date not in struct.keys():
                struct[log_day_date] = []

            struct[log_day_date].append({
                "time": log.date.strftime(DateConsts.HOUR_FORMATTING),
                "value": log.value
            })

    return struct


def serialize_daily_logs_struct(logs_struct):
    serialized_struct = []

    for day, data in logs_struct.items():
        day_data = {
            "day": day,
            "data": data
        }

        serialized_struct.append(day_data)

    return serialized_struct
