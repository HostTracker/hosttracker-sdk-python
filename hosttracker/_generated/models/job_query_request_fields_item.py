from typing import Literal

JobQueryRequestFieldsItem = Literal[
    "cancelRequested",
    "created",
    "expiresAt",
    "finishedAt",
    "id",
    "interruptedAt",
    "kind",
    "progress",
    "resultsUrl",
    "resumedCount",
    "scope",
    "startedAt",
    "state",
    "summary",
]

JOB_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[JobQueryRequestFieldsItem] = {
    "cancelRequested",
    "created",
    "expiresAt",
    "finishedAt",
    "id",
    "interruptedAt",
    "kind",
    "progress",
    "resultsUrl",
    "resumedCount",
    "scope",
    "startedAt",
    "state",
    "summary",
}


def check_job_query_request_fields_item(value: str) -> JobQueryRequestFieldsItem:
    if value in JOB_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
