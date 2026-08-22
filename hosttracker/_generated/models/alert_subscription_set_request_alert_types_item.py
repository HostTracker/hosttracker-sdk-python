from typing import Literal

AlertSubscriptionSetRequestAlertTypesItem = Literal["down", "repeatedlyDown", "up"]

ALERT_SUBSCRIPTION_SET_REQUEST_ALERT_TYPES_ITEM_VALUES: set[AlertSubscriptionSetRequestAlertTypesItem] = {
    "down",
    "repeatedlyDown",
    "up",
}


def check_alert_subscription_set_request_alert_types_item(value: str) -> AlertSubscriptionSetRequestAlertTypesItem:
    if value in ALERT_SUBSCRIPTION_SET_REQUEST_ALERT_TYPES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_SUBSCRIPTION_SET_REQUEST_ALERT_TYPES_ITEM_VALUES!r}"
    )
