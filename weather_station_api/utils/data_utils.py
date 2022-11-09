from weather_station_api.consts import DataConsts, DateConsts


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


def create_log_from_struct(model, struct):
    value = struct.get(DataConsts.VALUE_KEY_NAME)

    return model(value=value)


def get_daily_logs_struct(logs):
    struct = {}

    for log in logs:
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
