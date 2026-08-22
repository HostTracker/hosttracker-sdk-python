from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MaintenanceDeleteCascade")


@_attrs_define
class MaintenanceDeleteCascade:
    """What went with the window."""

    monitor_subscriptions: int
    """ The monitor attachments this window covered - `MaintenanceSubscription` rows, deleted with the window. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_subscriptions = self.monitor_subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitorSubscriptions": monitor_subscriptions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor_subscriptions = d.pop("monitorSubscriptions")

        maintenance_delete_cascade = cls(
            monitor_subscriptions=monitor_subscriptions,
        )

        maintenance_delete_cascade.additional_properties = d
        return maintenance_delete_cascade

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
