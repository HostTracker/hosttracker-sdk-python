from typing import Literal

ListInstantCheckFieldsItem = Literal["created", "dbId", "doneAt", "id", "state", "type", "up", "url"]

LIST_INSTANT_CHECK_FIELDS_ITEM_VALUES: set[ListInstantCheckFieldsItem] = {
    "created",
    "dbId",
    "doneAt",
    "id",
    "state",
    "type",
    "up",
    "url",
}


def check_list_instant_check_fields_item(value: str) -> ListInstantCheckFieldsItem:
    if value in LIST_INSTANT_CHECK_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INSTANT_CHECK_FIELDS_ITEM_VALUES!r}")
