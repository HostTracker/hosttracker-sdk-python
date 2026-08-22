from typing import Literal

InvalidIntervalStatus = Literal[422]

INVALID_INTERVAL_STATUS_VALUES: set[InvalidIntervalStatus] = {
    422,
}


def check_invalid_interval_status(value: int) -> InvalidIntervalStatus:
    if value in INVALID_INTERVAL_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_INTERVAL_STATUS_VALUES!r}")
