from flask import Blueprint, jsonify, request
import json
from datetime import datetime
from models import WeatherLog
from utils import db_utils
from consts import ApiConsts, DataConsts, DateConsts


api_ = Blueprint("api", __name__)


@api_.route("/api/days", methods=["GET"])
def get_logged_days():
    logged_days = []

    for log in WeatherLog.query.all():
        date_str = log.date.strftime(DateConsts.DAY_FORMATTING)

        if date_str not in logged_days:
            logged_days.append(date_str)

    return jsonify(days=logged_days)


@api_.route("/api/weather_data/<day_date>", methods=["GET"])
def get_weather_data(day_date):
    data = []

    matching_logs = [log for log in WeatherLog.query.all() if log.date.strftime(DateConsts.DAY_FORMATTING) == day_date]

    for matching_log in matching_logs:
        data.append({
            DataConsts.TIME_KEY_NAME: matching_log.date.strftime(DateConsts.HOUR_FORMATTING),
            DataConsts.TEMPERATURE_KEY_NAME: matching_log.temperature,
            DataConsts.HUMIDITY_KEY_NAME: matching_log.humidity,
        })

    return jsonify(data=data)


@api_.route("/api/log/weather", methods=["POST"])
def add_weather_log():
    response = ApiConsts.POST_FAILED_MESSAGE

    data = request.data

    if data:
        try:
            parsed_data = json.loads(data.decode(ApiConsts.REQUESTS_ENCODING))

            temperature = parsed_data[DataConsts.TEMPERATURE_KEY_NAME]
            humidity = parsed_data[DataConsts.HUMIDITY_KEY_NAME]

            data_log = WeatherLog(date=datetime.now(), temperature=temperature, humidity=humidity)

            db_utils.add_object_to_db(data_log)

            response = ApiConsts.POST_SUCCESS_MESSAGE

        except:
            pass

    return jsonify(status=response)
