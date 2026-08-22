from typing import Literal

GetContactFieldsItem = Literal[
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

GET_CONTACT_FIELDS_ITEM_VALUES: set[GetContactFieldsItem] = {
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


def check_get_contact_fields_item(value: str) -> GetContactFieldsItem:
    if value in GET_CONTACT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONTACT_FIELDS_ITEM_VALUES!r}")
