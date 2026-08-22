from typing import Literal

MonitorMaintenanceQueryRequestFieldsItem = Literal[
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

MONITOR_MAINTENANCE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MonitorMaintenanceQueryRequestFieldsItem] = {
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


def check_monitor_maintenance_query_request_fields_item(value: str) -> MonitorMaintenanceQueryRequestFieldsItem:
    if value in MONITOR_MAINTENANCE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_MAINTENANCE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
