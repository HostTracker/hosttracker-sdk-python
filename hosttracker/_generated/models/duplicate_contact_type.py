from typing import Literal

DuplicateContactType = Literal["https://api2.host-tracker.com/problems/duplicate-contact"]

DUPLICATE_CONTACT_TYPE_VALUES: set[DuplicateContactType] = {
    "https://api2.host-tracker.com/problems/duplicate-contact",
}


def check_duplicate_contact_type(value: str) -> DuplicateContactType:
    if value in DUPLICATE_CONTACT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_CONTACT_TYPE_VALUES!r}")
