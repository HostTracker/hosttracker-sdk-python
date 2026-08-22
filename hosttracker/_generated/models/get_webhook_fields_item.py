from typing import Literal

GetWebhookFieldsItem = Literal[
    "consecutiveFailures",
    "created",
    "disabledReason",
    "enabled",
    "events",
    "headers",
    "id",
    "lastDeliveryAt",
    "name",
    "scope",
    "secret",
    "updated",
    "url",
]

GET_WEBHOOK_FIELDS_ITEM_VALUES: set[GetWebhookFieldsItem] = {
    "consecutiveFailures",
    "created",
    "disabledReason",
    "enabled",
    "events",
    "headers",
    "id",
    "lastDeliveryAt",
    "name",
    "scope",
    "secret",
    "updated",
    "url",
}


def check_get_webhook_fields_item(value: str) -> GetWebhookFieldsItem:
    if value in GET_WEBHOOK_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_WEBHOOK_FIELDS_ITEM_VALUES!r}")
