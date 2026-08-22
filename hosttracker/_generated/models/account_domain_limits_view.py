from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountDomainLimitsView")


@_attrs_define
class AccountDomainLimitsView:
    """One domain's bounds. Same member names as the account-level pair, so a client that learns `maxBulkItems` once knows
    it everywhere it appears.

    """

    max_bulk_items: int
    """ Items one bulk CREATE may carry - the caller's own package count, clamped to the envelope ceiling. """
    max_bulk_selection: int
    """ Rows one bulk UPDATE or DELETE may target. Flat per domain and deliberately NOT the package number: deleting
    is how an account gets back under its cap. """
    max_total_rows: int | None | Unset = UNSET
    """ **The total-row ceiling** - how many rows the account may hold in this domain in ALL, running and dormant
    together (`packageCap + 5000`). Null when the domain is uncapped, which is the common shape for contacts.
    Published because it was previously discoverable ONLY by being refused: the package cap counts ACTIVE rows, so
    an account well under it could still be refused a create by a ceiling it had no way to read. "A limit that lives
    only inside a refusal is a limit nobody plans around" - and unlike the package cap, `onOverlimit:"disable"`
    cannot rescue a breach of this one, because a dormant row counts against it exactly like a running one. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_bulk_items = self.max_bulk_items

        max_bulk_selection = self.max_bulk_selection

        max_total_rows: int | None | Unset
        if isinstance(self.max_total_rows, Unset):
            max_total_rows = UNSET
        else:
            max_total_rows = self.max_total_rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maxBulkItems": max_bulk_items,
                "maxBulkSelection": max_bulk_selection,
            }
        )
        if max_total_rows is not UNSET:
            field_dict["maxTotalRows"] = max_total_rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_bulk_items = d.pop("maxBulkItems")

        max_bulk_selection = d.pop("maxBulkSelection")

        def _parse_max_total_rows(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_total_rows = _parse_max_total_rows(d.pop("maxTotalRows", UNSET))

        account_domain_limits_view = cls(
            max_bulk_items=max_bulk_items,
            max_bulk_selection=max_bulk_selection,
            max_total_rows=max_total_rows,
        )

        account_domain_limits_view.additional_properties = d
        return account_domain_limits_view

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
