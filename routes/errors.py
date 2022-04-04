from flask import Blueprint, jsonify
from flask import current_app as app


errors_ = Blueprint("errors", __name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify(error=404, text=str(error))


@app.errorhandler(500)
def overloaded(error):
    return jsonify(error=500, text=str(error))


@app.errorhandler(401)
def non_authenticated(error):
    return jsonify(error=401, text=str(error))


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(error=405, text=str(error))
