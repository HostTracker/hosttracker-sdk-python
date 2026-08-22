from typing import Literal

ContactNotificationQueryRequestFieldsItem = Literal[
    "attempts", "channel", "checkNumber", "contact", "gateway", "id", "kind", "monitor", "preview", "sentAt", "subject"
]

CONTACT_NOTIFICATION_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ContactNotificationQueryRequestFieldsItem] = {
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


def check_contact_notification_query_request_fields_item(value: str) -> ContactNotificationQueryRequestFieldsItem:
    if value in CONTACT_NOTIFICATION_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_NOTIFICATION_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
