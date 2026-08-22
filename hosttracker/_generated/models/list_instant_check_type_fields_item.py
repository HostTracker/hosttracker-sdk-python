from typing import Literal

ListInstantCheckTypeFieldsItem = Literal[
    "agentRouted",
    "description",
    "estimatedDurationSec",
    "example",
    "experimental",
    "label",
    "options",
    "retryAfter",
    "type",
]

LIST_INSTANT_CHECK_TYPE_FIELDS_ITEM_VALUES: set[ListInstantCheckTypeFieldsItem] = {
    "agentRouted",
    "description",
    "estimatedDurationSec",
    "example",
    "experimental",
    "label",
    "options",
    "retryAfter",
    "type",
}


def check_list_instant_check_type_fields_item(value: str) -> ListInstantCheckTypeFieldsItem:
    if value in LIST_INSTANT_CHECK_TYPE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INSTANT_CHECK_TYPE_FIELDS_ITEM_VALUES!r}")
