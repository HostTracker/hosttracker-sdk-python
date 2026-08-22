from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_monitor_ref_view import ContactsMonitorRefView


T = TypeVar("T", bound="ContactSubscriptionSummaryView")


@_attrs_define
class ContactSubscriptionSummaryView:
    """`expand=subscription`'s per-contact block: how many monitors this contact is alerted for, plus a bounded identifying
    sample. Never bare ids.

    """

    alerts: int
    reports: int
    monitors: list[ContactsMonitorRefView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alerts = self.alerts

        reports = self.reports

        monitors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monitors, Unset):
            monitors = []
            for monitors_item_data in self.monitors:
                monitors_item = monitors_item_data.to_dict()
                monitors.append(monitors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alerts": alerts,
                "reports": reports,
            }
        )
        if monitors is not UNSET:
            field_dict["monitors"] = monitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_monitor_ref_view import ContactsMonitorRefView

        d = dict(src_dict)
        alerts = d.pop("alerts")

        reports = d.pop("reports")

        _monitors = d.pop("monitors", UNSET)
        monitors: list[ContactsMonitorRefView] | Unset = UNSET
        if _monitors is not UNSET:
            monitors = []
            for monitors_item_data in _monitors:
                monitors_item = ContactsMonitorRefView.from_dict(monitors_item_data)

                monitors.append(monitors_item)

        contact_subscription_summary_view = cls(
            alerts=alerts,
            reports=reports,
            monitors=monitors,
        )

        contact_subscription_summary_view.additional_properties = d
        return contact_subscription_summary_view

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
