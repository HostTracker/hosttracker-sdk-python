from typing import Literal

InvalidTokenType = Literal["https://api2.host-tracker.com/problems/invalid-token"]

INVALID_TOKEN_TYPE_VALUES: set[InvalidTokenType] = {
    "https://api2.host-tracker.com/problems/invalid-token",
}


def check_invalid_token_type(value: str) -> InvalidTokenType:
    if value in INVALID_TOKEN_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_TOKEN_TYPE_VALUES!r}")
