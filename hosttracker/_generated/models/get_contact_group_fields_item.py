from typing import Literal

GetContactGroupFieldsItem = Literal["created", "id", "items", "name"]

GET_CONTACT_GROUP_FIELDS_ITEM_VALUES: set[GetContactGroupFieldsItem] = {
    "created",
    "id",
    "items",
    "name",
}


def check_get_contact_group_fields_item(value: str) -> GetContactGroupFieldsItem:
    if value in GET_CONTACT_GROUP_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONTACT_GROUP_FIELDS_ITEM_VALUES!r}")
