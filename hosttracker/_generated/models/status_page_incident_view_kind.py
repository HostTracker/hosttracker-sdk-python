from typing import Literal

StatusPageIncidentViewKind = Literal["incident", "maintenance"]

STATUS_PAGE_INCIDENT_VIEW_KIND_VALUES: set[StatusPageIncidentViewKind] = {
    "incident",
    "maintenance",
}


def check_status_page_incident_view_kind(value: str) -> StatusPageIncidentViewKind:
    if value in STATUS_PAGE_INCIDENT_VIEW_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_VIEW_KIND_VALUES!r}")
