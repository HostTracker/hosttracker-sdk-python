from typing import Literal

ContactGroupQueryRequestSort = Literal["created", "created:asc", "created:desc", "name", "name:asc", "name:desc"]

CONTACT_GROUP_QUERY_REQUEST_SORT_VALUES: set[ContactGroupQueryRequestSort] = {
    "created",
    "created:asc",
    "created:desc",
    "name",
    "name:asc",
    "name:desc",
}


def check_contact_group_query_request_sort(value: str) -> ContactGroupQueryRequestSort:
    if value in CONTACT_GROUP_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_QUERY_REQUEST_SORT_VALUES!r}")
