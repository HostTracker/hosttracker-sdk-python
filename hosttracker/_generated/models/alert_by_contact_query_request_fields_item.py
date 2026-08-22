from typing import Literal

AlertByContactQueryRequestFieldsItem = Literal["contact", "subscriptions"]

ALERT_BY_CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[AlertByContactQueryRequestFieldsItem] = {
    "contact",
    "subscriptions",
}


def check_alert_by_contact_query_request_fields_item(value: str) -> AlertByContactQueryRequestFieldsItem:
    if value in ALERT_BY_CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_BY_CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
