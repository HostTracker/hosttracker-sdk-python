from typing import Literal

MalformedRequestType = Literal["https://api2.host-tracker.com/problems/malformed-request"]

MALFORMED_REQUEST_TYPE_VALUES: set[MalformedRequestType] = {
    "https://api2.host-tracker.com/problems/malformed-request",
}


def check_malformed_request_type(value: str) -> MalformedRequestType:
    if value in MALFORMED_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MALFORMED_REQUEST_TYPE_VALUES!r}")
