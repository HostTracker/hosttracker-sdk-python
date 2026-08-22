from typing import Literal

ReportByMonitorQueryRequestFieldsItem = Literal["monitor", "subscriptions"]

REPORT_BY_MONITOR_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ReportByMonitorQueryRequestFieldsItem] = {
    "monitor",
    "subscriptions",
}


def check_report_by_monitor_query_request_fields_item(value: str) -> ReportByMonitorQueryRequestFieldsItem:
    if value in REPORT_BY_MONITOR_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_BY_MONITOR_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
