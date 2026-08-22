from typing import Literal

MissingScopeType = Literal["https://api2.host-tracker.com/problems/missing-scope"]

MISSING_SCOPE_TYPE_VALUES: set[MissingScopeType] = {
    "https://api2.host-tracker.com/problems/missing-scope",
}


def check_missing_scope_type(value: str) -> MissingScopeType:
    if value in MISSING_SCOPE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MISSING_SCOPE_TYPE_VALUES!r}")
