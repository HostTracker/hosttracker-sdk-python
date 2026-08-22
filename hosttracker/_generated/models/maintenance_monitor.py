from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.maintenance_monitor_suppress import MaintenanceMonitorSuppress


T = TypeVar("T", bound="MaintenanceMonitor")


@_attrs_define
class MaintenanceMonitor:
    """One monitor the window covers, and what it holds back for that monitor."""

    monitor_id: UUID
    """ A monitor this window covers. It must belong to the account; an id that does not is refused, never skipped.
    """
    suppress: MaintenanceMonitorSuppress
    """ What the window suppresses for THIS monitor. At least one of the two must be true - a monitor the window
    suppresses nothing for is a monitor it does not cover. """

    def to_dict(self) -> dict[str, Any]:
        monitor_id = str(self.monitor_id)

        suppress = self.suppress.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitorId": monitor_id,
                "suppress": suppress,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maintenance_monitor_suppress import MaintenanceMonitorSuppress

        d = dict(src_dict)
        monitor_id = UUID(d.pop("monitorId"))

        suppress = MaintenanceMonitorSuppress.from_dict(d.pop("suppress"))

        maintenance_monitor = cls(
            monitor_id=monitor_id,
            suppress=suppress,
        )

        return maintenance_monitor
