class ApiConsts:
    AUTH_TOKEN_KEY_NAME = "auth_token"
    LOG_TYPE_KEY_NAME = "type"
    LOG_CONTENT_KEY_NAME = "content"


class DataConsts:
    TEMPERATURE_TYPE = "temperature"
    HUMIDITY_TYPE = "humidity"
    BATTER_VOLTAGE_TYPE_NAME = "battery_voltage"

    TEMPERATURE_DISPLAY_NAME = "temperature"
    HUMIDITY_DISPLAY_NAME = "humidity"
    BATTER_VOLTAGE_DISPLAY_NAME = "battery voltage"

    VALUE_KEY_NAME = "value"


class DateConsts:
    HOUR_FORMATTING = "%H:%M:%S"
    DAY_FORMATTING = "%d-%m-%Y"


class PaginationConsts:
    # 7 days * 24 logs per day
    LOGS_DATA_PER_PAGE = 7 * 24
