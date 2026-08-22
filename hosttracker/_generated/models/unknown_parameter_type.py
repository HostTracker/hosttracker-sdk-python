from typing import Literal

UnknownParameterType = Literal["https://api2.host-tracker.com/problems/unknown-parameter"]

UNKNOWN_PARAMETER_TYPE_VALUES: set[UnknownParameterType] = {
    "https://api2.host-tracker.com/problems/unknown-parameter",
}


def check_unknown_parameter_type(value: str) -> UnknownParameterType:
    if value in UNKNOWN_PARAMETER_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_PARAMETER_TYPE_VALUES!r}")
