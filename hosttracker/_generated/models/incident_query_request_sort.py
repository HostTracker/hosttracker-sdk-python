from typing import Literal

IncidentQueryRequestSort = Literal["monitor", "monitor:asc", "monitor:desc", "time", "time:desc"]

INCIDENT_QUERY_REQUEST_SORT_VALUES: set[IncidentQueryRequestSort] = {
    "monitor",
    "monitor:asc",
    "monitor:desc",
    "time",
    "time:desc",
}


def check_incident_query_request_sort(value: str) -> IncidentQueryRequestSort:
    if value in INCIDENT_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_QUERY_REQUEST_SORT_VALUES!r}")
