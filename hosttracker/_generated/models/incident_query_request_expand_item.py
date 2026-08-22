from typing import Literal

IncidentQueryRequestExpandItem = Literal[
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

INCIDENT_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[IncidentQueryRequestExpandItem] = {
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_incident_query_request_expand_item(value: str) -> IncidentQueryRequestExpandItem:
    if value in INCIDENT_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
