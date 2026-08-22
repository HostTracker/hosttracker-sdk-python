from typing import Literal

ListContactNotificationFieldsItem = Literal[
    "attempts", "channel", "checkNumber", "contact", "gateway", "id", "kind", "monitor", "preview", "sentAt", "subject"
]

LIST_CONTACT_NOTIFICATION_FIELDS_ITEM_VALUES: set[ListContactNotificationFieldsItem] = {
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


def check_list_contact_notification_fields_item(value: str) -> ListContactNotificationFieldsItem:
    if value in LIST_CONTACT_NOTIFICATION_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_NOTIFICATION_FIELDS_ITEM_VALUES!r}")
