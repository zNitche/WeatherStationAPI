from tests.consts import LogsConsts


def test_new_temp_log(new_temp_log):
    assert new_temp_log.day_id == 1
    assert new_temp_log.value == LogsConsts.TEMP_VALUE


def test_new_humi_log(new_humi_log):
    assert new_humi_log.day_id == 1
    assert new_humi_log.value == LogsConsts.HUMIDITY_VALUE


def test_new_battery_voltage_log(new_battery_voltage_log):
    assert new_battery_voltage_log.day_id == 1
    assert new_battery_voltage_log.value == LogsConsts.BATTER_VOLTAGE_VALUE
