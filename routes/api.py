from flask import Blueprint, jsonify
from models import Day


api_ = Blueprint("api", __name__)


@api_.route("/api/days", methods=["GET"])
def get_days():
    return jsonify(days=[day.date.strftime("%m-%d-%Y") for day in Day.query.all()])


@api_.route("/api/weather_data/<day_date>", methods=["GET"])
def get_weather_data(day_date):
    data = []

    matching_days = [day for day in Day.query.all() if day.date.strftime("%x") == day_date]

    if len(matching_days) > 0:
        day = matching_days[0]

        for data_entry in day.weather_data:
            data.append({
                "time": data_entry.time.strftime("%H:%M:%S"),
                "temperature": data_entry.temperature,
                "humidity": data_entry.humidity,
            })

    return jsonify(data=data)
