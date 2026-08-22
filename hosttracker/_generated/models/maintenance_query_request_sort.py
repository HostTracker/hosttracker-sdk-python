from typing import Literal

MaintenanceQueryRequestSort = Literal["created", "created:asc", "created:desc", "from", "from:asc", "from:desc"]

MAINTENANCE_QUERY_REQUEST_SORT_VALUES: set[MaintenanceQueryRequestSort] = {
    "created",
    "created:asc",
    "created:desc",
    "from",
    "from:asc",
    "from:desc",
}


def check_maintenance_query_request_sort(value: str) -> MaintenanceQueryRequestSort:
    if value in MAINTENANCE_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_QUERY_REQUEST_SORT_VALUES!r}")
