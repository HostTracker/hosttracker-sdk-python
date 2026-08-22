from typing import Literal

ListMonitorTypeFieldsItem = Literal[
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

LIST_MONITOR_TYPE_FIELDS_ITEM_VALUES: set[ListMonitorTypeFieldsItem] = {
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


def check_list_monitor_type_fields_item(value: str) -> ListMonitorTypeFieldsItem:
    if value in LIST_MONITOR_TYPE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_TYPE_FIELDS_ITEM_VALUES!r}")
