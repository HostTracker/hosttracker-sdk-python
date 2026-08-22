from typing import Literal

ReportByContactQueryRequestFieldsItem = Literal["contact", "subscriptions"]

REPORT_BY_CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ReportByContactQueryRequestFieldsItem] = {
    "contact",
    "subscriptions",
}


def check_report_by_contact_query_request_fields_item(value: str) -> ReportByContactQueryRequestFieldsItem:
    if value in REPORT_BY_CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_BY_CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
