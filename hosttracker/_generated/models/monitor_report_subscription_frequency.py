from typing import Literal

MonitorReportSubscriptionFrequency = Literal["daily", "monthly", "quarterly", "weekly", "yearly"]

MONITOR_REPORT_SUBSCRIPTION_FREQUENCY_VALUES: set[MonitorReportSubscriptionFrequency] = {
    "daily",
    "monthly",
    "quarterly",
    "weekly",
    "yearly",
}


def check_monitor_report_subscription_frequency(value: str) -> MonitorReportSubscriptionFrequency:
    if value in MONITOR_REPORT_SUBSCRIPTION_FREQUENCY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_REPORT_SUBSCRIPTION_FREQUENCY_VALUES!r}")
