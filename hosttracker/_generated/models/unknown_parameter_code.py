from typing import Literal

UnknownParameterCode = Literal["unknown_parameter"]

UNKNOWN_PARAMETER_CODE_VALUES: set[UnknownParameterCode] = {
    "unknown_parameter",
}


def check_unknown_parameter_code(value: str) -> UnknownParameterCode:
    if value in UNKNOWN_PARAMETER_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_PARAMETER_CODE_VALUES!r}")
