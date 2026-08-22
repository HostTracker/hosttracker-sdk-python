from typing import Literal

InvalidUrlStatus = Literal[422]

INVALID_URL_STATUS_VALUES: set[InvalidUrlStatus] = {
    422,
}


def check_invalid_url_status(value: int) -> InvalidUrlStatus:
    if value in INVALID_URL_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_URL_STATUS_VALUES!r}")
