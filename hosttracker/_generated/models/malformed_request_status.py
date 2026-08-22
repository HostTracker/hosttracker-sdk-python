from typing import Literal

MalformedRequestStatus = Literal[400]

MALFORMED_REQUEST_STATUS_VALUES: set[MalformedRequestStatus] = {
    400,
}


def check_malformed_request_status(value: int) -> MalformedRequestStatus:
    if value in MALFORMED_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MALFORMED_REQUEST_STATUS_VALUES!r}")
