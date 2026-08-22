from typing import Literal

InvalidTokenCode = Literal["invalid_token"]

INVALID_TOKEN_CODE_VALUES: set[InvalidTokenCode] = {
    "invalid_token",
}


def check_invalid_token_code(value: str) -> InvalidTokenCode:
    if value in INVALID_TOKEN_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_TOKEN_CODE_VALUES!r}")
