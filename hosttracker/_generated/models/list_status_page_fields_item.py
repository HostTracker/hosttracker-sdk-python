from typing import Literal

ListStatusPageFieldsItem = Literal[
    "componentCount", "created", "hasPassword", "id", "slug", "title", "unresolvedIncidents"
]

LIST_STATUS_PAGE_FIELDS_ITEM_VALUES: set[ListStatusPageFieldsItem] = {
    "componentCount",
    "created",
    "hasPassword",
    "id",
    "slug",
    "title",
    "unresolvedIncidents",
}


def check_list_status_page_fields_item(value: str) -> ListStatusPageFieldsItem:
    if value in LIST_STATUS_PAGE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_STATUS_PAGE_FIELDS_ITEM_VALUES!r}")
