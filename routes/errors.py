from flask import Blueprint, jsonify, make_response
from flask import current_app as app


errors_ = Blueprint("errors", __name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(error=str(error)), 404)


@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify(error=str(error)), 500)


@app.errorhandler(401)
def non_authenticated(error):
    return make_response(jsonify(error=str(error)), 401)


@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify(error=str(error)), 405)
