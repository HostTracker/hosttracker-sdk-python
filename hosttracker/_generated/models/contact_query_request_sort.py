from typing import Literal

ContactQueryRequestSort = Literal[
    "address", "address:asc", "address:desc", "created", "created:asc", "created:desc", "name", "name:asc", "name:desc"
]

CONTACT_QUERY_REQUEST_SORT_VALUES: set[ContactQueryRequestSort] = {
    "address",
    "address:asc",
    "address:desc",
    "created",
    "created:asc",
    "created:desc",
    "name",
    "name:asc",
    "name:desc",
}


def check_contact_query_request_sort(value: str) -> ContactQueryRequestSort:
    if value in CONTACT_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_QUERY_REQUEST_SORT_VALUES!r}")
