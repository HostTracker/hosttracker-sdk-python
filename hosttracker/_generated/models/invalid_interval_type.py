from typing import Literal

InvalidIntervalType = Literal["https://api2.host-tracker.com/problems/invalid-interval"]

INVALID_INTERVAL_TYPE_VALUES: set[InvalidIntervalType] = {
    "https://api2.host-tracker.com/problems/invalid-interval",
}


def check_invalid_interval_type(value: str) -> InvalidIntervalType:
    if value in INVALID_INTERVAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_INTERVAL_TYPE_VALUES!r}")
