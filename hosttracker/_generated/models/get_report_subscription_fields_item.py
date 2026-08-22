from typing import Literal

GetReportSubscriptionFieldsItem = Literal["contact", "created", "frequencies", "id", "monitor"]

GET_REPORT_SUBSCRIPTION_FIELDS_ITEM_VALUES: set[GetReportSubscriptionFieldsItem] = {
    "contact",
    "created",
    "frequencies",
    "id",
    "monitor",
}


def check_get_report_subscription_fields_item(value: str) -> GetReportSubscriptionFieldsItem:
    if value in GET_REPORT_SUBSCRIPTION_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_REPORT_SUBSCRIPTION_FIELDS_ITEM_VALUES!r}")
