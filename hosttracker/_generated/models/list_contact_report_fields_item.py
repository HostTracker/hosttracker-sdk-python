from typing import Literal

ListContactReportFieldsItem = Literal["created", "frequencies", "monitor"]

LIST_CONTACT_REPORT_FIELDS_ITEM_VALUES: set[ListContactReportFieldsItem] = {
    "created",
    "frequencies",
    "monitor",
}


def check_list_contact_report_fields_item(value: str) -> ListContactReportFieldsItem:
    if value in LIST_CONTACT_REPORT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_REPORT_FIELDS_ITEM_VALUES!r}")
