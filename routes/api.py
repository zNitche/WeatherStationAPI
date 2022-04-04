from flask import Blueprint, jsonify
from models import Day


api_ = Blueprint("api", __name__)


@api_.route("/api/days")
def get_days():
    return jsonify(days=[day.date.strftime("%x") for day in Day.query.all()])
