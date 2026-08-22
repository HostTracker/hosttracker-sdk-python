from typing import Literal

InvalidAlertDelayCode = Literal["invalid_alert_delay"]

INVALID_ALERT_DELAY_CODE_VALUES: set[InvalidAlertDelayCode] = {
    "invalid_alert_delay",
}


def check_invalid_alert_delay_code(value: str) -> InvalidAlertDelayCode:
    if value in INVALID_ALERT_DELAY_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_ALERT_DELAY_CODE_VALUES!r}")
