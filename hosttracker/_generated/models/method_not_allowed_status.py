from typing import Literal

MethodNotAllowedStatus = Literal[405]

METHOD_NOT_ALLOWED_STATUS_VALUES: set[MethodNotAllowedStatus] = {
    405,
}


def check_method_not_allowed_status(value: int) -> MethodNotAllowedStatus:
    if value in METHOD_NOT_ALLOWED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {METHOD_NOT_ALLOWED_STATUS_VALUES!r}")
