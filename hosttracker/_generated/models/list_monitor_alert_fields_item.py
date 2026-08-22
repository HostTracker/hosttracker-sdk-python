from typing import Literal

ListMonitorAlertFieldsItem = Literal["alertTypes", "contact", "created"]

LIST_MONITOR_ALERT_FIELDS_ITEM_VALUES: set[ListMonitorAlertFieldsItem] = {
    "alertTypes",
    "contact",
    "created",
}


def check_list_monitor_alert_fields_item(value: str) -> ListMonitorAlertFieldsItem:
    if value in LIST_MONITOR_ALERT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_ALERT_FIELDS_ITEM_VALUES!r}")
