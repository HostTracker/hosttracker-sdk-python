from typing import Literal

InstantCheckQueryRequestFieldsItem = Literal["created", "dbId", "doneAt", "id", "state", "type", "up", "url"]

INSTANT_CHECK_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[InstantCheckQueryRequestFieldsItem] = {
    "created",
    "dbId",
    "doneAt",
    "id",
    "state",
    "type",
    "up",
    "url",
}


def check_instant_check_query_request_fields_item(value: str) -> InstantCheckQueryRequestFieldsItem:
    if value in INSTANT_CHECK_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSTANT_CHECK_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
