from typing import Literal

ListMonitorPresetItem = Literal["bl:ru"]

LIST_MONITOR_PRESET_ITEM_VALUES: set[ListMonitorPresetItem] = {
    "bl:ru",
}


def check_list_monitor_preset_item(value: str) -> ListMonitorPresetItem:
    if value in LIST_MONITOR_PRESET_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_PRESET_ITEM_VALUES!r}")
