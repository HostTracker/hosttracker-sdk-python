from typing import Literal

ContactQueryRequestFieldsItem = Literal[
    "activePeriod",
    "address",
    "alertDelay",
    "billingNotifications",
    "botId",
    "confirmed",
    "created",
    "gateway",
    "groupedAlerts",
    "groups",
    "httpHeaders",
    "id",
    "language",
    "mimeType",
    "name",
    "overlimited",
    "sendCost",
    "sendNews",
    "subscription",
    "templates",
    "type",
    "updated",
]

CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ContactQueryRequestFieldsItem] = {
    "activePeriod",
    "address",
    "alertDelay",
    "billingNotifications",
    "botId",
    "confirmed",
    "created",
    "gateway",
    "groupedAlerts",
    "groups",
    "httpHeaders",
    "id",
    "language",
    "mimeType",
    "name",
    "overlimited",
    "sendCost",
    "sendNews",
    "subscription",
    "templates",
    "type",
    "updated",
}


def check_contact_query_request_fields_item(value: str) -> ContactQueryRequestFieldsItem:
    if value in CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
