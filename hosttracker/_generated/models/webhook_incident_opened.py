from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookIncidentOpened")


@_attrs_define
class WebhookIncidentOpened:
    """An episode opened in the engine's state model - every episode, including maintenance-flagged ones."""

    incident_id: str
    """ The episode's id - paste it straight into GET /monitor/incident/{id}. """
    monitor_id: UUID
    """ The monitor the episode is about. """
    start: int
    """ When the episode began. Unix seconds. """
    cause: str
    """ The failure that opened the episode, as the engine described it. """
    under_maintenance: bool
    """ True when the episode began inside a maintenance window - it is still an episode, but no alert was sent. """

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        monitor_id = str(self.monitor_id)

        start = self.start

        cause = self.cause

        under_maintenance = self.under_maintenance

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incidentId": incident_id,
                "monitorId": monitor_id,
                "start": start,
                "cause": cause,
                "underMaintenance": under_maintenance,
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

        webhook_incident_opened = cls(
            incident_id=incident_id,
            monitor_id=monitor_id,
            start=start,
            cause=cause,
            under_maintenance=under_maintenance,
        )

        return webhook_incident_opened
