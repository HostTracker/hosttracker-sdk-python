from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceSuppress")


@_attrs_define
class MaintenanceSuppress:
    """What the maintenance window suppresses. At least one of the two must be true - a window that suppresses neither does
    nothing and is refused.

    """

    alerts: bool | Unset = UNSET
    """ Hold back alerting for the duration of the window. """
    stats: bool | Unset = UNSET
    """ Keep the window's checks out of the uptime statistics, so planned downtime does not read as an outage. """

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

        maintenance_suppress = cls(
            alerts=alerts,
            stats=stats,
        )

        return maintenance_suppress
