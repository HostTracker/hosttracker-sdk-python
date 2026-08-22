from typing import Literal

WebhookQueryRequestFieldsItem = Literal[
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

WEBHOOK_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[WebhookQueryRequestFieldsItem] = {
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


def check_webhook_query_request_fields_item(value: str) -> WebhookQueryRequestFieldsItem:
    if value in WEBHOOK_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
