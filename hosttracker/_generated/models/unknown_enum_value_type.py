from typing import Literal

UnknownEnumValueType = Literal["https://api2.host-tracker.com/problems/unknown-enum-value"]

UNKNOWN_ENUM_VALUE_TYPE_VALUES: set[UnknownEnumValueType] = {
    "https://api2.host-tracker.com/problems/unknown-enum-value",
}


def check_unknown_enum_value_type(value: str) -> UnknownEnumValueType:
    if value in UNKNOWN_ENUM_VALUE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_ENUM_VALUE_TYPE_VALUES!r}")
