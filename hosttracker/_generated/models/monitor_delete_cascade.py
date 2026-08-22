from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonitorDeleteCascade")


@_attrs_define
class MonitorDeleteCascade:
    """What went with the monitor."""

    alert_subscriptions: int
    report_subscriptions: int
    maintenance_subscriptions: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_subscriptions = self.alert_subscriptions

        report_subscriptions = self.report_subscriptions

        maintenance_subscriptions = self.maintenance_subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alertSubscriptions": alert_subscriptions,
                "reportSubscriptions": report_subscriptions,
                "maintenanceSubscriptions": maintenance_subscriptions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_subscriptions = d.pop("alertSubscriptions")

        report_subscriptions = d.pop("reportSubscriptions")

        maintenance_subscriptions = d.pop("maintenanceSubscriptions")

        monitor_delete_cascade = cls(
            alert_subscriptions=alert_subscriptions,
            report_subscriptions=report_subscriptions,
            maintenance_subscriptions=maintenance_subscriptions,
        )

        monitor_delete_cascade.additional_properties = d
        return monitor_delete_cascade

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
