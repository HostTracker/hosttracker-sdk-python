from typing import Literal

InvalidTokenStatus = Literal[401]

INVALID_TOKEN_STATUS_VALUES: set[InvalidTokenStatus] = {
    401,
}


def check_invalid_token_status(value: int) -> InvalidTokenStatus:
    if value in INVALID_TOKEN_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_TOKEN_STATUS_VALUES!r}")
