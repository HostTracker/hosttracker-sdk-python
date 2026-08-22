from typing import Literal

FilterRequiredCode = Literal["filter_required"]

FILTER_REQUIRED_CODE_VALUES: set[FilterRequiredCode] = {
    "filter_required",
}


def check_filter_required_code(value: str) -> FilterRequiredCode:
    if value in FILTER_REQUIRED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILTER_REQUIRED_CODE_VALUES!r}")
