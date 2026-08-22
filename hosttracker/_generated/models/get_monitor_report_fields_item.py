from typing import Literal

GetMonitorReportFieldsItem = Literal["contact", "created", "frequencies"]

GET_MONITOR_REPORT_FIELDS_ITEM_VALUES: set[GetMonitorReportFieldsItem] = {
    "contact",
    "created",
    "frequencies",
}


def check_get_monitor_report_fields_item(value: str) -> GetMonitorReportFieldsItem:
    if value in GET_MONITOR_REPORT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MONITOR_REPORT_FIELDS_ITEM_VALUES!r}")
