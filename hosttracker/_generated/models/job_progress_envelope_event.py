from typing import Literal

JobProgressEnvelopeEvent = Literal["job.progress"]

JOB_PROGRESS_ENVELOPE_EVENT_VALUES: set[JobProgressEnvelopeEvent] = {
    "job.progress",
}


def check_job_progress_envelope_event(value: str) -> JobProgressEnvelopeEvent:
    if value in JOB_PROGRESS_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_PROGRESS_ENVELOPE_EVENT_VALUES!r}")
