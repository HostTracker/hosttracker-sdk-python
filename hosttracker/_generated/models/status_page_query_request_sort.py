from typing import Literal

StatusPageQueryRequestSort = Literal[
    "created", "created:asc", "created:desc", "slug", "slug:asc", "slug:desc", "title", "title:asc", "title:desc"
]

STATUS_PAGE_QUERY_REQUEST_SORT_VALUES: set[StatusPageQueryRequestSort] = {
    "created",
    "created:asc",
    "created:desc",
    "slug",
    "slug:asc",
    "slug:desc",
    "title",
    "title:asc",
    "title:desc",
}


def check_status_page_query_request_sort(value: str) -> StatusPageQueryRequestSort:
    if value in STATUS_PAGE_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_QUERY_REQUEST_SORT_VALUES!r}")
