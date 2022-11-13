from weather_station_api.consts import DateConsts
from weather_station_api import models
from weather_station_api.utils import db_utils


def get_logs_types():
    types = []

    for log in models.Log.__subclasses__():
        types.append(log.get_type())

    return types


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
    logged_days_data = []

    for log_day in logged_days:
        logs_by_type = log_day.get_logs_by_type(log_type)
        day_logged_data = []

        for log in logs_by_type:
            day_logged_data.append({
                "time": log.date.strftime(DateConsts.HOUR_FORMATTING_WO_SECONDS),
                "value": log.value
            })

        logged_days_data.append(
            {
                "day": log_day.date.strftime(DateConsts.DAY_FORMATTING),
                "data": day_logged_data
            }
        )

    return logged_days_data
