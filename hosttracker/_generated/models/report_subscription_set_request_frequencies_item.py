from typing import Literal

ReportSubscriptionSetRequestFrequenciesItem = Literal["daily", "monthly", "quarterly", "weekly", "yearly"]

REPORT_SUBSCRIPTION_SET_REQUEST_FREQUENCIES_ITEM_VALUES: set[ReportSubscriptionSetRequestFrequenciesItem] = {
    "daily",
    "monthly",
    "quarterly",
    "weekly",
    "yearly",
}


def check_report_subscription_set_request_frequencies_item(value: str) -> ReportSubscriptionSetRequestFrequenciesItem:
    if value in REPORT_SUBSCRIPTION_SET_REQUEST_FREQUENCIES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SUBSCRIPTION_SET_REQUEST_FREQUENCIES_ITEM_VALUES!r}"
    )
