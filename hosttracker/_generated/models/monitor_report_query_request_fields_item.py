from typing import Literal

MonitorReportQueryRequestFieldsItem = Literal["contact", "created", "frequencies"]

MONITOR_REPORT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MonitorReportQueryRequestFieldsItem] = {
    "contact",
    "created",
    "frequencies",
}


def check_monitor_report_query_request_fields_item(value: str) -> MonitorReportQueryRequestFieldsItem:
    if value in MONITOR_REPORT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_REPORT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
