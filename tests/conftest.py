import pytest
from weather_station_api import models
from weather_station_api import create_app
from tests.test_config import TestConfig
from tests.consts import LogsConsts


@pytest.fixture(scope="function")
def new_temp_log():
    log = models.TempLog(day_id=1, value=LogsConsts.TEMP_VALUE)

    return log


@pytest.fixture(scope="function")
def new_humi_log():
    log = models.HumidityLog(day_id=1, value=LogsConsts.HUMIDITY_VALUE)

    return log


@pytest.fixture(scope="function")
def new_battery_voltage_log():
    log = models.BatteryVoltageLog(day_id=1, value=LogsConsts.BATTER_VOLTAGE_VALUE)

    return log


@pytest.fixture(scope="session")
def test_client():
    flask_app = create_app(app_config=TestConfig)
    client = flask_app.test_client()

    with flask_app.test_request_context():
        yield client
