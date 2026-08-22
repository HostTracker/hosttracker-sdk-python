from typing import Literal

MaintenanceQueryRequestFieldsItem = Literal[
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

MAINTENANCE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MaintenanceQueryRequestFieldsItem] = {
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


def check_maintenance_query_request_fields_item(value: str) -> MaintenanceQueryRequestFieldsItem:
    if value in MAINTENANCE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
