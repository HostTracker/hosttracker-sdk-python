from typing import Literal

PayloadTooLargeStatus = Literal[413]

PAYLOAD_TOO_LARGE_STATUS_VALUES: set[PayloadTooLargeStatus] = {
    413,
}


def check_payload_too_large_status(value: int) -> PayloadTooLargeStatus:
    if value in PAYLOAD_TOO_LARGE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PAYLOAD_TOO_LARGE_STATUS_VALUES!r}")
