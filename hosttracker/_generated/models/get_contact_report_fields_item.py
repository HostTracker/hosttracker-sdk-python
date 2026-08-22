from typing import Literal

GetContactReportFieldsItem = Literal["created", "frequencies", "monitor"]

GET_CONTACT_REPORT_FIELDS_ITEM_VALUES: set[GetContactReportFieldsItem] = {
    "created",
    "frequencies",
    "monitor",
}


def check_get_contact_report_fields_item(value: str) -> GetContactReportFieldsItem:
    if value in GET_CONTACT_REPORT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONTACT_REPORT_FIELDS_ITEM_VALUES!r}")
