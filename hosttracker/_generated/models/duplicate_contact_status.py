from typing import Literal

DuplicateContactStatus = Literal[409]

DUPLICATE_CONTACT_STATUS_VALUES: set[DuplicateContactStatus] = {
    409,
}


def check_duplicate_contact_status(value: int) -> DuplicateContactStatus:
    if value in DUPLICATE_CONTACT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_CONTACT_STATUS_VALUES!r}")
