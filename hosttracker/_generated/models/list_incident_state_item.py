from typing import Literal

ListIncidentStateItem = Literal["open", "resolved"]

LIST_INCIDENT_STATE_ITEM_VALUES: set[ListIncidentStateItem] = {
    "open",
    "resolved",
}


def check_list_incident_state_item(value: str) -> ListIncidentStateItem:
    if value in LIST_INCIDENT_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_STATE_ITEM_VALUES!r}")
