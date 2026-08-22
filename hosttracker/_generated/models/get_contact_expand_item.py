from typing import Literal

GetContactExpandItem = Literal["count", "group", "subscription", "summary", "template"]

GET_CONTACT_EXPAND_ITEM_VALUES: set[GetContactExpandItem] = {
    "count",
    "group",
    "subscription",
    "summary",
    "template",
}


def check_get_contact_expand_item(value: str) -> GetContactExpandItem:
    if value in GET_CONTACT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONTACT_EXPAND_ITEM_VALUES!r}")
