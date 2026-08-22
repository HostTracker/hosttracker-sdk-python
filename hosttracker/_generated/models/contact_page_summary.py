from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_type_count import ContactTypeCount


T = TypeVar("T", bound="ContactPageSummary")


@_attrs_define
class ContactPageSummary:
    """Account-wide contact counts, returned in the envelope when `expand=summary` asks for them. Counts the whole account,
    not the page.

    """

    total: int | Unset = UNSET
    """ How many contacts the account holds. """
    confirmed: int | Unset = UNSET
    """ How many of them have confirmed their address. """
    unconfirmed: int | Unset = UNSET
    """ How many have not - alerts to these are not delivered. """
    by_type: list[ContactTypeCount] | Unset = UNSET
    """ The same total, split by contact type. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        confirmed = self.confirmed

        unconfirmed = self.unconfirmed

        by_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = []
            for by_type_item_data in self.by_type:
                by_type_item = by_type_item_data.to_dict()
                by_type.append(by_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if unconfirmed is not UNSET:
            field_dict["unconfirmed"] = unconfirmed
        if by_type is not UNSET:
            field_dict["byType"] = by_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_type_count import ContactTypeCount

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        confirmed = d.pop("confirmed", UNSET)

        unconfirmed = d.pop("unconfirmed", UNSET)

        _by_type = d.pop("byType", UNSET)
        by_type: list[ContactTypeCount] | Unset = UNSET
        if _by_type is not UNSET:
            by_type = []
            for by_type_item_data in _by_type:
                by_type_item = ContactTypeCount.from_dict(by_type_item_data)

                by_type.append(by_type_item)

        contact_page_summary = cls(
            total=total,
            confirmed=confirmed,
            unconfirmed=unconfirmed,
            by_type=by_type,
        )

        contact_page_summary.additional_properties = d
        return contact_page_summary

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
