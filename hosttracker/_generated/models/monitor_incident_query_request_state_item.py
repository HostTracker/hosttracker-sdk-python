from typing import Literal

MonitorIncidentQueryRequestStateItem = Literal["open", "resolved"]

MONITOR_INCIDENT_QUERY_REQUEST_STATE_ITEM_VALUES: set[MonitorIncidentQueryRequestStateItem] = {
    "open",
    "resolved",
}


def check_monitor_incident_query_request_state_item(value: str) -> MonitorIncidentQueryRequestStateItem:
    if value in MONITOR_INCIDENT_QUERY_REQUEST_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_INCIDENT_QUERY_REQUEST_STATE_ITEM_VALUES!r}")
