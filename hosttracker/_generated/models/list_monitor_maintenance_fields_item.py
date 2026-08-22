from typing import Literal

ListMonitorMaintenanceFieldsItem = Literal[
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

LIST_MONITOR_MAINTENANCE_FIELDS_ITEM_VALUES: set[ListMonitorMaintenanceFieldsItem] = {
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


def check_list_monitor_maintenance_fields_item(value: str) -> ListMonitorMaintenanceFieldsItem:
    if value in LIST_MONITOR_MAINTENANCE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_MAINTENANCE_FIELDS_ITEM_VALUES!r}")
