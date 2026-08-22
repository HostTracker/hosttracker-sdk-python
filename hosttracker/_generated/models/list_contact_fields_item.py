from typing import Literal

ListContactFieldsItem = Literal[
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

LIST_CONTACT_FIELDS_ITEM_VALUES: set[ListContactFieldsItem] = {
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


def check_list_contact_fields_item(value: str) -> ListContactFieldsItem:
    if value in LIST_CONTACT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_FIELDS_ITEM_VALUES!r}")
