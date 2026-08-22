from typing import Literal

ListWebhookSort = Literal[
    "created",
    "created:asc",
    "created:desc",
    "name",
    "name:asc",
    "name:desc",
    "updated",
    "updated:asc",
    "updated:desc",
    "url",
    "url:asc",
    "url:desc",
]

LIST_WEBHOOK_SORT_VALUES: set[ListWebhookSort] = {
    "created",
    "created:asc",
    "created:desc",
    "name",
    "name:asc",
    "name:desc",
    "updated",
    "updated:asc",
    "updated:desc",
    "url",
    "url:asc",
    "url:desc",
}


def check_list_webhook_sort(value: str) -> ListWebhookSort:
    if value in LIST_WEBHOOK_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOK_SORT_VALUES!r}")
