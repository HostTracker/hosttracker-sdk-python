from typing import Literal

ContactGroupQueryRequestFieldsItem = Literal["created", "id", "items", "name"]

CONTACT_GROUP_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ContactGroupQueryRequestFieldsItem] = {
    "created",
    "id",
    "items",
    "name",
}


def check_contact_group_query_request_fields_item(value: str) -> ContactGroupQueryRequestFieldsItem:
    if value in CONTACT_GROUP_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
