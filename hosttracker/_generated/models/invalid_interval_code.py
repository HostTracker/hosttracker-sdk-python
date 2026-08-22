from typing import Literal

InvalidIntervalCode = Literal["invalid_interval"]

INVALID_INTERVAL_CODE_VALUES: set[InvalidIntervalCode] = {
    "invalid_interval",
}


def check_invalid_interval_code(value: str) -> InvalidIntervalCode:
    if value in INVALID_INTERVAL_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_INTERVAL_CODE_VALUES!r}")
