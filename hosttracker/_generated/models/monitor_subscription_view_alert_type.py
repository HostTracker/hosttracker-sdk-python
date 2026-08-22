from typing import Literal

MonitorSubscriptionViewAlertType = Literal["down", "repeatedlyDown", "up"]

MONITOR_SUBSCRIPTION_VIEW_ALERT_TYPE_VALUES: set[MonitorSubscriptionViewAlertType] = {
    "down",
    "repeatedlyDown",
    "up",
}


def check_monitor_subscription_view_alert_type(value: str) -> MonitorSubscriptionViewAlertType:
    if value in MONITOR_SUBSCRIPTION_VIEW_ALERT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SUBSCRIPTION_VIEW_ALERT_TYPE_VALUES!r}")
