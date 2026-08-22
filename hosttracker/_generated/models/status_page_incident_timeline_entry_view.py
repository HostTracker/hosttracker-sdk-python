from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_incident_timeline_entry_view_state import (
    StatusPageIncidentTimelineEntryViewState,
    check_status_page_incident_timeline_entry_view_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageIncidentTimelineEntryView")


@_attrs_define
class StatusPageIncidentTimelineEntryView:
    """One timeline entry."""

    at: int
    """ Unix seconds. """
    state: StatusPageIncidentTimelineEntryViewState | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at = self.at

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "at": at,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at = d.pop("at")

        _state = d.pop("state", UNSET)
        state: StatusPageIncidentTimelineEntryViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_status_page_incident_timeline_entry_view_state(_state)

        message = d.pop("message", UNSET)

        status_page_incident_timeline_entry_view = cls(
            at=at,
            state=state,
            message=message,
        )

        status_page_incident_timeline_entry_view.additional_properties = d
        return status_page_incident_timeline_entry_view

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
