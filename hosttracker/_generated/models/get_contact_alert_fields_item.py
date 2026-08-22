from typing import Literal

GetContactAlertFieldsItem = Literal["alertTypes", "created", "monitor"]

GET_CONTACT_ALERT_FIELDS_ITEM_VALUES: set[GetContactAlertFieldsItem] = {
    "alertTypes",
    "created",
    "monitor",
}


def check_get_contact_alert_fields_item(value: str) -> GetContactAlertFieldsItem:
    if value in GET_CONTACT_ALERT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONTACT_ALERT_FIELDS_ITEM_VALUES!r}")
