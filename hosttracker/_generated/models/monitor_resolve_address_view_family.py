from typing import Literal

MonitorResolveAddressViewFamily = Literal["ipv4", "ipv6"]

MONITOR_RESOLVE_ADDRESS_VIEW_FAMILY_VALUES: set[MonitorResolveAddressViewFamily] = {
    "ipv4",
    "ipv6",
}


def check_monitor_resolve_address_view_family(value: str) -> MonitorResolveAddressViewFamily:
    if value in MONITOR_RESOLVE_ADDRESS_VIEW_FAMILY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_RESOLVE_ADDRESS_VIEW_FAMILY_VALUES!r}")
