from typing import Literal

ListReportSubscriptionFieldsItem = Literal["contact", "created", "frequencies", "id", "monitor"]

LIST_REPORT_SUBSCRIPTION_FIELDS_ITEM_VALUES: set[ListReportSubscriptionFieldsItem] = {
    "contact",
    "created",
    "frequencies",
    "id",
    "monitor",
}


def check_list_report_subscription_fields_item(value: str) -> ListReportSubscriptionFieldsItem:
    if value in LIST_REPORT_SUBSCRIPTION_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_SUBSCRIPTION_FIELDS_ITEM_VALUES!r}")
