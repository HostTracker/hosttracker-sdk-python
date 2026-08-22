from typing import Literal

ListAlertByMonitorFieldsItem = Literal["monitor", "subscriptions"]

LIST_ALERT_BY_MONITOR_FIELDS_ITEM_VALUES: set[ListAlertByMonitorFieldsItem] = {
    "monitor",
    "subscriptions",
}


def check_list_alert_by_monitor_fields_item(value: str) -> ListAlertByMonitorFieldsItem:
    if value in LIST_ALERT_BY_MONITOR_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_BY_MONITOR_FIELDS_ITEM_VALUES!r}")
