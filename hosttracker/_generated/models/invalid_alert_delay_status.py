from typing import Literal

InvalidAlertDelayStatus = Literal[422]

INVALID_ALERT_DELAY_STATUS_VALUES: set[InvalidAlertDelayStatus] = {
    422,
}


def check_invalid_alert_delay_status(value: int) -> InvalidAlertDelayStatus:
    if value in INVALID_ALERT_DELAY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_ALERT_DELAY_STATUS_VALUES!r}")
