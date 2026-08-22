from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.alert_subscription_summary import AlertSubscriptionSummary
    from ..models.alert_subscription_view import AlertSubscriptionView


T = TypeVar("T", bound="AlertSubscriptionWriteResult")


@_attrs_define
class AlertSubscriptionWriteResult:
    """What the write changed, and the subscriptions that resulted."""

    summary: AlertSubscriptionSummary
    """ How much the write touched. """
    data: list[AlertSubscriptionView]
    """ The resulting alert subscriptions. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_subscription_summary import AlertSubscriptionSummary
        from ..models.alert_subscription_view import AlertSubscriptionView

        d = dict(src_dict)
        summary = AlertSubscriptionSummary.from_dict(d.pop("summary"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = AlertSubscriptionView.from_dict(data_item_data)

            data.append(data_item)

        alert_subscription_write_result = cls(
            summary=summary,
            data=data,
        )

        alert_subscription_write_result.additional_properties = d
        return alert_subscription_write_result

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
