from typing import Literal

ContactTypeNotCreatableType = Literal["https://api2.host-tracker.com/problems/contact-type-not-creatable"]

CONTACT_TYPE_NOT_CREATABLE_TYPE_VALUES: set[ContactTypeNotCreatableType] = {
    "https://api2.host-tracker.com/problems/contact-type-not-creatable",
}


def check_contact_type_not_creatable_type(value: str) -> ContactTypeNotCreatableType:
    if value in CONTACT_TYPE_NOT_CREATABLE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_TYPE_NOT_CREATABLE_TYPE_VALUES!r}")
