from typing import Literal

InsufficientRightsCode = Literal["insufficient_rights"]

INSUFFICIENT_RIGHTS_CODE_VALUES: set[InsufficientRightsCode] = {
    "insufficient_rights",
}


def check_insufficient_rights_code(value: str) -> InsufficientRightsCode:
    if value in INSUFFICIENT_RIGHTS_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_RIGHTS_CODE_VALUES!r}")
