from typing import Literal

MethodNotAllowedType = Literal["https://api2.host-tracker.com/problems/method-not-allowed"]

METHOD_NOT_ALLOWED_TYPE_VALUES: set[MethodNotAllowedType] = {
    "https://api2.host-tracker.com/problems/method-not-allowed",
}


def check_method_not_allowed_type(value: str) -> MethodNotAllowedType:
    if value in METHOD_NOT_ALLOWED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {METHOD_NOT_ALLOWED_TYPE_VALUES!r}")
