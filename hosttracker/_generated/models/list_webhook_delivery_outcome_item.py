from typing import Literal

ListWebhookDeliveryOutcomeItem = Literal["delivered", "dropped", "failed", "pending"]

LIST_WEBHOOK_DELIVERY_OUTCOME_ITEM_VALUES: set[ListWebhookDeliveryOutcomeItem] = {
    "delivered",
    "dropped",
    "failed",
    "pending",
}


def check_list_webhook_delivery_outcome_item(value: str) -> ListWebhookDeliveryOutcomeItem:
    if value in LIST_WEBHOOK_DELIVERY_OUTCOME_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOK_DELIVERY_OUTCOME_ITEM_VALUES!r}")
