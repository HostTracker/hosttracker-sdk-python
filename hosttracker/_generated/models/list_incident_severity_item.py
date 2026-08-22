from typing import Literal

ListIncidentSeverityItem = Literal["critical", "major", "minor"]

LIST_INCIDENT_SEVERITY_ITEM_VALUES: set[ListIncidentSeverityItem] = {
    "critical",
    "major",
    "minor",
}


def check_list_incident_severity_item(value: str) -> ListIncidentSeverityItem:
    if value in LIST_INCIDENT_SEVERITY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_SEVERITY_ITEM_VALUES!r}")
