from typing import Literal

GetMonitorAlertFieldsItem = Literal["alertTypes", "contact", "created"]

GET_MONITOR_ALERT_FIELDS_ITEM_VALUES: set[GetMonitorAlertFieldsItem] = {
    "alertTypes",
    "contact",
    "created",
}


def check_get_monitor_alert_fields_item(value: str) -> GetMonitorAlertFieldsItem:
    if value in GET_MONITOR_ALERT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MONITOR_ALERT_FIELDS_ITEM_VALUES!r}")
