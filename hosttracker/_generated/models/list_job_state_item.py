from typing import Literal

ListJobStateItem = Literal["cancelled", "failed", "interrupted", "partial", "queued", "running", "succeeded"]

LIST_JOB_STATE_ITEM_VALUES: set[ListJobStateItem] = {
    "cancelled",
    "failed",
    "interrupted",
    "partial",
    "queued",
    "running",
    "succeeded",
}


def check_list_job_state_item(value: str) -> ListJobStateItem:
    if value in LIST_JOB_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_JOB_STATE_ITEM_VALUES!r}")
