from typing import Literal

MalformedRequestCode = Literal["malformed_request"]

MALFORMED_REQUEST_CODE_VALUES: set[MalformedRequestCode] = {
    "malformed_request",
}


def check_malformed_request_code(value: str) -> MalformedRequestCode:
    if value in MALFORMED_REQUEST_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MALFORMED_REQUEST_CODE_VALUES!r}")
