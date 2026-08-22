from typing import Literal

DuplicateContactCode = Literal["duplicate_contact"]

DUPLICATE_CONTACT_CODE_VALUES: set[DuplicateContactCode] = {
    "duplicate_contact",
}


def check_duplicate_contact_code(value: str) -> DuplicateContactCode:
    if value in DUPLICATE_CONTACT_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_CONTACT_CODE_VALUES!r}")
