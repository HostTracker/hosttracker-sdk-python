from typing import Literal

MonitorReportSubscriptionType = Literal["daily", "monthly", "quarterly", "weekly", "yearly"]

MONITOR_REPORT_SUBSCRIPTION_TYPE_VALUES: set[MonitorReportSubscriptionType] = {
    "daily",
    "monthly",
    "quarterly",
    "weekly",
    "yearly",
}


def check_monitor_report_subscription_type(value: str) -> MonitorReportSubscriptionType:
    if value in MONITOR_REPORT_SUBSCRIPTION_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_REPORT_SUBSCRIPTION_TYPE_VALUES!r}")
