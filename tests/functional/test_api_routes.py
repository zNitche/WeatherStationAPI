from flask import url_for
from weather_station_api import models
from weather_station_api.utils import data_utils
from weather_station_api.consts import ApiConsts, DateConsts
from tests.consts import LogsConsts
from tests.test_config import TestConfig


def test_get_log_types(test_client):
    response = test_client.get(url_for("api.get_logs_types"), follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("api.get_logs_types")

    assert response.json == data_utils.get_logs_types()


def test_add_weather_log(test_client):
    logs_types = data_utils.get_logs_types()

    for log_type in logs_types:
        url = url_for("api.add_weather_log", log_type=log_type)
        log_creation_struct = LogsConsts.LOGS_CREATION_STRUCT[log_type]

        response = test_client.post(url, headers={ApiConsts.AUTH_TOKEN_KEY_NAME: TestConfig.API_AUTH_TOKEN},
                                    json=log_creation_struct, follow_redirects=True)

        assert response.status_code == 200


def test_get_logged_days_by_type(test_client):
    logs_types = data_utils.get_logs_types()

    for log_type in logs_types:
        url = url_for("api.get_logged_days_by_type", log_type=log_type)

        response = test_client.get(url, follow_redirects=True)

        assert response.status_code == 200
        assert response.request.path == url

        log_by_type = models.Log.get_subclass_by_type(log_type)

        assert log_by_type is not None

        logged_days = data_utils.get_logged_days(log_by_type)
        serialized_logged_days = [day.date.strftime(DateConsts.DAY_FORMATTING) for day in models.LoggedDay.query.all()]

        assert logged_days == serialized_logged_days


def test_get_logs_data_by_type(test_client):
    logs_types = data_utils.get_logs_types()

    for log_type in logs_types:
        url = url_for("api.get_logs_data_by_type", log_type=log_type)

        response = test_client.get(url, follow_redirects=True)

        assert response.status_code == 200
        assert response.request.path == url


def test_get_logs_data_by_day_and_type(test_client):
    logs_types = data_utils.get_logs_types()

    for log_type in logs_types:
        log_by_type = models.Log.get_subclass_by_type(log_type)
        logged_days = data_utils.get_logged_days(log_by_type)

        for day_date in logged_days:
            url = url_for("api.get_logs_data_by_day_and_type", log_type=log_type, day_date=day_date)

            response = test_client.get(url, follow_redirects=True)

            assert response.status_code == 200
            assert response.request.path == url
