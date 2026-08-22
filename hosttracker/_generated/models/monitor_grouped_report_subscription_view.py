from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_monitor_ref_view import ContactsMonitorRefView
    from ..models.monitor_report_subscription_view import MonitorReportSubscriptionView


T = TypeVar("T", bound="MonitorGroupedReportSubscriptionView")


@_attrs_define
class MonitorGroupedReportSubscriptionView:
    """One element of the BY-MONITOR grouping of the account-wide report list (`GET /report/by-monitor`): one monitor and
    every contact subscribed to its reports, so the monitor identity is carried once per monitor.

    """

    monitor: ContactsMonitorRefView | Unset = UNSET
    """ The minimal identifying projection of a monitor, as embedded in relation reads. """
    subscriptions: list[MonitorReportSubscriptionView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_monitor_ref_view import ContactsMonitorRefView
        from ..models.monitor_report_subscription_view import MonitorReportSubscriptionView

        d = dict(src_dict)
        _monitor = d.pop("monitor", UNSET)
        monitor: ContactsMonitorRefView | Unset
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = ContactsMonitorRefView.from_dict(_monitor)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[MonitorReportSubscriptionView] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = MonitorReportSubscriptionView.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        monitor_grouped_report_subscription_view = cls(
            monitor=monitor,
            subscriptions=subscriptions,
        )

        monitor_grouped_report_subscription_view.additional_properties = d
        return monitor_grouped_report_subscription_view

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
