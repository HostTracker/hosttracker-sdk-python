from typing import Literal

GetNotificationFieldsItem = Literal[
    "attempts",
    "body",
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
]

GET_NOTIFICATION_FIELDS_ITEM_VALUES: set[GetNotificationFieldsItem] = {
    "attempts",
    "body",
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


def check_get_notification_fields_item(value: str) -> GetNotificationFieldsItem:
    if value in GET_NOTIFICATION_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_NOTIFICATION_FIELDS_ITEM_VALUES!r}")
