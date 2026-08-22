from typing import Literal

ContactNotificationQueryRequestExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

CONTACT_NOTIFICATION_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[ContactNotificationQueryRequestExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_contact_notification_query_request_expand_item(value: str) -> ContactNotificationQueryRequestExpandItem:
    if value in CONTACT_NOTIFICATION_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_NOTIFICATION_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}"
    )
