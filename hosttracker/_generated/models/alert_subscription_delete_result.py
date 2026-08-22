from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_subscription_view import AlertSubscriptionView


T = TypeVar("T", bound="AlertSubscriptionDeleteResult")


@_attrs_define
class AlertSubscriptionDeleteResult:
    """What the filter selects, right now."""

    matched: int | Unset = UNSET
    """ How many subscriptions the filter selects. """
    sample: list[AlertSubscriptionView] | Unset = UNSET
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
        from ..models.alert_subscription_view import AlertSubscriptionView

        d = dict(src_dict)
        matched = d.pop("matched", UNSET)

        _sample = d.pop("sample", UNSET)
        sample: list[AlertSubscriptionView] | Unset = UNSET
        if _sample is not UNSET:
            sample = []
            for sample_item_data in _sample:
                sample_item = AlertSubscriptionView.from_dict(sample_item_data)

                sample.append(sample_item)

        alert_subscription_delete_result = cls(
            matched=matched,
            sample=sample,
        )

        alert_subscription_delete_result.additional_properties = d
        return alert_subscription_delete_result

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
