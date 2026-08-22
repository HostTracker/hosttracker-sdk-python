from typing import Literal

UnknownExpandType = Literal["https://api2.host-tracker.com/problems/unknown-expand"]

UNKNOWN_EXPAND_TYPE_VALUES: set[UnknownExpandType] = {
    "https://api2.host-tracker.com/problems/unknown-expand",
}


def check_unknown_expand_type(value: str) -> UnknownExpandType:
    if value in UNKNOWN_EXPAND_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_EXPAND_TYPE_VALUES!r}")
