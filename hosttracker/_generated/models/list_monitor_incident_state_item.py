from typing import Literal

ListMonitorIncidentStateItem = Literal["open", "resolved"]

LIST_MONITOR_INCIDENT_STATE_ITEM_VALUES: set[ListMonitorIncidentStateItem] = {
    "open",
    "resolved",
}


def check_list_monitor_incident_state_item(value: str) -> ListMonitorIncidentStateItem:
    if value in LIST_MONITOR_INCIDENT_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_INCIDENT_STATE_ITEM_VALUES!r}")
