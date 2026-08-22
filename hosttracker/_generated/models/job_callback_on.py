from typing import Literal

JobCallbackOn = Literal["completed", "progress"]

JOB_CALLBACK_ON_VALUES: set[JobCallbackOn] = {
    "completed",
    "progress",
}


def check_job_callback_on(value: str) -> JobCallbackOn:
    if value in JOB_CALLBACK_ON_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_CALLBACK_ON_VALUES!r}")
