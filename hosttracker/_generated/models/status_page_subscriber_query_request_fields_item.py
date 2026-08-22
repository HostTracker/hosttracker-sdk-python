from typing import Literal

StatusPageSubscriberQueryRequestFieldsItem = Literal[
    "componentId", "confirmedAt", "created", "email", "id", "kind", "url"
]

STATUS_PAGE_SUBSCRIBER_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[StatusPageSubscriberQueryRequestFieldsItem] = {
    "componentId",
    "confirmedAt",
    "created",
    "email",
    "id",
    "kind",
    "url",
}


def check_status_page_subscriber_query_request_fields_item(value: str) -> StatusPageSubscriberQueryRequestFieldsItem:
    if value in STATUS_PAGE_SUBSCRIBER_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SUBSCRIBER_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
