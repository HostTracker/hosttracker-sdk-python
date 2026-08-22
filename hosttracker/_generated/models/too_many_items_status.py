from typing import Literal

TooManyItemsStatus = Literal[422]

TOO_MANY_ITEMS_STATUS_VALUES: set[TooManyItemsStatus] = {
    422,
}


def check_too_many_items_status(value: int) -> TooManyItemsStatus:
    if value in TOO_MANY_ITEMS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOO_MANY_ITEMS_STATUS_VALUES!r}")
