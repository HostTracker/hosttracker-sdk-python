from typing import Literal

InsufficientRightsType = Literal["https://api2.host-tracker.com/problems/insufficient-rights"]

INSUFFICIENT_RIGHTS_TYPE_VALUES: set[InsufficientRightsType] = {
    "https://api2.host-tracker.com/problems/insufficient-rights",
}


def check_insufficient_rights_type(value: str) -> InsufficientRightsType:
    if value in INSUFFICIENT_RIGHTS_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_RIGHTS_TYPE_VALUES!r}")
