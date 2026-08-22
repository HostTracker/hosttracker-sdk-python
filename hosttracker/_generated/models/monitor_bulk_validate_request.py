from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_bulk_validate_request_on_duplicate import (
    MonitorBulkValidateRequestOnDuplicate,
    check_monitor_bulk_validate_request_on_duplicate,
)
from ..models.monitor_bulk_validate_request_on_overlimit import (
    MonitorBulkValidateRequestOnOverlimit,
    check_monitor_bulk_validate_request_on_overlimit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_bulk_item import MonitorBulkItem


T = TypeVar("T", bound="MonitorBulkValidateRequest")


@_attrs_define
class MonitorBulkValidateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    items: list[MonitorBulkItem]
    """ The batch's entries. 1 to 500. """
    defaults: MonitorBulkItem | Unset = UNSET
    """ One monitor to create, in the same shape POST /monitor takes. A member this entry omits is taken from
    `defaults`; the two are merged before the entry is validated, so an entry may look incomplete on its own and
    still be valid. """
    on_duplicate: MonitorBulkValidateRequestOnDuplicate | Unset = UNSET
    """ What to do with an item whose address already exists on the account: refuse the item, report it as skipped,
    or create the duplicate anyway. """
    on_overlimit: MonitorBulkValidateRequestOnOverlimit | Unset = UNSET
    """ What to do with an item the account's package will not fit. "fail" (the default) refuses that item and
    carries on; "disable" creates it disabled so nothing is lost; "stop" halts the run and reports the remainder as
    cancelled. Packages that bill overages as extras never refuse, so this has no effect on them. """

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate

        on_overlimit: str | Unset = UNSET
        if not isinstance(self.on_overlimit, Unset):
            on_overlimit = self.on_overlimit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
            }
        )
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if on_duplicate is not UNSET:
            field_dict["onDuplicate"] = on_duplicate
        if on_overlimit is not UNSET:
            field_dict["onOverlimit"] = on_overlimit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_bulk_item import MonitorBulkItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = MonitorBulkItem.from_dict(items_item_data)

            items.append(items_item)

        _defaults = d.pop("defaults", UNSET)
        defaults: MonitorBulkItem | Unset
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = MonitorBulkItem.from_dict(_defaults)

        _on_duplicate = d.pop("onDuplicate", UNSET)
        on_duplicate: MonitorBulkValidateRequestOnDuplicate | Unset
        if isinstance(_on_duplicate, Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = check_monitor_bulk_validate_request_on_duplicate(_on_duplicate)

        _on_overlimit = d.pop("onOverlimit", UNSET)
        on_overlimit: MonitorBulkValidateRequestOnOverlimit | Unset
        if isinstance(_on_overlimit, Unset):
            on_overlimit = UNSET
        else:
            on_overlimit = check_monitor_bulk_validate_request_on_overlimit(_on_overlimit)

        monitor_bulk_validate_request = cls(
            items=items,
            defaults=defaults,
            on_duplicate=on_duplicate,
            on_overlimit=on_overlimit,
        )

        return monitor_bulk_validate_request
