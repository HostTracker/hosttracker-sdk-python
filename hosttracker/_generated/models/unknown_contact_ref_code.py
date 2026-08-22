from typing import Literal

UnknownContactRefCode = Literal["unknown_contact_ref"]

UNKNOWN_CONTACT_REF_CODE_VALUES: set[UnknownContactRefCode] = {
    "unknown_contact_ref",
}


def check_unknown_contact_ref_code(value: str) -> UnknownContactRefCode:
    if value in UNKNOWN_CONTACT_REF_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_CONTACT_REF_CODE_VALUES!r}")
