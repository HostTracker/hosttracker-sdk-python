from typing import Literal

MissingScopeStatus = Literal[403]

MISSING_SCOPE_STATUS_VALUES: set[MissingScopeStatus] = {
    403,
}


def check_missing_scope_status(value: int) -> MissingScopeStatus:
    if value in MISSING_SCOPE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MISSING_SCOPE_STATUS_VALUES!r}")
