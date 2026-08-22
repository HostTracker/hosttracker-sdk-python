from typing import Literal

ListNotificationExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

LIST_NOTIFICATION_EXPAND_ITEM_VALUES: set[ListNotificationExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_list_notification_expand_item(value: str) -> ListNotificationExpandItem:
    if value in LIST_NOTIFICATION_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_NOTIFICATION_EXPAND_ITEM_VALUES!r}")
