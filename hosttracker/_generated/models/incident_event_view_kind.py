from typing import Literal

IncidentEventViewKind = Literal["enter", "exit"]

INCIDENT_EVENT_VIEW_KIND_VALUES: set[IncidentEventViewKind] = {
    "enter",
    "exit",
}


def check_incident_event_view_kind(value: str) -> IncidentEventViewKind:
    if value in INCIDENT_EVENT_VIEW_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_VIEW_KIND_VALUES!r}")
