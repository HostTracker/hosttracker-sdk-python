from typing import Literal

ListContactNotificationExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

LIST_CONTACT_NOTIFICATION_EXPAND_ITEM_VALUES: set[ListContactNotificationExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_list_contact_notification_expand_item(value: str) -> ListContactNotificationExpandItem:
    if value in LIST_CONTACT_NOTIFICATION_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_NOTIFICATION_EXPAND_ITEM_VALUES!r}")
