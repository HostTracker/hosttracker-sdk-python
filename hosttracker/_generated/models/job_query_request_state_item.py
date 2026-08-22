from typing import Literal

JobQueryRequestStateItem = Literal["cancelled", "failed", "interrupted", "partial", "queued", "running", "succeeded"]

JOB_QUERY_REQUEST_STATE_ITEM_VALUES: set[JobQueryRequestStateItem] = {
    "cancelled",
    "failed",
    "interrupted",
    "partial",
    "queued",
    "running",
    "succeeded",
}


def check_job_query_request_state_item(value: str) -> JobQueryRequestStateItem:
    if value in JOB_QUERY_REQUEST_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_QUERY_REQUEST_STATE_ITEM_VALUES!r}")
