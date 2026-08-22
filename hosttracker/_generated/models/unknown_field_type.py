from typing import Literal

UnknownFieldType = Literal["https://api2.host-tracker.com/problems/unknown-field"]

UNKNOWN_FIELD_TYPE_VALUES: set[UnknownFieldType] = {
    "https://api2.host-tracker.com/problems/unknown-field",
}


def check_unknown_field_type(value: str) -> UnknownFieldType:
    if value in UNKNOWN_FIELD_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_FIELD_TYPE_VALUES!r}")
