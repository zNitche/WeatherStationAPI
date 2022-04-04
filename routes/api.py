from flask import Blueprint, jsonify
from models import Log


api_ = Blueprint("api", __name__)


@api_.route("/api/days", methods=["GET"])
def get_logged_days():
    logged_days = []

    for date in Log.query.all():
        if date not in logged_days:
            logged_days.append(date)

    return jsonify(days=[date.date.strftime("%m-%d-%Y") for date in logged_days])


@api_.route("/api/weather_data/<day_date>", methods=["GET"])
def get_weather_data(day_date):
    data = []

    matching_days = [log for log in Log.query.all() if log.date.strftime("%m-%d-%Y") == day_date]

    if len(matching_days) > 0:
        log_data = matching_days[0]

        for data_entry in log_data.weather_data:
            data.append({
                "time": log_data.date.strftime("%H:%M:%S"),
                "temperature": data_entry.temperature,
                "humidity": data_entry.humidity,
            })

    return jsonify(data=data)
