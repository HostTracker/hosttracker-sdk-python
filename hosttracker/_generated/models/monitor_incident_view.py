from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_incident_view_state import MonitorIncidentViewState, check_monitor_incident_view_state
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorIncidentView")


@_attrs_define
class MonitorIncidentView:
    """The monitor's last up/down transition."""

    event_number: int
    """ The event number the transition carries - the id an incident/result read joins on. """
    at: int
    """ Unix seconds. """
    duration_sec: int
    under_maintenance: bool
    """ True when the transition happened inside a maintenance window. """
    state: MonitorIncidentViewState | Unset = UNSET
    """ The state the monitor moved INTO at this transition. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_number = self.event_number

        at = self.at

        duration_sec = self.duration_sec

        under_maintenance = self.under_maintenance

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventNumber": event_number,
                "at": at,
                "durationSec": duration_sec,
                "underMaintenance": under_maintenance,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_number = d.pop("eventNumber")

        at = d.pop("at")

        duration_sec = d.pop("durationSec")

        under_maintenance = d.pop("underMaintenance")

        _state = d.pop("state", UNSET)
        state: MonitorIncidentViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_monitor_incident_view_state(_state)

        monitor_incident_view = cls(
            event_number=event_number,
            at=at,
            duration_sec=duration_sec,
            under_maintenance=under_maintenance,
            state=state,
        )

        monitor_incident_view.additional_properties = d
        return monitor_incident_view

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
