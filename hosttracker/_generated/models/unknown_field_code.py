from typing import Literal

UnknownFieldCode = Literal["unknown_field"]

UNKNOWN_FIELD_CODE_VALUES: set[UnknownFieldCode] = {
    "unknown_field",
}


def check_unknown_field_code(value: str) -> UnknownFieldCode:
    if value in UNKNOWN_FIELD_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_FIELD_CODE_VALUES!r}")
