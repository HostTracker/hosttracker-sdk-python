from typing import Literal

ContactAlertSubscriptionAlertTypesItem = Literal["down", "repeatedlyDown", "up"]

CONTACT_ALERT_SUBSCRIPTION_ALERT_TYPES_ITEM_VALUES: set[ContactAlertSubscriptionAlertTypesItem] = {
    "down",
    "repeatedlyDown",
    "up",
}


def check_contact_alert_subscription_alert_types_item(value: str) -> ContactAlertSubscriptionAlertTypesItem:
    if value in CONTACT_ALERT_SUBSCRIPTION_ALERT_TYPES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_ALERT_SUBSCRIPTION_ALERT_TYPES_ITEM_VALUES!r}"
    )
