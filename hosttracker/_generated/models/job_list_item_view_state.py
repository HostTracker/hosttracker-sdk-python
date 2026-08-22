from typing import Literal

JobListItemViewState = Literal["cancelled", "failed", "interrupted", "partial", "queued", "running", "succeeded"]

JOB_LIST_ITEM_VIEW_STATE_VALUES: set[JobListItemViewState] = {
    "cancelled",
    "failed",
    "interrupted",
    "partial",
    "queued",
    "running",
    "succeeded",
}


def check_job_list_item_view_state(value: str) -> JobListItemViewState:
    if value in JOB_LIST_ITEM_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_LIST_ITEM_VIEW_STATE_VALUES!r}")
