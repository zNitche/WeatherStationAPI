from functools import wraps
from flask import abort, request
from config import AppConfig
from weather_station_api.consts import ApiConsts


def auth_token_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_token = request.headers.get(ApiConsts.AUTH_TOKEN_KEY_NAME)

        if auth_token and auth_token == AppConfig.API_AUTH_TOKEN:
            return func(*args, **kwargs)

        else:
            abort(403)

    return decorated_function
