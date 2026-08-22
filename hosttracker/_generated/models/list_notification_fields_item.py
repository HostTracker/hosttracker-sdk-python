from typing import Literal

ListNotificationFieldsItem = Literal[
    "attempts", "channel", "checkNumber", "contact", "gateway", "id", "kind", "monitor", "preview", "sentAt", "subject"
]

LIST_NOTIFICATION_FIELDS_ITEM_VALUES: set[ListNotificationFieldsItem] = {
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


def check_list_notification_fields_item(value: str) -> ListNotificationFieldsItem:
    if value in LIST_NOTIFICATION_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_NOTIFICATION_FIELDS_ITEM_VALUES!r}")
