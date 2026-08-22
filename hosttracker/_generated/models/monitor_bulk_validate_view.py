from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_item_verdict_view import MonitorItemVerdictView


T = TypeVar("T", bound="MonitorBulkValidateView")


@_attrs_define
class MonitorBulkValidateView:
    """`bulkValidateMonitor`'s answer - the whole-batch tallies plus one verdict per item. The tallies are counts of the
    SAME `items[]` below, not a second source of truth: a client renders "N of M fit; K will be created disabled"
    without folding 500 rows itself.

    """

    valid: int
    """ How many items would be created (including any that would land disabled). """
    invalid: int
    """ How many would be refused. """
    would_disable: int
    """ How many would be created DISABLED under the submitted `onOverlimit` mode. Always 0 unless that mode is
    `disable`. """
    items: list[MonitorItemVerdictView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        invalid = self.invalid

        would_disable = self.would_disable

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
                "invalid": invalid,
                "wouldDisable": would_disable,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_item_verdict_view import MonitorItemVerdictView

        d = dict(src_dict)
        valid = d.pop("valid")

        invalid = d.pop("invalid")

        would_disable = d.pop("wouldDisable")

        _items = d.pop("items", UNSET)
        items: list[MonitorItemVerdictView] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = MonitorItemVerdictView.from_dict(items_item_data)

                items.append(items_item)

        monitor_bulk_validate_view = cls(
            valid=valid,
            invalid=invalid,
            would_disable=would_disable,
            items=items,
        )

        monitor_bulk_validate_view.additional_properties = d
        return monitor_bulk_validate_view

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
