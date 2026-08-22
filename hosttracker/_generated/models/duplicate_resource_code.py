from typing import Literal

DuplicateResourceCode = Literal["duplicate_resource"]

DUPLICATE_RESOURCE_CODE_VALUES: set[DuplicateResourceCode] = {
    "duplicate_resource",
}


def check_duplicate_resource_code(value: str) -> DuplicateResourceCode:
    if value in DUPLICATE_RESOURCE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_RESOURCE_CODE_VALUES!r}")
