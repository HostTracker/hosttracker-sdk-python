from typing import Literal

FilterRequiredType = Literal["https://api2.host-tracker.com/problems/filter-required"]

FILTER_REQUIRED_TYPE_VALUES: set[FilterRequiredType] = {
    "https://api2.host-tracker.com/problems/filter-required",
}


def check_filter_required_type(value: str) -> FilterRequiredType:
    if value in FILTER_REQUIRED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILTER_REQUIRED_TYPE_VALUES!r}")
