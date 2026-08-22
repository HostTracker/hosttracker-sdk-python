from typing import Literal

GetReportFieldsItem = Literal[
    "contentUrl", "expiresAt", "format", "id", "monitorIds", "range", "sections", "sizeBytes", "state", "type"
]

GET_REPORT_FIELDS_ITEM_VALUES: set[GetReportFieldsItem] = {
    "contentUrl",
    "expiresAt",
    "format",
    "id",
    "monitorIds",
    "range",
    "sections",
    "sizeBytes",
    "state",
    "type",
}


def check_get_report_fields_item(value: str) -> GetReportFieldsItem:
    if value in GET_REPORT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_REPORT_FIELDS_ITEM_VALUES!r}")
