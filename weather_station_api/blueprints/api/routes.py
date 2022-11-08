from flask import Blueprint, jsonify, request, make_response, abort
from weather_station_api import models
from weather_station_api.utils import db_utils, data_utils
from weather_station_api.consts import DateConsts, ApiConsts
from weather_station_api.app_modules import decorators


api = Blueprint("api", __name__, template_folder="templates", static_folder="static", url_prefix="/api")


@api.route("/logs/types", methods=["GET"])
def get_logs_types():
    types = []

    for log in models.LogBase.__subclasses__():
        types.append(log.get_type())

    return make_response(jsonify(types), 200)


@api.route("/logs/<log_type>/logged_days", methods=["GET"])
def get_logged_days_by_type(log_type):
    log_by_type = models.LogBase.get_subclass_by_type(log_type)

    if log_by_type:
        logged_days = data_utils.get_logged_days(log_by_type)

        return make_response(jsonify(logged_days), 200)

    else:
        abort(404)


@api.route("/logs/<log_type>/data", methods=["GET"])
def get_logs_data_by_type(log_type):
    log_by_type = models.LogBase.get_subclass_by_type(log_type)

    if log_by_type:
        data = data_utils.get_logged_data_struct(log_by_type)
        serialized_data = {str(key): data[key] for key, value in data.items()}

        return make_response(jsonify(serialized_data), 200)

    else:
        abort(404)


@api.route("/logs/<log_type>/<day_date>/data", methods=["GET"])
def get_logs_data_by_day_and_type(log_type, day_date):
    log_by_type = models.LogBase.get_subclass_by_type(log_type)

    if log_by_type:
        all_data = data_utils.get_logged_data_struct(log_by_type)

        picked_data = {str(date): value for date, value in all_data.items() if
                       date.strftime(DateConsts.DAY_FORMATTING) == day_date}

        return make_response(jsonify(picked_data), 200)

    else:
        abort(404)


@api.route("/logs/<log_type>/add", methods=["POST"])
@decorators.auth_token_required
def add_weather_log(log_type):
    log_by_type = models.LogBase.get_subclass_by_type(log_type)

    if log_by_type:
        log = data_utils.create_log_from_struct(log_by_type, request.json)

        if log:
            db_utils.add_object_to_db(log)

            return make_response({}, 200)

        else:
            abort(400)

    else:
        abort(404)


@api.route("/logs/add", methods=["POST"])
@decorators.auth_token_required
def add_many_weather_logs():
    logs_struct = request.json

    if logs_struct:
        for log_struct in logs_struct:
            log_by_type = models.LogBase.get_subclass_by_type(log_struct.get(ApiConsts.LOG_TYPE_KEY_NAME))

            if log_by_type:
                log = data_utils.create_log_from_struct(log_by_type, log_struct.get(ApiConsts.LOG_CONTENT_KEY_NAME))

                if log:
                    db_utils.add_object_to_db(log)

            else:
                abort(400)

        return make_response({}, 200)

    else:
        abort(404)
