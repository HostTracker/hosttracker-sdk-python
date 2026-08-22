from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_subscription_view import ReportSubscriptionView


T = TypeVar("T", bound="ReportSubscriptionDeleteResult")


@_attrs_define
class ReportSubscriptionDeleteResult:
    """What the filter selects, right now."""

    matched: int | Unset = UNSET
    """ How many subscriptions the filter selects. """
    sample: list[ReportSubscriptionView] | Unset = UNSET
    """ A sample of them. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matched = self.matched

        sample: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sample, Unset):
            sample = []
            for sample_item_data in self.sample:
                sample_item = sample_item_data.to_dict()
                sample.append(sample_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if matched is not UNSET:
            field_dict["matched"] = matched
        if sample is not UNSET:
            field_dict["sample"] = sample

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_subscription_view import ReportSubscriptionView

        d = dict(src_dict)
        matched = d.pop("matched", UNSET)

        _sample = d.pop("sample", UNSET)
        sample: list[ReportSubscriptionView] | Unset = UNSET
        if _sample is not UNSET:
            sample = []
            for sample_item_data in _sample:
                sample_item = ReportSubscriptionView.from_dict(sample_item_data)

                sample.append(sample_item)

        report_subscription_delete_result = cls(
            matched=matched,
            sample=sample,
        )

        report_subscription_delete_result.additional_properties = d
        return report_subscription_delete_result

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
