from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertSubscriptionSummary")


@_attrs_define
class AlertSubscriptionSummary:
    """How much the write touched."""

    monitors: int
    """ Monitors touched by the write. """
    contacts: int
    """ Contacts touched by the write. """
    subscriptions: int
    """ Subscriptions in the resulting set. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitors = self.monitors

        contacts = self.contacts

        subscriptions = self.subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitors": monitors,
                "contacts": contacts,
                "subscriptions": subscriptions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitors = d.pop("monitors")

        contacts = d.pop("contacts")

        subscriptions = d.pop("subscriptions")

        alert_subscription_summary = cls(
            monitors=monitors,
            contacts=contacts,
            subscriptions=subscriptions,
        )

        alert_subscription_summary.additional_properties = d
        return alert_subscription_summary

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
