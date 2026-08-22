from typing import Literal

JobNotResumableType = Literal["https://api2.host-tracker.com/problems/job-not-resumable"]

JOB_NOT_RESUMABLE_TYPE_VALUES: set[JobNotResumableType] = {
    "https://api2.host-tracker.com/problems/job-not-resumable",
}


def check_job_not_resumable_type(value: str) -> JobNotResumableType:
    if value in JOB_NOT_RESUMABLE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_NOT_RESUMABLE_TYPE_VALUES!r}")
