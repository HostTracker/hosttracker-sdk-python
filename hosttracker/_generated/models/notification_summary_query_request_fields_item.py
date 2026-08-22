from typing import Literal

NotificationSummaryQueryRequestFieldsItem = Literal["contact", "count", "day", "outcome"]

NOTIFICATION_SUMMARY_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[NotificationSummaryQueryRequestFieldsItem] = {
    "contact",
    "count",
    "day",
    "outcome",
}


def check_notification_summary_query_request_fields_item(value: str) -> NotificationSummaryQueryRequestFieldsItem:
    if value in NOTIFICATION_SUMMARY_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NOTIFICATION_SUMMARY_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
