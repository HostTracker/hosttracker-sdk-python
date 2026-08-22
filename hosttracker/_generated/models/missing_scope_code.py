from typing import Literal

MissingScopeCode = Literal["missing_scope"]

MISSING_SCOPE_CODE_VALUES: set[MissingScopeCode] = {
    "missing_scope",
}


def check_missing_scope_code(value: str) -> MissingScopeCode:
    if value in MISSING_SCOPE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MISSING_SCOPE_CODE_VALUES!r}")
