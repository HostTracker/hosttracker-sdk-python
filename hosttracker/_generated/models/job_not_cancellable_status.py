from typing import Literal

JobNotCancellableStatus = Literal[409]

JOB_NOT_CANCELLABLE_STATUS_VALUES: set[JobNotCancellableStatus] = {
    409,
}


def check_job_not_cancellable_status(value: int) -> JobNotCancellableStatus:
    if value in JOB_NOT_CANCELLABLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_NOT_CANCELLABLE_STATUS_VALUES!r}")
