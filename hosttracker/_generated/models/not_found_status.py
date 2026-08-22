from typing import Literal

NotFoundStatus = Literal[404]

NOT_FOUND_STATUS_VALUES: set[NotFoundStatus] = {
    404,
}


def check_not_found_status(value: int) -> NotFoundStatus:
    if value in NOT_FOUND_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOT_FOUND_STATUS_VALUES!r}")
