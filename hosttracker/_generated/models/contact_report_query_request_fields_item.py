from typing import Literal

ContactReportQueryRequestFieldsItem = Literal["created", "frequencies", "monitor"]

CONTACT_REPORT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ContactReportQueryRequestFieldsItem] = {
    "created",
    "frequencies",
    "monitor",
}


def check_contact_report_query_request_fields_item(value: str) -> ContactReportQueryRequestFieldsItem:
    if value in CONTACT_REPORT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_REPORT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
