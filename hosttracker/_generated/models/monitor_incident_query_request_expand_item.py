from typing import Literal

MonitorIncidentQueryRequestExpandItem = Literal[
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

MONITOR_INCIDENT_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[MonitorIncidentQueryRequestExpandItem] = {
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_monitor_incident_query_request_expand_item(value: str) -> MonitorIncidentQueryRequestExpandItem:
    if value in MONITOR_INCIDENT_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_INCIDENT_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}"
    )
