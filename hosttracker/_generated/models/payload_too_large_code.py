from typing import Literal

PayloadTooLargeCode = Literal["payload_too_large"]

PAYLOAD_TOO_LARGE_CODE_VALUES: set[PayloadTooLargeCode] = {
    "payload_too_large",
}


def check_payload_too_large_code(value: str) -> PayloadTooLargeCode:
    if value in PAYLOAD_TOO_LARGE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PAYLOAD_TOO_LARGE_CODE_VALUES!r}")
