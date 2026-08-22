from typing import Literal

UnknownParameterStatus = Literal[422]

UNKNOWN_PARAMETER_STATUS_VALUES: set[UnknownParameterStatus] = {
    422,
}


def check_unknown_parameter_status(value: int) -> UnknownParameterStatus:
    if value in UNKNOWN_PARAMETER_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_PARAMETER_STATUS_VALUES!r}")
