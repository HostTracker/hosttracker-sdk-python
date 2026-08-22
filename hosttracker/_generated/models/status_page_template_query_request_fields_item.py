from typing import Literal

StatusPageTemplateQueryRequestFieldsItem = Literal["created", "defaultImpact", "id", "message", "title"]

STATUS_PAGE_TEMPLATE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[StatusPageTemplateQueryRequestFieldsItem] = {
    "created",
    "defaultImpact",
    "id",
    "message",
    "title",
}


def check_status_page_template_query_request_fields_item(value: str) -> StatusPageTemplateQueryRequestFieldsItem:
    if value in STATUS_PAGE_TEMPLATE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEMPLATE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
