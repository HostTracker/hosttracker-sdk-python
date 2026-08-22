from typing import Literal

UrlBlacklistedCode = Literal["url_blacklisted"]

URL_BLACKLISTED_CODE_VALUES: set[UrlBlacklistedCode] = {
    "url_blacklisted",
}


def check_url_blacklisted_code(value: str) -> UrlBlacklistedCode:
    if value in URL_BLACKLISTED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {URL_BLACKLISTED_CODE_VALUES!r}")
