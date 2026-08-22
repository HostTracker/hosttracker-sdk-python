from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UptimeIncidentCounts")


@_attrs_define
class UptimeIncidentCounts:
    opened: int
    """ Episodes that OPENED in the bucket. """
    restored: int
    """ Episodes that CLOSED (the monitor came back) in the bucket. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        opened = self.opened

        restored = self.restored

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "opened": opened,
                "restored": restored,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        opened = d.pop("opened")

        restored = d.pop("restored")

        uptime_incident_counts = cls(
            opened=opened,
            restored=restored,
        )

        uptime_incident_counts.additional_properties = d
        return uptime_incident_counts

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
