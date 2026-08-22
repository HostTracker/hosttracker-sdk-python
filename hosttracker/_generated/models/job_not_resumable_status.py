from typing import Literal

JobNotResumableStatus = Literal[409]

JOB_NOT_RESUMABLE_STATUS_VALUES: set[JobNotResumableStatus] = {
    409,
}


def check_job_not_resumable_status(value: int) -> JobNotResumableStatus:
    if value in JOB_NOT_RESUMABLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_NOT_RESUMABLE_STATUS_VALUES!r}")
