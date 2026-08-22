from typing import Literal

ContactReportSubscriptionFrequency = Literal["daily", "monthly", "quarterly", "weekly", "yearly"]

CONTACT_REPORT_SUBSCRIPTION_FREQUENCY_VALUES: set[ContactReportSubscriptionFrequency] = {
    "daily",
    "monthly",
    "quarterly",
    "weekly",
    "yearly",
}


def check_contact_report_subscription_frequency(value: str) -> ContactReportSubscriptionFrequency:
    if value in CONTACT_REPORT_SUBSCRIPTION_FREQUENCY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_REPORT_SUBSCRIPTION_FREQUENCY_VALUES!r}")
