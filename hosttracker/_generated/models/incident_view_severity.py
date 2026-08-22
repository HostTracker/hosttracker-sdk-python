from typing import Literal

IncidentViewSeverity = Literal["critical", "major", "minor"]

INCIDENT_VIEW_SEVERITY_VALUES: set[IncidentViewSeverity] = {
    "critical",
    "major",
    "minor",
}


def check_incident_view_severity(value: str) -> IncidentViewSeverity:
    if value in INCIDENT_VIEW_SEVERITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_VIEW_SEVERITY_VALUES!r}")
