from typing import Literal

GetMonitorTypeFieldsItem = Literal["attachedSchema", "schema", "type"]

GET_MONITOR_TYPE_FIELDS_ITEM_VALUES: set[GetMonitorTypeFieldsItem] = {
    "attachedSchema",
    "schema",
    "type",
}


def check_get_monitor_type_fields_item(value: str) -> GetMonitorTypeFieldsItem:
    if value in GET_MONITOR_TYPE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MONITOR_TYPE_FIELDS_ITEM_VALUES!r}")
