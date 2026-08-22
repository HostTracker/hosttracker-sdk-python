from typing import Literal

JobCompletedEnvelopeEvent = Literal["job.completed"]

JOB_COMPLETED_ENVELOPE_EVENT_VALUES: set[JobCompletedEnvelopeEvent] = {
    "job.completed",
}


def check_job_completed_envelope_event(value: str) -> JobCompletedEnvelopeEvent:
    if value in JOB_COMPLETED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JOB_COMPLETED_ENVELOPE_EVENT_VALUES!r}")
