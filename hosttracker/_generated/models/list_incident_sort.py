from typing import Literal

ListIncidentSort = Literal["monitor", "monitor:asc", "monitor:desc", "time", "time:desc"]

LIST_INCIDENT_SORT_VALUES: set[ListIncidentSort] = {
    "monitor",
    "monitor:asc",
    "monitor:desc",
    "time",
    "time:desc",
}


def check_list_incident_sort(value: str) -> ListIncidentSort:
    if value in LIST_INCIDENT_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_SORT_VALUES!r}")
