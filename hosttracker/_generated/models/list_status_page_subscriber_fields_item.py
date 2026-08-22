from typing import Literal

ListStatusPageSubscriberFieldsItem = Literal["componentId", "confirmedAt", "created", "email", "id", "kind", "url"]

LIST_STATUS_PAGE_SUBSCRIBER_FIELDS_ITEM_VALUES: set[ListStatusPageSubscriberFieldsItem] = {
    "componentId",
    "confirmedAt",
    "created",
    "email",
    "id",
    "kind",
    "url",
}


def check_list_status_page_subscriber_fields_item(value: str) -> ListStatusPageSubscriberFieldsItem:
    if value in LIST_STATUS_PAGE_SUBSCRIBER_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_STATUS_PAGE_SUBSCRIBER_FIELDS_ITEM_VALUES!r}")
