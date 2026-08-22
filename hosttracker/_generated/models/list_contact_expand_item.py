from typing import Literal

ListContactExpandItem = Literal["count", "group", "subscription", "summary", "template"]

LIST_CONTACT_EXPAND_ITEM_VALUES: set[ListContactExpandItem] = {
    "count",
    "group",
    "subscription",
    "summary",
    "template",
}


def check_list_contact_expand_item(value: str) -> ListContactExpandItem:
    if value in LIST_CONTACT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_EXPAND_ITEM_VALUES!r}")
