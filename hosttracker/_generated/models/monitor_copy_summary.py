from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonitorCopySummary")


@_attrs_define
class MonitorCopySummary:
    """How much the copy reproduced."""

    created: int
    """ How many monitors were created and are running. """
    created_disabled: int
    """ How many were created disabled because the package had no room and the request asked for onOverlimit
    disable. Zero under the default, which refuses instead. """
    alert_subscriptions: int
    """ Alert-subscription rows written across all copies. """
    report_subscriptions: int
    """ Report-subscription rows written across all copies. """
    maintenance_windows: int
    """ How many maintenance windows the copies were added to. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_disabled = self.created_disabled

        alert_subscriptions = self.alert_subscriptions

        report_subscriptions = self.report_subscriptions

        maintenance_windows = self.maintenance_windows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "createdDisabled": created_disabled,
                "alertSubscriptions": alert_subscriptions,
                "reportSubscriptions": report_subscriptions,
                "maintenanceWindows": maintenance_windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        created_disabled = d.pop("createdDisabled")

        alert_subscriptions = d.pop("alertSubscriptions")

        report_subscriptions = d.pop("reportSubscriptions")

        maintenance_windows = d.pop("maintenanceWindows")

        monitor_copy_summary = cls(
            created=created,
            created_disabled=created_disabled,
            alert_subscriptions=alert_subscriptions,
            report_subscriptions=report_subscriptions,
            maintenance_windows=maintenance_windows,
        )

        monitor_copy_summary.additional_properties = d
        return monitor_copy_summary

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
