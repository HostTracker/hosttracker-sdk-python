from typing import Literal

ContactAlertQueryRequestFieldsItem = Literal["alertTypes", "created", "monitor"]

CONTACT_ALERT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ContactAlertQueryRequestFieldsItem] = {
    "alertTypes",
    "created",
    "monitor",
}


def check_contact_alert_query_request_fields_item(value: str) -> ContactAlertQueryRequestFieldsItem:
    if value in CONTACT_ALERT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_ALERT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
