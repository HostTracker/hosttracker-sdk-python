from typing import Literal

InvalidRangeStatus = Literal[422]

INVALID_RANGE_STATUS_VALUES: set[InvalidRangeStatus] = {
    422,
}


def check_invalid_range_status(value: int) -> InvalidRangeStatus:
    if value in INVALID_RANGE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_RANGE_STATUS_VALUES!r}")
