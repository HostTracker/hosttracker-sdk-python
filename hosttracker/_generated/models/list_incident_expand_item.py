from typing import Literal

ListIncidentExpandItem = Literal[
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

LIST_INCIDENT_EXPAND_ITEM_VALUES: set[ListIncidentExpandItem] = {
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_list_incident_expand_item(value: str) -> ListIncidentExpandItem:
    if value in LIST_INCIDENT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_EXPAND_ITEM_VALUES!r}")
