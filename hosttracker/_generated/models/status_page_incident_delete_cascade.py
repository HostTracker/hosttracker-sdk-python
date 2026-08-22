from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusPageIncidentDeleteCascade")


@_attrs_define
class StatusPageIncidentDeleteCascade:
    """What went with the incident."""

    timeline: int
    """ The entries of its append-only timeline, including the first one the declaration wrote. Subscribers were
    notified of these and are not told they are gone - a delete sends no notice, the same deliberate choice the
    dashboard makes. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timeline = self.timeline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeline": timeline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeline = d.pop("timeline")

        status_page_incident_delete_cascade = cls(
            timeline=timeline,
        )

        status_page_incident_delete_cascade.additional_properties = d
        return status_page_incident_delete_cascade

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
