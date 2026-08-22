from typing import Literal

ContactQueryRequestExpandItem = Literal["count", "group", "subscription", "summary", "template"]

CONTACT_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[ContactQueryRequestExpandItem] = {
    "count",
    "group",
    "subscription",
    "summary",
    "template",
}


def check_contact_query_request_expand_item(value: str) -> ContactQueryRequestExpandItem:
    if value in CONTACT_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
