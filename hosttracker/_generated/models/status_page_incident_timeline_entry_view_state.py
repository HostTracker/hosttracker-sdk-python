from typing import Literal

StatusPageIncidentTimelineEntryViewState = Literal["identified", "investigating", "monitoring", "resolved"]

STATUS_PAGE_INCIDENT_TIMELINE_ENTRY_VIEW_STATE_VALUES: set[StatusPageIncidentTimelineEntryViewState] = {
    "identified",
    "investigating",
    "monitoring",
    "resolved",
}


def check_status_page_incident_timeline_entry_view_state(value: str) -> StatusPageIncidentTimelineEntryViewState:
    if value in STATUS_PAGE_INCIDENT_TIMELINE_ENTRY_VIEW_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_TIMELINE_ENTRY_VIEW_STATE_VALUES!r}"
    )
