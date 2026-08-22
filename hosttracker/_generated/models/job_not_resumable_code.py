from typing import Literal

JobNotResumableCode = Literal["job_not_resumable"]

JOB_NOT_RESUMABLE_CODE_VALUES: set[JobNotResumableCode] = {
    "job_not_resumable",
}


def check_job_not_resumable_code(value: str) -> JobNotResumableCode:
    if value in JOB_NOT_RESUMABLE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_NOT_RESUMABLE_CODE_VALUES!r}")
