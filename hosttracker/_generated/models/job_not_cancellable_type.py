from typing import Literal

JobNotCancellableType = Literal["https://api2.host-tracker.com/problems/job-not-cancellable"]

JOB_NOT_CANCELLABLE_TYPE_VALUES: set[JobNotCancellableType] = {
    "https://api2.host-tracker.com/problems/job-not-cancellable",
}


def check_job_not_cancellable_type(value: str) -> JobNotCancellableType:
    if value in JOB_NOT_CANCELLABLE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_NOT_CANCELLABLE_TYPE_VALUES!r}")
