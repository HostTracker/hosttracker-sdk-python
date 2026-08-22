from typing import Literal

WebhookDeliveryQueryRequestOutcomeItem = Literal["delivered", "dropped", "failed", "pending"]

WEBHOOK_DELIVERY_QUERY_REQUEST_OUTCOME_ITEM_VALUES: set[WebhookDeliveryQueryRequestOutcomeItem] = {
    "delivered",
    "dropped",
    "failed",
    "pending",
}


def check_webhook_delivery_query_request_outcome_item(value: str) -> WebhookDeliveryQueryRequestOutcomeItem:
    if value in WEBHOOK_DELIVERY_QUERY_REQUEST_OUTCOME_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_QUERY_REQUEST_OUTCOME_ITEM_VALUES!r}"
    )
