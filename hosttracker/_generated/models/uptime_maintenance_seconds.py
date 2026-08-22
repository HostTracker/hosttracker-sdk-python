from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UptimeMaintenanceSeconds")


@_attrs_define
class UptimeMaintenanceSeconds:
    """How much of a bucket fell inside a maintenance window, split by what the monitor was doing at the time. This
    replaced a single `maintenanceSec` total, which could not answer the question the figure exists for. Only the part
    of a window that overlapped real DOWNTIME is excused from the uptime figure - a window scheduled while the monitor
    was answering normally excuses nothing - so one combined number left a client unable to reproduce, or even sanity-
    check, the percentage beside it.

    """

    up_sec: int
    """ Seconds inside a maintenance window during which the monitor was UP. Counts toward uptime, exactly as any
    other up-time does. """
    down_sec: int
    """ Seconds inside a maintenance window during which the monitor was DOWN. This is the excused downtime: it is
    taken out of the uptime denominator and out of the error budget. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up_sec = self.up_sec

        down_sec = self.down_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upSec": up_sec,
                "downSec": down_sec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        up_sec = d.pop("upSec")

        down_sec = d.pop("downSec")

        uptime_maintenance_seconds = cls(
            up_sec=up_sec,
            down_sec=down_sec,
        )

        uptime_maintenance_seconds.additional_properties = d
        return uptime_maintenance_seconds

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
