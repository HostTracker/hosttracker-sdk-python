from typing import Literal

ReportSubscriptionQueryRequestFieldsItem = Literal["contact", "created", "frequencies", "id", "monitor"]

REPORT_SUBSCRIPTION_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ReportSubscriptionQueryRequestFieldsItem] = {
    "contact",
    "created",
    "frequencies",
    "id",
    "monitor",
}


def check_report_subscription_query_request_fields_item(value: str) -> ReportSubscriptionQueryRequestFieldsItem:
    if value in REPORT_SUBSCRIPTION_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SUBSCRIPTION_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
