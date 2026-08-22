from typing import Literal

ListMaintenanceFieldsItem = Literal[
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

LIST_MAINTENANCE_FIELDS_ITEM_VALUES: set[ListMaintenanceFieldsItem] = {
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


def check_list_maintenance_fields_item(value: str) -> ListMaintenanceFieldsItem:
    if value in LIST_MAINTENANCE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MAINTENANCE_FIELDS_ITEM_VALUES!r}")
