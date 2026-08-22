from typing import Literal

ListStatusPageTemplateFieldsItem = Literal["created", "defaultImpact", "id", "message", "title"]

LIST_STATUS_PAGE_TEMPLATE_FIELDS_ITEM_VALUES: set[ListStatusPageTemplateFieldsItem] = {
    "created",
    "defaultImpact",
    "id",
    "message",
    "title",
}


def check_list_status_page_template_fields_item(value: str) -> ListStatusPageTemplateFieldsItem:
    if value in LIST_STATUS_PAGE_TEMPLATE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_STATUS_PAGE_TEMPLATE_FIELDS_ITEM_VALUES!r}")
