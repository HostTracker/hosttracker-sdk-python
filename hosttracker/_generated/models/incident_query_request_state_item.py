from typing import Literal

IncidentQueryRequestStateItem = Literal["open", "resolved"]

INCIDENT_QUERY_REQUEST_STATE_ITEM_VALUES: set[IncidentQueryRequestStateItem] = {
    "open",
    "resolved",
}


def check_incident_query_request_state_item(value: str) -> IncidentQueryRequestStateItem:
    if value in INCIDENT_QUERY_REQUEST_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_QUERY_REQUEST_STATE_ITEM_VALUES!r}")
