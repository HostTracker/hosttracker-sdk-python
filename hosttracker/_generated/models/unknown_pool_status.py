from typing import Literal

UnknownPoolStatus = Literal[422]

UNKNOWN_POOL_STATUS_VALUES: set[UnknownPoolStatus] = {
    422,
}


def check_unknown_pool_status(value: int) -> UnknownPoolStatus:
    if value in UNKNOWN_POOL_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_POOL_STATUS_VALUES!r}")
