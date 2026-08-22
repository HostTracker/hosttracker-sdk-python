from typing import Literal

ListStatusPageIncidentFieldsItem = Literal[
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

LIST_STATUS_PAGE_INCIDENT_FIELDS_ITEM_VALUES: set[ListStatusPageIncidentFieldsItem] = {
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


def check_list_status_page_incident_fields_item(value: str) -> ListStatusPageIncidentFieldsItem:
    if value in LIST_STATUS_PAGE_INCIDENT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_STATUS_PAGE_INCIDENT_FIELDS_ITEM_VALUES!r}")
