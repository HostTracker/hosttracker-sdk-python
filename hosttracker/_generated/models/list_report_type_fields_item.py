from typing import Literal

ListReportTypeFieldsItem = Literal["formats", "frequencies", "label", "sections", "type"]

LIST_REPORT_TYPE_FIELDS_ITEM_VALUES: set[ListReportTypeFieldsItem] = {
    "formats",
    "frequencies",
    "label",
    "sections",
    "type",
}


def check_list_report_type_fields_item(value: str) -> ListReportTypeFieldsItem:
    if value in LIST_REPORT_TYPE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_TYPE_FIELDS_ITEM_VALUES!r}")
