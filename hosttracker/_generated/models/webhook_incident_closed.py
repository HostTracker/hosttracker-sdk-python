from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookIncidentClosed")


@_attrs_define
class WebhookIncidentClosed:
    """The episode resolved, with how long it lasted."""

    incident_id: str
    """ The episode's id - the SAME token incident.opened carried. """
    monitor_id: UUID
    """ The monitor the episode is about. """
    start: int
    """ When the episode began. Unix seconds. """
    cause: str
    """ The failure that opened the episode, as the engine described it. """
    under_maintenance: bool
    """ True when the episode began inside a maintenance window. """
    end: int
    """ When the episode resolved. Unix seconds. """
    duration_sec: int
    """ How long the episode lasted, in seconds. """
    check_count: int
    """ Failed checks observed during the episode; 0 when the engine could not count them. """

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        monitor_id = str(self.monitor_id)

        start = self.start

        cause = self.cause

        under_maintenance = self.under_maintenance

        end = self.end

        duration_sec = self.duration_sec

        check_count = self.check_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incidentId": incident_id,
                "monitorId": monitor_id,
                "start": start,
                "cause": cause,
                "underMaintenance": under_maintenance,
                "end": end,
                "durationSec": duration_sec,
                "checkCount": check_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_id = d.pop("incidentId")

        monitor_id = UUID(d.pop("monitorId"))

        start = d.pop("start")

        cause = d.pop("cause")

        under_maintenance = d.pop("underMaintenance")

        end = d.pop("end")

        duration_sec = d.pop("durationSec")

        check_count = d.pop("checkCount")

        webhook_incident_closed = cls(
            incident_id=incident_id,
            monitor_id=monitor_id,
            start=start,
            cause=cause,
            under_maintenance=under_maintenance,
            end=end,
            duration_sec=duration_sec,
            check_count=check_count,
        )

        return webhook_incident_closed
