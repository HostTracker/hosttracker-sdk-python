from typing import Literal

MonitorBulkItemOnOverlimit = Literal["disable", "fail"]

MONITOR_BULK_ITEM_ON_OVERLIMIT_VALUES: set[MonitorBulkItemOnOverlimit] = {
    "disable",
    "fail",
}


def check_monitor_bulk_item_on_overlimit(value: str) -> MonitorBulkItemOnOverlimit:
    if value in MONITOR_BULK_ITEM_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_ITEM_ON_OVERLIMIT_VALUES!r}")
