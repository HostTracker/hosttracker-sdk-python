from typing import Literal

DuplicateResourceType = Literal["https://api2.host-tracker.com/problems/duplicate-resource"]

DUPLICATE_RESOURCE_TYPE_VALUES: set[DuplicateResourceType] = {
    "https://api2.host-tracker.com/problems/duplicate-resource",
}


def check_duplicate_resource_type(value: str) -> DuplicateResourceType:
    if value in DUPLICATE_RESOURCE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_RESOURCE_TYPE_VALUES!r}")
