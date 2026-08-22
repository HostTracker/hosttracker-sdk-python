from typing import Literal

MethodNotAllowedCode = Literal["method_not_allowed"]

METHOD_NOT_ALLOWED_CODE_VALUES: set[MethodNotAllowedCode] = {
    "method_not_allowed",
}


def check_method_not_allowed_code(value: str) -> MethodNotAllowedCode:
    if value in METHOD_NOT_ALLOWED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {METHOD_NOT_ALLOWED_CODE_VALUES!r}")
