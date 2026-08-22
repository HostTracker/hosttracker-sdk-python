from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonitorStateCounts")


@_attrs_define
class MonitorStateCounts:
    """The four states, always all four present - a zero is information, an absent key is a question."""

    up: int
    down: int
    paused: int
    maintenance: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up = self.up

        down = self.down

        paused = self.paused

        maintenance = self.maintenance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "up": up,
                "down": down,
                "paused": paused,
                "maintenance": maintenance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        up = d.pop("up")

        down = d.pop("down")

        paused = d.pop("paused")

        maintenance = d.pop("maintenance")

        monitor_state_counts = cls(
            up=up,
            down=down,
            paused=paused,
            maintenance=maintenance,
        )

        monitor_state_counts.additional_properties = d
        return monitor_state_counts

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
