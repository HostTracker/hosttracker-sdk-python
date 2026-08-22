from typing import Literal

JobNotCancellableCode = Literal["job_not_cancellable"]

JOB_NOT_CANCELLABLE_CODE_VALUES: set[JobNotCancellableCode] = {
    "job_not_cancellable",
}


def check_job_not_cancellable_code(value: str) -> JobNotCancellableCode:
    if value in JOB_NOT_CANCELLABLE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_NOT_CANCELLABLE_CODE_VALUES!r}")
