from typing import Literal

WebhookDeliveryQueryRequestFieldsItem = Literal[
    "attempts", "event", "id", "nextRetryAt", "occurredAt", "outcome", "payloadDigest", "resourceId"
]

WEBHOOK_DELIVERY_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[WebhookDeliveryQueryRequestFieldsItem] = {
    "attempts",
    "event",
    "id",
    "nextRetryAt",
    "occurredAt",
    "outcome",
    "payloadDigest",
    "resourceId",
}


def check_webhook_delivery_query_request_fields_item(value: str) -> WebhookDeliveryQueryRequestFieldsItem:
    if value in WEBHOOK_DELIVERY_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
