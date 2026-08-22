from typing import Literal

ListReportByMonitorFieldsItem = Literal["monitor", "subscriptions"]

LIST_REPORT_BY_MONITOR_FIELDS_ITEM_VALUES: set[ListReportByMonitorFieldsItem] = {
    "monitor",
    "subscriptions",
}


def check_list_report_by_monitor_fields_item(value: str) -> ListReportByMonitorFieldsItem:
    if value in LIST_REPORT_BY_MONITOR_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_BY_MONITOR_FIELDS_ITEM_VALUES!r}")
