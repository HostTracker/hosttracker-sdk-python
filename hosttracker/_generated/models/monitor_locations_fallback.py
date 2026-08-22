from typing import Literal

MonitorLocationsFallback = Literal["geo", "starve", "world"]

MONITOR_LOCATIONS_FALLBACK_VALUES: set[MonitorLocationsFallback] = {
    "geo",
    "starve",
    "world",
}


def check_monitor_locations_fallback(value: str) -> MonitorLocationsFallback:
    if value in MONITOR_LOCATIONS_FALLBACK_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_LOCATIONS_FALLBACK_VALUES!r}")
