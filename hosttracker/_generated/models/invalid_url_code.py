from typing import Literal

InvalidUrlCode = Literal["invalid_url"]

INVALID_URL_CODE_VALUES: set[InvalidUrlCode] = {
    "invalid_url",
}


def check_invalid_url_code(value: str) -> InvalidUrlCode:
    if value in INVALID_URL_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_URL_CODE_VALUES!r}")
