from typing import Literal

DuplicateResourceStatus = Literal[409]

DUPLICATE_RESOURCE_STATUS_VALUES: set[DuplicateResourceStatus] = {
    409,
}


def check_duplicate_resource_status(value: int) -> DuplicateResourceStatus:
    if value in DUPLICATE_RESOURCE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_RESOURCE_STATUS_VALUES!r}")
