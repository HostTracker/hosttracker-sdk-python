from typing import Literal

ContactTypeNotCreatableStatus = Literal[422]

CONTACT_TYPE_NOT_CREATABLE_STATUS_VALUES: set[ContactTypeNotCreatableStatus] = {
    422,
}


def check_contact_type_not_creatable_status(value: int) -> ContactTypeNotCreatableStatus:
    if value in CONTACT_TYPE_NOT_CREATABLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_TYPE_NOT_CREATABLE_STATUS_VALUES!r}")
