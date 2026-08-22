from typing import Literal

UnknownEnumValueCode = Literal["unknown_enum_value"]

UNKNOWN_ENUM_VALUE_CODE_VALUES: set[UnknownEnumValueCode] = {
    "unknown_enum_value",
}


def check_unknown_enum_value_code(value: str) -> UnknownEnumValueCode:
    if value in UNKNOWN_ENUM_VALUE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_ENUM_VALUE_CODE_VALUES!r}")
