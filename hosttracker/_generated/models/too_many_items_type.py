from typing import Literal

TooManyItemsType = Literal["https://api2.host-tracker.com/problems/too-many-items"]

TOO_MANY_ITEMS_TYPE_VALUES: set[TooManyItemsType] = {
    "https://api2.host-tracker.com/problems/too-many-items",
}


def check_too_many_items_type(value: str) -> TooManyItemsType:
    if value in TOO_MANY_ITEMS_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOO_MANY_ITEMS_TYPE_VALUES!r}")
