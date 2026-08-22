from typing import Literal

UrlBlacklistedStatus = Literal[403]

URL_BLACKLISTED_STATUS_VALUES: set[UrlBlacklistedStatus] = {
    403,
}


def check_url_blacklisted_status(value: int) -> UrlBlacklistedStatus:
    if value in URL_BLACKLISTED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {URL_BLACKLISTED_STATUS_VALUES!r}")
