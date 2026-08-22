from typing import Literal

NotificationQueryRequestExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

NOTIFICATION_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[NotificationQueryRequestExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_notification_query_request_expand_item(value: str) -> NotificationQueryRequestExpandItem:
    if value in NOTIFICATION_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
