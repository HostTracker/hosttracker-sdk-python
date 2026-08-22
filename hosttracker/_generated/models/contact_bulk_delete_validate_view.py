from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_selection_sample import ContactSelectionSample


T = TypeVar("T", bound="ContactBulkDeleteValidateView")


@_attrs_define
class ContactBulkDeleteValidateView:
    """What a bulk-delete verification answers: what the filter selects, right now. `matched` is the family's word for this
    count - one concept, one name across the surface.

    """

    matched: int
    """ How many contacts the filter selects. """
    truncated: bool
    """ True when the selection is larger than one job may carry (`max`). An honest cap signal: a caller that is not
    told would believe one submission deletes everything the filter matched. """
    max_: int
    """ The largest selection one submission accepts. """
    sample: list[ContactSelectionSample] | Unset = UNSET
    """ The first few of them, so a human can recognise the selection before acting on it. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        truncated = self.truncated

        max_ = self.max_

        sample: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sample, Unset):
            sample = []
            for sample_item_data in self.sample:
                sample_item = sample_item_data.to_dict()
                sample.append(sample_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matched": matched,
                "truncated": truncated,
                "max": max_,
            }
        )
        if sample is not UNSET:
            field_dict["sample"] = sample

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_selection_sample import ContactSelectionSample

        d = dict(src_dict)
        matched = d.pop("matched")

        truncated = d.pop("truncated")

        max_ = d.pop("max")

        _sample = d.pop("sample", UNSET)
        sample: list[ContactSelectionSample] | Unset = UNSET
        if _sample is not UNSET:
            sample = []
            for sample_item_data in _sample:
                sample_item = ContactSelectionSample.from_dict(sample_item_data)

                sample.append(sample_item)

        contact_bulk_delete_validate_view = cls(
            matched=matched,
            truncated=truncated,
            max_=max_,
            sample=sample,
        )

        contact_bulk_delete_validate_view.additional_properties = d
        return contact_bulk_delete_validate_view

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
