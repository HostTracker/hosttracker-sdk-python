from typing import Literal

PayloadTooLargeType = Literal["https://api2.host-tracker.com/problems/payload-too-large"]

PAYLOAD_TOO_LARGE_TYPE_VALUES: set[PayloadTooLargeType] = {
    "https://api2.host-tracker.com/problems/payload-too-large",
}


def check_payload_too_large_type(value: str) -> PayloadTooLargeType:
    if value in PAYLOAD_TOO_LARGE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PAYLOAD_TOO_LARGE_TYPE_VALUES!r}")
