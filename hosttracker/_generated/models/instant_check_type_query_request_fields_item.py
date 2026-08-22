from typing import Literal

InstantCheckTypeQueryRequestFieldsItem = Literal[
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

INSTANT_CHECK_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[InstantCheckTypeQueryRequestFieldsItem] = {
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


def check_instant_check_type_query_request_fields_item(value: str) -> InstantCheckTypeQueryRequestFieldsItem:
    if value in INSTANT_CHECK_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INSTANT_CHECK_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
