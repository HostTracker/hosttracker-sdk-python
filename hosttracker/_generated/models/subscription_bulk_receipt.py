from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionBulkReceipt")


@_attrs_define
class SubscriptionBulkReceipt:
    """**What a subscription bulk write changed**. `unchanged` is the honest half: a create that was already wired and a
    delete of a pair that was not wired are both no-ops, and reporting them as work done would make a convergent client
    believe it had changed something.

    """

    created: int
    """ Subscription rows written. """
    deleted: int
    """ Subscription rows removed. """
    unchanged: int
    """ Requested rows that were already in the state the request asked for. """
    pairs: int
    """ How many distinct monitor-and-contact pairs the request touched, after the wildcards expanded. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        deleted = self.deleted

        unchanged = self.unchanged

        pairs = self.pairs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "deleted": deleted,
                "unchanged": unchanged,
                "pairs": pairs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        deleted = d.pop("deleted")

        unchanged = d.pop("unchanged")

        pairs = d.pop("pairs")

        subscription_bulk_receipt = cls(
            created=created,
            deleted=deleted,
            unchanged=unchanged,
            pairs=pairs,
        )

        subscription_bulk_receipt.additional_properties = d
        return subscription_bulk_receipt

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
