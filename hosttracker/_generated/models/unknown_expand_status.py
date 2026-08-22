from typing import Literal

UnknownExpandStatus = Literal[422]

UNKNOWN_EXPAND_STATUS_VALUES: set[UnknownExpandStatus] = {
    422,
}


def check_unknown_expand_status(value: int) -> UnknownExpandStatus:
    if value in UNKNOWN_EXPAND_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_EXPAND_STATUS_VALUES!r}")
