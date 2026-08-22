from typing import Literal

MonitorTypeQueryRequestFieldsItem = Literal[
    "accountLimits",
    "attachable",
    "attachableTo",
    "creatable",
    "entitlement",
    "fixedInterval",
    "label",
    "minInterval",
    "presets",
    "requiresPool",
    "type",
]

MONITOR_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MonitorTypeQueryRequestFieldsItem] = {
    "accountLimits",
    "attachable",
    "attachableTo",
    "creatable",
    "entitlement",
    "fixedInterval",
    "label",
    "minInterval",
    "presets",
    "requiresPool",
    "type",
}


def check_monitor_type_query_request_fields_item(value: str) -> MonitorTypeQueryRequestFieldsItem:
    if value in MONITOR_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_TYPE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
