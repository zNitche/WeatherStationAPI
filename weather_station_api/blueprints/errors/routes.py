from flask import Blueprint, make_response, jsonify


errors = Blueprint("errors", __name__, template_folder="templates", static_folder="static")


@errors.app_errorhandler(404)
def error_404(error):
    return make_response(jsonify(error=str(error), status_code=404), 404)


@errors.app_errorhandler(500)
def error_500(error):
    return make_response(jsonify(error=str(error), status_code=500), 500)


@errors.app_errorhandler(405)
def error_405(error):
    return make_response(jsonify(error=str(error), status_code=405), 405)


@errors.app_errorhandler(403)
def error_403(error):
    return make_response(jsonify(error=str(error), status_code=403), 403)


@errors.app_errorhandler(400)
def error_400(error):
    return make_response(jsonify(error=str(error), status_code=400), 400)
