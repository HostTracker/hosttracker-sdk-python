from typing import Literal

InvalidUrlType = Literal["https://api2.host-tracker.com/problems/invalid-url"]

INVALID_URL_TYPE_VALUES: set[InvalidUrlType] = {
    "https://api2.host-tracker.com/problems/invalid-url",
}


def check_invalid_url_type(value: str) -> InvalidUrlType:
    if value in INVALID_URL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_URL_TYPE_VALUES!r}")
