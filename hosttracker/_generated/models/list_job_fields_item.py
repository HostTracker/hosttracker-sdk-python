from typing import Literal

ListJobFieldsItem = Literal[
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

LIST_JOB_FIELDS_ITEM_VALUES: set[ListJobFieldsItem] = {
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


def check_list_job_fields_item(value: str) -> ListJobFieldsItem:
    if value in LIST_JOB_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_JOB_FIELDS_ITEM_VALUES!r}")
