from typing import Literal

GetJobFieldsItem = Literal[
    "cancelRequested",
    "created",
    "error",
    "expiresAt",
    "finishedAt",
    "hasMore",
    "id",
    "interruptedAt",
    "kind",
    "nextCursor",
    "progress",
    "results",
    "resultSummary",
    "resumedCount",
    "scope",
    "startedAt",
    "state",
    "summary",
]

GET_JOB_FIELDS_ITEM_VALUES: set[GetJobFieldsItem] = {
    "cancelRequested",
    "created",
    "error",
    "expiresAt",
    "finishedAt",
    "hasMore",
    "id",
    "interruptedAt",
    "kind",
    "nextCursor",
    "progress",
    "results",
    "resultSummary",
    "resumedCount",
    "scope",
    "startedAt",
    "state",
    "summary",
}


def check_get_job_fields_item(value: str) -> GetJobFieldsItem:
    if value in GET_JOB_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_JOB_FIELDS_ITEM_VALUES!r}")
