from typing import Literal

ReportTypeQueryRequestFieldsItem = Literal["formats", "frequencies", "label", "sections", "type"]

REPORT_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ReportTypeQueryRequestFieldsItem] = {
    "formats",
    "frequencies",
    "label",
    "sections",
    "type",
}


def check_report_type_query_request_fields_item(value: str) -> ReportTypeQueryRequestFieldsItem:
    if value in REPORT_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
