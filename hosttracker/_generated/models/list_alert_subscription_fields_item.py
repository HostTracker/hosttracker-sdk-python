from typing import Literal

ListAlertSubscriptionFieldsItem = Literal["alertTypes", "contact", "created", "id", "monitor"]

LIST_ALERT_SUBSCRIPTION_FIELDS_ITEM_VALUES: set[ListAlertSubscriptionFieldsItem] = {
    "alertTypes",
    "contact",
    "created",
    "id",
    "monitor",
}


def check_list_alert_subscription_fields_item(value: str) -> ListAlertSubscriptionFieldsItem:
    if value in LIST_ALERT_SUBSCRIPTION_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_SUBSCRIPTION_FIELDS_ITEM_VALUES!r}")
