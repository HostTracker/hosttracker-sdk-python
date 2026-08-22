from typing import Literal

ListReportByContactFieldsItem = Literal["contact", "subscriptions"]

LIST_REPORT_BY_CONTACT_FIELDS_ITEM_VALUES: set[ListReportByContactFieldsItem] = {
    "contact",
    "subscriptions",
}


def check_list_report_by_contact_fields_item(value: str) -> ListReportByContactFieldsItem:
    if value in LIST_REPORT_BY_CONTACT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_BY_CONTACT_FIELDS_ITEM_VALUES!r}")
