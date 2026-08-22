from typing import Literal

TooManyItemsCode = Literal["too_many_items"]

TOO_MANY_ITEMS_CODE_VALUES: set[TooManyItemsCode] = {
    "too_many_items",
}


def check_too_many_items_code(value: str) -> TooManyItemsCode:
    if value in TOO_MANY_ITEMS_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TOO_MANY_ITEMS_CODE_VALUES!r}")
