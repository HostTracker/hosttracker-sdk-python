from typing import Literal

GetNotificationSummaryFieldsItem = Literal["contact", "count", "day", "outcome"]

GET_NOTIFICATION_SUMMARY_FIELDS_ITEM_VALUES: set[GetNotificationSummaryFieldsItem] = {
    "contact",
    "count",
    "day",
    "outcome",
}


def check_get_notification_summary_fields_item(value: str) -> GetNotificationSummaryFieldsItem:
    if value in GET_NOTIFICATION_SUMMARY_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_NOTIFICATION_SUMMARY_FIELDS_ITEM_VALUES!r}")
