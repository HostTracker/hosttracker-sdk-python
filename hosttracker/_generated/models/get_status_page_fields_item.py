from typing import Literal

GetStatusPageFieldsItem = Literal[
    "componentCount",
    "components",
    "created",
    "customDomain",
    "hasPassword",
    "id",
    "settings",
    "slug",
    "title",
    "unresolvedIncidents",
]

GET_STATUS_PAGE_FIELDS_ITEM_VALUES: set[GetStatusPageFieldsItem] = {
    "componentCount",
    "components",
    "created",
    "customDomain",
    "hasPassword",
    "id",
    "settings",
    "slug",
    "title",
    "unresolvedIncidents",
}


def check_get_status_page_fields_item(value: str) -> GetStatusPageFieldsItem:
    if value in GET_STATUS_PAGE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_STATUS_PAGE_FIELDS_ITEM_VALUES!r}")
