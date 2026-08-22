from typing import Literal

ListContactAlertFieldsItem = Literal["alertTypes", "created", "monitor"]

LIST_CONTACT_ALERT_FIELDS_ITEM_VALUES: set[ListContactAlertFieldsItem] = {
    "alertTypes",
    "created",
    "monitor",
}


def check_list_contact_alert_fields_item(value: str) -> ListContactAlertFieldsItem:
    if value in LIST_CONTACT_ALERT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_ALERT_FIELDS_ITEM_VALUES!r}")
