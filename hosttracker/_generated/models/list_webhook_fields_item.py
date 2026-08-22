from typing import Literal

ListWebhookFieldsItem = Literal[
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

LIST_WEBHOOK_FIELDS_ITEM_VALUES: set[ListWebhookFieldsItem] = {
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


def check_list_webhook_fields_item(value: str) -> ListWebhookFieldsItem:
    if value in LIST_WEBHOOK_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOK_FIELDS_ITEM_VALUES!r}")
