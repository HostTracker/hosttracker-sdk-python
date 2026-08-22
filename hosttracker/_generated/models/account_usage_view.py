from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_usage_item_view import AccountUsageItemView


T = TypeVar("T", bound="AccountUsageView")


@_attrs_define
class AccountUsageView:
    monitor: AccountUsageItemView | Unset = UNSET
    """ One usage dimension: what the account has, and what its package allows. """
    contact: AccountUsageItemView | Unset = UNSET
    """ One usage dimension: what the account has, and what its package allows. """
    report: AccountUsageItemView | Unset = UNSET
    """ One usage dimension: what the account has, and what its package allows. """
    maintenance: AccountUsageItemView | Unset = UNSET
    """ One usage dimension: what the account has, and what its package allows. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        maintenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if contact is not UNSET:
            field_dict["contact"] = contact
        if report is not UNSET:
            field_dict["report"] = report
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_usage_item_view import AccountUsageItemView

        d = dict(src_dict)
        _monitor = d.pop("monitor", UNSET)
        monitor: AccountUsageItemView | Unset
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = AccountUsageItemView.from_dict(_monitor)

        _contact = d.pop("contact", UNSET)
        contact: AccountUsageItemView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = AccountUsageItemView.from_dict(_contact)

        _report = d.pop("report", UNSET)
        report: AccountUsageItemView | Unset
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = AccountUsageItemView.from_dict(_report)

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: AccountUsageItemView | Unset
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = AccountUsageItemView.from_dict(_maintenance)

        account_usage_view = cls(
            monitor=monitor,
            contact=contact,
            report=report,
            maintenance=maintenance,
        )

        account_usage_view.additional_properties = d
        return account_usage_view

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
