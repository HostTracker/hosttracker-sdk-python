from typing import Literal

ListWebhookDeliveryFieldsItem = Literal[
    "attempts", "event", "id", "nextRetryAt", "occurredAt", "outcome", "payloadDigest", "resourceId"
]

LIST_WEBHOOK_DELIVERY_FIELDS_ITEM_VALUES: set[ListWebhookDeliveryFieldsItem] = {
    "attempts",
    "event",
    "id",
    "nextRetryAt",
    "occurredAt",
    "outcome",
    "payloadDigest",
    "resourceId",
}


def check_list_webhook_delivery_fields_item(value: str) -> ListWebhookDeliveryFieldsItem:
    if value in LIST_WEBHOOK_DELIVERY_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOK_DELIVERY_FIELDS_ITEM_VALUES!r}")
