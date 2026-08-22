from typing import Literal

GetAlertSubscriptionFieldsItem = Literal["alertTypes", "contact", "created", "id", "monitor"]

GET_ALERT_SUBSCRIPTION_FIELDS_ITEM_VALUES: set[GetAlertSubscriptionFieldsItem] = {
    "alertTypes",
    "contact",
    "created",
    "id",
    "monitor",
}


def check_get_alert_subscription_fields_item(value: str) -> GetAlertSubscriptionFieldsItem:
    if value in GET_ALERT_SUBSCRIPTION_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ALERT_SUBSCRIPTION_FIELDS_ITEM_VALUES!r}")
