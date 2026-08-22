from typing import Literal

PackageLimitStatus = Literal[403]

PACKAGE_LIMIT_STATUS_VALUES: set[PackageLimitStatus] = {
    403,
}


def check_package_limit_status(value: int) -> PackageLimitStatus:
    if value in PACKAGE_LIMIT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PACKAGE_LIMIT_STATUS_VALUES!r}")
