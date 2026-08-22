from typing import Literal

StatusPageIncidentViewImpact = Literal["major", "minor"]

STATUS_PAGE_INCIDENT_VIEW_IMPACT_VALUES: set[StatusPageIncidentViewImpact] = {
    "major",
    "minor",
}


def check_status_page_incident_view_impact(value: str) -> StatusPageIncidentViewImpact:
    if value in STATUS_PAGE_INCIDENT_VIEW_IMPACT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_VIEW_IMPACT_VALUES!r}")
