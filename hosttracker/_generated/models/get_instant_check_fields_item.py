from typing import Literal

GetInstantCheckFieldsItem = Literal["created", "dbId", "doneAt", "events", "id", "retryAfter", "state", "type", "url"]

GET_INSTANT_CHECK_FIELDS_ITEM_VALUES: set[GetInstantCheckFieldsItem] = {
    "created",
    "dbId",
    "doneAt",
    "events",
    "id",
    "retryAfter",
    "state",
    "type",
    "url",
}


def check_get_instant_check_fields_item(value: str) -> GetInstantCheckFieldsItem:
    if value in GET_INSTANT_CHECK_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INSTANT_CHECK_FIELDS_ITEM_VALUES!r}")
