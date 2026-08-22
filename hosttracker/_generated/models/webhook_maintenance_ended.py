from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookMaintenanceEnded")


@_attrs_define
class WebhookMaintenanceEnded:
    """A maintenance window stopped covering its monitors, by expiry or by an early cancel."""

    maintenance_id: UUID
    """ The window's id - what GET /maintenance/{id} takes. """
    name: str
    """ The window's name. """
    from_: int
    """ The window's start. Unix seconds. """
    to: int
    """ The window's scheduled end - which an early cancel does not reach. Unix seconds. """
    monitor_ids: list[UUID]
    """ The window's monitors, filtered to the ones this webhook's scope covers. """
    ended_early: bool
    """ True when the window was cancelled while active; false when it reached its scheduled end. """
    ended_at: int
    """ When it actually ended. Unix seconds. """

    def to_dict(self) -> dict[str, Any]:
        maintenance_id = str(self.maintenance_id)

        name = self.name

        from_ = self.from_

        to = self.to

        monitor_ids = []
        for monitor_ids_item_data in self.monitor_ids:
            monitor_ids_item = str(monitor_ids_item_data)
            monitor_ids.append(monitor_ids_item)

        ended_early = self.ended_early

        ended_at = self.ended_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "maintenanceId": maintenance_id,
                "name": name,
                "from": from_,
                "to": to,
                "monitorIds": monitor_ids,
                "endedEarly": ended_early,
                "endedAt": ended_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        maintenance_id = UUID(d.pop("maintenanceId"))

        name = d.pop("name")

        from_ = d.pop("from")

        to = d.pop("to")

        monitor_ids = []
        _monitor_ids = d.pop("monitorIds")
        for monitor_ids_item_data in _monitor_ids:
            monitor_ids_item = UUID(monitor_ids_item_data)

            monitor_ids.append(monitor_ids_item)

        ended_early = d.pop("endedEarly")

        ended_at = d.pop("endedAt")

        webhook_maintenance_ended = cls(
            maintenance_id=maintenance_id,
            name=name,
            from_=from_,
            to=to,
            monitor_ids=monitor_ids,
            ended_early=ended_early,
            ended_at=ended_at,
        )

        return webhook_maintenance_ended
