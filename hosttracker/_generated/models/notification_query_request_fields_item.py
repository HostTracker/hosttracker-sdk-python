from typing import Literal

NotificationQueryRequestFieldsItem = Literal[
    "attempts", "channel", "checkNumber", "contact", "gateway", "id", "kind", "monitor", "preview", "sentAt", "subject"
]

NOTIFICATION_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[NotificationQueryRequestFieldsItem] = {
    "attempts",
    "channel",
    "checkNumber",
    "contact",
    "gateway",
    "id",
    "kind",
    "monitor",
    "preview",
    "sentAt",
    "subject",
}


def check_notification_query_request_fields_item(value: str) -> NotificationQueryRequestFieldsItem:
    if value in NOTIFICATION_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
