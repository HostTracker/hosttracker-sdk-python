from typing import Literal

UnknownEnumValueStatus = Literal[422]

UNKNOWN_ENUM_VALUE_STATUS_VALUES: set[UnknownEnumValueStatus] = {
    422,
}


def check_unknown_enum_value_status(value: int) -> UnknownEnumValueStatus:
    if value in UNKNOWN_ENUM_VALUE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_ENUM_VALUE_STATUS_VALUES!r}")
