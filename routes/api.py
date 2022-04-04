from flask import Blueprint, jsonify, request
import json
from datetime import datetime
from models import Log, WeatherData
from utils import db_utils


api_ = Blueprint("api", __name__)


@api_.route("/api/days", methods=["GET"])
def get_logged_days():
    logged_days = []

    for log in Log.query.all():
        date_str = log.date.strftime("%m-%d-%Y")

        if date_str not in logged_days:
            logged_days.append(date_str)

    return jsonify(days=logged_days)


@api_.route("/api/weather_data/<day_date>", methods=["GET"])
def get_weather_data(day_date):
    data = []

    matching_logs = [log for log in Log.query.all() if log.date.strftime("%m-%d-%Y") == day_date]

    for matching_log in matching_logs:
        for data_entry in matching_log.weather_data:
            data.append({
                "time": matching_log.date.strftime("%H:%M:%S"),
                "temperature": data_entry.temperature,
                "humidity": data_entry.humidity,
            })

    return jsonify(data=data)


@api_.route("/api/log", methods=["POST"])
def add_station_log():
    response = "FAIL"

    data = request.data

    if data:
        try:
            parsed_data = json.loads(data.decode("utf-8"))

            temp = parsed_data["temperature"]
            humi = parsed_data["humidity"]

            data_log = Log(date=datetime.now(), weather_data=[WeatherData(temperature=temp, humidity=humi)])

            db_utils.add_object_to_db(data_log)

            response = "OK"

        except:
            pass

    return jsonify(status=response)
