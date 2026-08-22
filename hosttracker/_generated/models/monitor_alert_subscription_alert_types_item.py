from typing import Literal

MonitorAlertSubscriptionAlertTypesItem = Literal["down", "repeatedlyDown", "up"]

MONITOR_ALERT_SUBSCRIPTION_ALERT_TYPES_ITEM_VALUES: set[MonitorAlertSubscriptionAlertTypesItem] = {
    "down",
    "repeatedlyDown",
    "up",
}


def check_monitor_alert_subscription_alert_types_item(value: str) -> MonitorAlertSubscriptionAlertTypesItem:
    if value in MONITOR_ALERT_SUBSCRIPTION_ALERT_TYPES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_ALERT_SUBSCRIPTION_ALERT_TYPES_ITEM_VALUES!r}"
    )
