from typing import Literal

FilterRequiredStatus = Literal[422]

FILTER_REQUIRED_STATUS_VALUES: set[FilterRequiredStatus] = {
    422,
}


def check_filter_required_status(value: int) -> FilterRequiredStatus:
    if value in FILTER_REQUIRED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILTER_REQUIRED_STATUS_VALUES!r}")
