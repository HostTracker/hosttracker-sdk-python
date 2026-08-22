from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceMonitorSuppress")


@_attrs_define
class MaintenanceMonitorSuppress:
    """What the window suppresses for THIS monitor. At least one of the two must be true - a monitor the window suppresses
    nothing for is a monitor it does not cover.

    """

    alerts: bool | Unset = UNSET
    """ Hold back alerting for this monitor for the duration of the window. """
    stats: bool | Unset = UNSET
    """ Keep this monitor's checks inside the window out of the uptime statistics. """

    def to_dict(self) -> dict[str, Any]:
        alerts = self.alerts

        stats = self.stats

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alerts = d.pop("alerts", UNSET)

        stats = d.pop("stats", UNSET)

        maintenance_monitor_suppress = cls(
            alerts=alerts,
            stats=stats,
        )

        return maintenance_monitor_suppress
