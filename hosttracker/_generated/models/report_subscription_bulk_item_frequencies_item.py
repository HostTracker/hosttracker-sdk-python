from typing import Literal

ReportSubscriptionBulkItemFrequenciesItem = Literal["daily", "monthly", "quarterly", "weekly", "yearly"]

REPORT_SUBSCRIPTION_BULK_ITEM_FREQUENCIES_ITEM_VALUES: set[ReportSubscriptionBulkItemFrequenciesItem] = {
    "daily",
    "monthly",
    "quarterly",
    "weekly",
    "yearly",
}


def check_report_subscription_bulk_item_frequencies_item(value: str) -> ReportSubscriptionBulkItemFrequenciesItem:
    if value in REPORT_SUBSCRIPTION_BULK_ITEM_FREQUENCIES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SUBSCRIPTION_BULK_ITEM_FREQUENCIES_ITEM_VALUES!r}"
    )
