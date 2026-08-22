from typing import Literal

UnknownFieldStatus = Literal[422]

UNKNOWN_FIELD_STATUS_VALUES: set[UnknownFieldStatus] = {
    422,
}


def check_unknown_field_status(value: int) -> UnknownFieldStatus:
    if value in UNKNOWN_FIELD_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_FIELD_STATUS_VALUES!r}")
