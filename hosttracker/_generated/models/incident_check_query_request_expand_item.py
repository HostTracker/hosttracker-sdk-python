from typing import Literal

IncidentCheckQueryRequestExpandItem = Literal[
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

INCIDENT_CHECK_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[IncidentCheckQueryRequestExpandItem] = {
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_incident_check_query_request_expand_item(value: str) -> IncidentCheckQueryRequestExpandItem:
    if value in INCIDENT_CHECK_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_CHECK_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
