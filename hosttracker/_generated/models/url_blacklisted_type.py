from typing import Literal

UrlBlacklistedType = Literal["https://api2.host-tracker.com/problems/url-blacklisted"]

URL_BLACKLISTED_TYPE_VALUES: set[UrlBlacklistedType] = {
    "https://api2.host-tracker.com/problems/url-blacklisted",
}


def check_url_blacklisted_type(value: str) -> UrlBlacklistedType:
    if value in URL_BLACKLISTED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {URL_BLACKLISTED_TYPE_VALUES!r}")
