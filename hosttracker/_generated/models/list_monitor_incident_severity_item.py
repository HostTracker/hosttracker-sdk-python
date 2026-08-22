from typing import Literal

ListMonitorIncidentSeverityItem = Literal["critical", "major", "minor"]

LIST_MONITOR_INCIDENT_SEVERITY_ITEM_VALUES: set[ListMonitorIncidentSeverityItem] = {
    "critical",
    "major",
    "minor",
}


def check_list_monitor_incident_severity_item(value: str) -> ListMonitorIncidentSeverityItem:
    if value in LIST_MONITOR_INCIDENT_SEVERITY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_INCIDENT_SEVERITY_ITEM_VALUES!r}")
