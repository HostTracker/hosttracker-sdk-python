from typing import Literal

StatusPageIncidentPatchRequestKind = Literal["incident", "maintenance"]

STATUS_PAGE_INCIDENT_PATCH_REQUEST_KIND_VALUES: set[StatusPageIncidentPatchRequestKind] = {
    "incident",
    "maintenance",
}


def check_status_page_incident_patch_request_kind(value: str) -> StatusPageIncidentPatchRequestKind:
    if value in STATUS_PAGE_INCIDENT_PATCH_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_PATCH_REQUEST_KIND_VALUES!r}")
