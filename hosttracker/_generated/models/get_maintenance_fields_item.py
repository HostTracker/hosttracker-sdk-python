from typing import Literal

GetMaintenanceFieldsItem = Literal[
    "created",
    "durationSec",
    "enabled",
    "from",
    "id",
    "monitorIds",
    "monitors",
    "name",
    "overlimited",
    "recurrence",
    "state",
    "suppress",
    "timezone",
    "to",
    "updated",
]

GET_MAINTENANCE_FIELDS_ITEM_VALUES: set[GetMaintenanceFieldsItem] = {
    "created",
    "durationSec",
    "enabled",
    "from",
    "id",
    "monitorIds",
    "monitors",
    "name",
    "overlimited",
    "recurrence",
    "state",
    "suppress",
    "timezone",
    "to",
    "updated",
}


def check_get_maintenance_fields_item(value: str) -> GetMaintenanceFieldsItem:
    if value in GET_MAINTENANCE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MAINTENANCE_FIELDS_ITEM_VALUES!r}")
