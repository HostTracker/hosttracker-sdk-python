from typing import Literal

NotFoundType = Literal["https://api2.host-tracker.com/problems/not-found"]

NOT_FOUND_TYPE_VALUES: set[NotFoundType] = {
    "https://api2.host-tracker.com/problems/not-found",
}


def check_not_found_type(value: str) -> NotFoundType:
    if value in NOT_FOUND_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOT_FOUND_TYPE_VALUES!r}")
