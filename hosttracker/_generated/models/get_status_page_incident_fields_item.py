from typing import Literal

GetStatusPageIncidentFieldsItem = Literal[
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

GET_STATUS_PAGE_INCIDENT_FIELDS_ITEM_VALUES: set[GetStatusPageIncidentFieldsItem] = {
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


def check_get_status_page_incident_fields_item(value: str) -> GetStatusPageIncidentFieldsItem:
    if value in GET_STATUS_PAGE_INCIDENT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_STATUS_PAGE_INCIDENT_FIELDS_ITEM_VALUES!r}")
