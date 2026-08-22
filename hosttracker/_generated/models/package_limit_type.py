from typing import Literal

PackageLimitType = Literal["https://api2.host-tracker.com/problems/package-limit"]

PACKAGE_LIMIT_TYPE_VALUES: set[PackageLimitType] = {
    "https://api2.host-tracker.com/problems/package-limit",
}


def check_package_limit_type(value: str) -> PackageLimitType:
    if value in PACKAGE_LIMIT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PACKAGE_LIMIT_TYPE_VALUES!r}")
