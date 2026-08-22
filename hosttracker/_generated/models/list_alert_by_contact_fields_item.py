from typing import Literal

ListAlertByContactFieldsItem = Literal["contact", "subscriptions"]

LIST_ALERT_BY_CONTACT_FIELDS_ITEM_VALUES: set[ListAlertByContactFieldsItem] = {
    "contact",
    "subscriptions",
}


def check_list_alert_by_contact_fields_item(value: str) -> ListAlertByContactFieldsItem:
    if value in LIST_ALERT_BY_CONTACT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_BY_CONTACT_FIELDS_ITEM_VALUES!r}")
