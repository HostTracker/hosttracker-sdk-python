from typing import Literal

ListIncidentCheckExpandItem = Literal[
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

LIST_INCIDENT_CHECK_EXPAND_ITEM_VALUES: set[ListIncidentCheckExpandItem] = {
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_list_incident_check_expand_item(value: str) -> ListIncidentCheckExpandItem:
    if value in LIST_INCIDENT_CHECK_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_CHECK_EXPAND_ITEM_VALUES!r}")
