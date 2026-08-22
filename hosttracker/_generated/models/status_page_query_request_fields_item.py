from typing import Literal

StatusPageQueryRequestFieldsItem = Literal[
    "componentCount", "created", "hasPassword", "id", "slug", "title", "unresolvedIncidents"
]

STATUS_PAGE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[StatusPageQueryRequestFieldsItem] = {
    "componentCount",
    "created",
    "hasPassword",
    "id",
    "slug",
    "title",
    "unresolvedIncidents",
}


def check_status_page_query_request_fields_item(value: str) -> StatusPageQueryRequestFieldsItem:
    if value in STATUS_PAGE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
