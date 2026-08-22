from typing import Literal

InsufficientRightsStatus = Literal[403]

INSUFFICIENT_RIGHTS_STATUS_VALUES: set[InsufficientRightsStatus] = {
    403,
}


def check_insufficient_rights_status(value: int) -> InsufficientRightsStatus:
    if value in INSUFFICIENT_RIGHTS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_RIGHTS_STATUS_VALUES!r}")
