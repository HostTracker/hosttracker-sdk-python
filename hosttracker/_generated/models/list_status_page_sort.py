from typing import Literal

ListStatusPageSort = Literal[
    "created", "created:asc", "created:desc", "slug", "slug:asc", "slug:desc", "title", "title:asc", "title:desc"
]

LIST_STATUS_PAGE_SORT_VALUES: set[ListStatusPageSort] = {
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


def check_list_status_page_sort(value: str) -> ListStatusPageSort:
    if value in LIST_STATUS_PAGE_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_STATUS_PAGE_SORT_VALUES!r}")
