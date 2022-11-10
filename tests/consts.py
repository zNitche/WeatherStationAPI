class LogsConsts:
    TEMP_VALUE = 5
    HUMIDITY_VALUE = 10
    BATTER_VOLTAGE_VALUE = 3

    TEMP_LOG_STRUCT = {
        "value": TEMP_VALUE
    }

    HUMI_LOG_STRUCT = {
        "value": HUMIDITY_VALUE
    }

    BATTERY_VOLTAGE_LOG_STRUCT = {
        "value": BATTER_VOLTAGE_VALUE
    }

    LOGS_CREATION_STRUCT = {
        "temperature": TEMP_LOG_STRUCT,
        "humidity": HUMI_LOG_STRUCT,
        "battery_voltage": BATTERY_VOLTAGE_LOG_STRUCT
    }
