from weather_station_api.consts import DataConsts, DateConsts


def get_value_from_dict(key, dict):
    value = dict[key] if key in dict.keys() else None

    return value


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


def create_from_struct(model, struct):
    value = get_value_from_dict(DataConsts.VALUE_KEY_NAME, struct)

    return model(value=value)
