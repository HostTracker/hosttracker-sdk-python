from typing import Literal

JobViewState = Literal["cancelled", "failed", "interrupted", "partial", "queued", "running", "succeeded"]

JOB_VIEW_STATE_VALUES: set[JobViewState] = {
    "cancelled",
    "failed",
    "interrupted",
    "partial",
    "queued",
    "running",
    "succeeded",
}


def check_job_view_state(value: str) -> JobViewState:
    if value in JOB_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_VIEW_STATE_VALUES!r}")
