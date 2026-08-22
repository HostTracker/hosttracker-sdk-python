from typing import Literal

JobItemViewStatus = Literal[
    "cancelled", "created", "createdDisabled", "deleted", "failed", "pending", "skipped", "updated"
]

JOB_ITEM_VIEW_STATUS_VALUES: set[JobItemViewStatus] = {
    "cancelled",
    "created",
    "createdDisabled",
    "deleted",
    "failed",
    "pending",
    "skipped",
    "updated",
}


def check_job_item_view_status(value: str) -> JobItemViewStatus:
    if value in JOB_ITEM_VIEW_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_ITEM_VIEW_STATUS_VALUES!r}")
