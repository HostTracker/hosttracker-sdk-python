from typing import Literal

PackageLimitCode = Literal["package_limit"]

PACKAGE_LIMIT_CODE_VALUES: set[PackageLimitCode] = {
    "package_limit",
}


def check_package_limit_code(value: str) -> PackageLimitCode:
    if value in PACKAGE_LIMIT_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PACKAGE_LIMIT_CODE_VALUES!r}")
