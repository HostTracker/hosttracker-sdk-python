from typing import Literal

InvalidAlertDelayType = Literal["https://api2.host-tracker.com/problems/invalid-alert-delay"]

INVALID_ALERT_DELAY_TYPE_VALUES: set[InvalidAlertDelayType] = {
    "https://api2.host-tracker.com/problems/invalid-alert-delay",
}


def check_invalid_alert_delay_type(value: str) -> InvalidAlertDelayType:
    if value in INVALID_ALERT_DELAY_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_ALERT_DELAY_TYPE_VALUES!r}")
