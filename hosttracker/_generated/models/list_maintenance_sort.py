from typing import Literal

ListMaintenanceSort = Literal["created", "created:asc", "created:desc", "from", "from:asc", "from:desc"]

LIST_MAINTENANCE_SORT_VALUES: set[ListMaintenanceSort] = {
    "created",
    "created:asc",
    "created:desc",
    "from",
    "from:asc",
    "from:desc",
}


def check_list_maintenance_sort(value: str) -> ListMaintenanceSort:
    if value in LIST_MAINTENANCE_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MAINTENANCE_SORT_VALUES!r}")
