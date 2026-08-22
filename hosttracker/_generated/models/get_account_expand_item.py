from typing import Literal

GetAccountExpandItem = Literal["quota"]

GET_ACCOUNT_EXPAND_ITEM_VALUES: set[GetAccountExpandItem] = {
    "quota",
}


def check_get_account_expand_item(value: str) -> GetAccountExpandItem:
    if value in GET_ACCOUNT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ACCOUNT_EXPAND_ITEM_VALUES!r}")
