from typing import Literal

MonitorAlertQueryRequestFieldsItem = Literal["alertTypes", "contact", "created"]

MONITOR_ALERT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MonitorAlertQueryRequestFieldsItem] = {
    "alertTypes",
    "contact",
    "created",
}


def check_monitor_alert_query_request_fields_item(value: str) -> MonitorAlertQueryRequestFieldsItem:
    if value in MONITOR_ALERT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_ALERT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
