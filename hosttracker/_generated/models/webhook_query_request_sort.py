from typing import Literal

WebhookQueryRequestSort = Literal[
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

WEBHOOK_QUERY_REQUEST_SORT_VALUES: set[WebhookQueryRequestSort] = {
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


def check_webhook_query_request_sort(value: str) -> WebhookQueryRequestSort:
    if value in WEBHOOK_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_QUERY_REQUEST_SORT_VALUES!r}")
