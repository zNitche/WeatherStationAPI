from flask import Blueprint, make_response


errors = Blueprint("errors", __name__, template_folder="templates", static_folder="static")


@errors.app_errorhandler(404)
def error_404(error):
    return make_response({"error": str(error)}, 404)


@errors.app_errorhandler(500)
def error_500(error):
    return make_response({"error": str(error)}, 500)


@errors.app_errorhandler(405)
def error_405(error):
    return make_response({"error": str(error)}, 405)


@errors.app_errorhandler(403)
def error_403(error):
    return make_response({"error": str(error)}, 403)


@errors.app_errorhandler(400)
def error_400(error):
    return make_response({"error": str(error)}, 400)
