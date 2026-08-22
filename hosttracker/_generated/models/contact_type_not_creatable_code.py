from typing import Literal

ContactTypeNotCreatableCode = Literal["contact_type_not_creatable"]

CONTACT_TYPE_NOT_CREATABLE_CODE_VALUES: set[ContactTypeNotCreatableCode] = {
    "contact_type_not_creatable",
}


def check_contact_type_not_creatable_code(value: str) -> ContactTypeNotCreatableCode:
    if value in CONTACT_TYPE_NOT_CREATABLE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_TYPE_NOT_CREATABLE_CODE_VALUES!r}")
