from typing import Literal

ListMonitorReportFieldsItem = Literal["contact", "created", "frequencies"]

LIST_MONITOR_REPORT_FIELDS_ITEM_VALUES: set[ListMonitorReportFieldsItem] = {
    "contact",
    "created",
    "frequencies",
}


def check_list_monitor_report_fields_item(value: str) -> ListMonitorReportFieldsItem:
    if value in LIST_MONITOR_REPORT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_REPORT_FIELDS_ITEM_VALUES!r}")
