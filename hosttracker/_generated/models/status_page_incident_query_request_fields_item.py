from typing import Literal

StatusPageIncidentQueryRequestFieldsItem = Literal[
    "componentIds",
    "componentNames",
    "created",
    "id",
    "impact",
    "kind",
    "postmortem",
    "resolvedAt",
    "scheduledEnd",
    "scheduledStart",
    "state",
    "timeline",
    "title",
]

STATUS_PAGE_INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[StatusPageIncidentQueryRequestFieldsItem] = {
    "componentIds",
    "componentNames",
    "created",
    "id",
    "impact",
    "kind",
    "postmortem",
    "resolvedAt",
    "scheduledEnd",
    "scheduledStart",
    "state",
    "timeline",
    "title",
}


def check_status_page_incident_query_request_fields_item(value: str) -> StatusPageIncidentQueryRequestFieldsItem:
    if value in STATUS_PAGE_INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
