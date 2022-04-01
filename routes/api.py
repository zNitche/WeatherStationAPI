from flask import Blueprint, jsonify


api_ = Blueprint("api", __name__)


@api_.route("/")
def hello():
    return jsonify(hello="Hello")
