from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_domain_limits_view import AccountDomainLimitsView


T = TypeVar("T", bound="AccountLimitsView")


@_attrs_define
class AccountLimitsView:
    max_bulk_items: int
    """ Items one bulk CREATE may carry - **the caller's own cap, not a constant**: a batch larger than the
    account's package allows was always going to end as N creates and the rest refused, so the bound is published
    rather than discovered from a 422. """
    max_bulk_selection: int
    """ Monitors one bulk UPDATE or DELETE may target - a FIXED 2000, deliberately not the package number: deleting
    is how an account gets back under its cap, so tying the two would tighten exactly when a caller needs it
    loosest. Published beside `maxBulkItems` because the two used to be one number and a client that assumed they
    still are would size its delete batches by its package. """
    max_limit: int
    """ The largest `limit` any collection read accepts. """
    default_limit: int
    """ The default `limit` when a collection read sends none. """
    max_inline_contacts: int
    """ Inline `contacts[]` a single monitor create may declare. """
    intervals: list[int] | Unset = UNSET
    alert_delays: list[int] | Unset = UNSET
    """ The alert-delay ladder in **minutes**, sorted - never the stored index. """
    monitor: AccountDomainLimitsView | Unset = UNSET
    """ One domain's bounds. Same member names as the account-level pair, so a client that learns `maxBulkItems`
    once knows it everywhere it appears. """
    contact: AccountDomainLimitsView | Unset = UNSET
    """ One domain's bounds. Same member names as the account-level pair, so a client that learns `maxBulkItems`
    once knows it everywhere it appears. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_bulk_items = self.max_bulk_items

        max_bulk_selection = self.max_bulk_selection

        max_limit = self.max_limit

        default_limit = self.default_limit

        max_inline_contacts = self.max_inline_contacts

        intervals: list[int] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = self.intervals

        alert_delays: list[int] | Unset = UNSET
        if not isinstance(self.alert_delays, Unset):
            alert_delays = self.alert_delays

        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxBulkItems": max_bulk_items,
                "maxBulkSelection": max_bulk_selection,
                "maxLimit": max_limit,
                "defaultLimit": default_limit,
                "maxInlineContacts": max_inline_contacts,
            }
        )
        if intervals is not UNSET:
            field_dict["intervals"] = intervals
        if alert_delays is not UNSET:
            field_dict["alertDelays"] = alert_delays
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if contact is not UNSET:
            field_dict["contact"] = contact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_domain_limits_view import AccountDomainLimitsView

        d = dict(src_dict)
        max_bulk_items = d.pop("maxBulkItems")

        max_bulk_selection = d.pop("maxBulkSelection")

        max_limit = d.pop("maxLimit")

        default_limit = d.pop("defaultLimit")

        max_inline_contacts = d.pop("maxInlineContacts")

        intervals = cast(list[int], d.pop("intervals", UNSET))

        alert_delays = cast(list[int], d.pop("alertDelays", UNSET))

        _monitor = d.pop("monitor", UNSET)
        monitor: AccountDomainLimitsView | Unset
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = AccountDomainLimitsView.from_dict(_monitor)

        _contact = d.pop("contact", UNSET)
        contact: AccountDomainLimitsView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = AccountDomainLimitsView.from_dict(_contact)

        account_limits_view = cls(
            max_bulk_items=max_bulk_items,
            max_bulk_selection=max_bulk_selection,
            max_limit=max_limit,
            default_limit=default_limit,
            max_inline_contacts=max_inline_contacts,
            intervals=intervals,
            alert_delays=alert_delays,
            monitor=monitor,
            contact=contact,
        )

        account_limits_view.additional_properties = d
        return account_limits_view

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
