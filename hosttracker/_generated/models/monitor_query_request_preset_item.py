from typing import Literal

MonitorQueryRequestPresetItem = Literal["bl:ru"]

MONITOR_QUERY_REQUEST_PRESET_ITEM_VALUES: set[MonitorQueryRequestPresetItem] = {
    "bl:ru",
}


def check_monitor_query_request_preset_item(value: str) -> MonitorQueryRequestPresetItem:
    if value in MONITOR_QUERY_REQUEST_PRESET_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_QUERY_REQUEST_PRESET_ITEM_VALUES!r}")
