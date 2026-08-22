from typing import Literal

AlertSubscriptionBulkItemAlertTypesItem = Literal["down", "repeatedlyDown", "up"]

ALERT_SUBSCRIPTION_BULK_ITEM_ALERT_TYPES_ITEM_VALUES: set[AlertSubscriptionBulkItemAlertTypesItem] = {
    "down",
    "repeatedlyDown",
    "up",
}


def check_alert_subscription_bulk_item_alert_types_item(value: str) -> AlertSubscriptionBulkItemAlertTypesItem:
    if value in ALERT_SUBSCRIPTION_BULK_ITEM_ALERT_TYPES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_SUBSCRIPTION_BULK_ITEM_ALERT_TYPES_ITEM_VALUES!r}"
    )
