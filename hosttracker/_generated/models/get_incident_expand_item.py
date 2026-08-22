from typing import Literal

GetIncidentExpandItem = Literal[
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

GET_INCIDENT_EXPAND_ITEM_VALUES: set[GetIncidentExpandItem] = {
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_get_incident_expand_item(value: str) -> GetIncidentExpandItem:
    if value in GET_INCIDENT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INCIDENT_EXPAND_ITEM_VALUES!r}")
