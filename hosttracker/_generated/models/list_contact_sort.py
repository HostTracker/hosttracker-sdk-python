from typing import Literal

ListContactSort = Literal[
    "address", "address:asc", "address:desc", "created", "created:asc", "created:desc", "name", "name:asc", "name:desc"
]

LIST_CONTACT_SORT_VALUES: set[ListContactSort] = {
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


def check_list_contact_sort(value: str) -> ListContactSort:
    if value in LIST_CONTACT_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_SORT_VALUES!r}")
