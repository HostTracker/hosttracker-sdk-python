from typing import Literal

ListContactGroupFieldsItem = Literal["created", "id", "items", "name"]

LIST_CONTACT_GROUP_FIELDS_ITEM_VALUES: set[ListContactGroupFieldsItem] = {
    "created",
    "id",
    "items",
    "name",
}


def check_list_contact_group_fields_item(value: str) -> ListContactGroupFieldsItem:
    if value in LIST_CONTACT_GROUP_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_GROUP_FIELDS_ITEM_VALUES!r}")
