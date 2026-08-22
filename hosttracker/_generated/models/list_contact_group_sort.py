from typing import Literal

ListContactGroupSort = Literal["created", "created:asc", "created:desc", "name", "name:asc", "name:desc"]

LIST_CONTACT_GROUP_SORT_VALUES: set[ListContactGroupSort] = {
    "created",
    "created:asc",
    "created:desc",
    "name",
    "name:asc",
    "name:desc",
}


def check_list_contact_group_sort(value: str) -> ListContactGroupSort:
    if value in LIST_CONTACT_GROUP_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_GROUP_SORT_VALUES!r}")
