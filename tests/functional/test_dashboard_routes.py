from flask import url_for
from weather_station_api.utils import data_utils


def test_home_page(test_client):
    response = test_client.get(url_for("dashboard.home"), follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("dashboard.home")


def test_logs_preview_page(test_client):
    logs_types = data_utils.get_logs_types()

    for log_type in logs_types:
        url = url_for("dashboard.preview_logs_by_type", log_type=log_type)

        response = test_client.get(url, follow_redirects=True)

        assert response.status_code == 200
        assert response.request.path == url
