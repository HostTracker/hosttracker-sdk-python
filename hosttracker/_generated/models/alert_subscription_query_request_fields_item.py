from typing import Literal

AlertSubscriptionQueryRequestFieldsItem = Literal["alertTypes", "contact", "created", "id", "monitor"]

ALERT_SUBSCRIPTION_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[AlertSubscriptionQueryRequestFieldsItem] = {
    "alertTypes",
    "contact",
    "created",
    "id",
    "monitor",
}


def check_alert_subscription_query_request_fields_item(value: str) -> AlertSubscriptionQueryRequestFieldsItem:
    if value in ALERT_SUBSCRIPTION_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_SUBSCRIPTION_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
