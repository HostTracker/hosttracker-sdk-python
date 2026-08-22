from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_bulk_create_request_on_duplicate import (
    MonitorBulkCreateRequestOnDuplicate,
    check_monitor_bulk_create_request_on_duplicate,
)
from ..models.monitor_bulk_create_request_on_error import (
    MonitorBulkCreateRequestOnError,
    check_monitor_bulk_create_request_on_error,
)
from ..models.monitor_bulk_create_request_on_overlimit import (
    MonitorBulkCreateRequestOnOverlimit,
    check_monitor_bulk_create_request_on_overlimit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_callback import JobCallback
    from ..models.monitor_bulk_item import MonitorBulkItem


T = TypeVar("T", bound="MonitorBulkCreateRequest")


@_attrs_define
class MonitorBulkCreateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    items: list[MonitorBulkItem]
    """ The batch's entries. 1 to 500. """
    callback: JobCallback | Unset = UNSET
    """ A webhook to call when the job finishes, carrying the terminal job document and its first page of results.
    Send null for none. """
    continue_on_error: bool | Unset = UNSET
    """ The older spelling of `onError`, still accepted: true means "continue", false means "stop". Sending both
    with different meanings is refused rather than resolved for you. """
    defaults: MonitorBulkItem | Unset = UNSET
    """ One monitor to create, in the same shape POST /monitor takes. A member this entry omits is taken from
    `defaults`; the two are merged before the entry is validated, so an entry may look incomplete on its own and
    still be valid. """
    on_duplicate: MonitorBulkCreateRequestOnDuplicate | Unset = UNSET
    """ What to do with an item whose address already exists on the account: refuse the item, report it as skipped,
    or create the duplicate anyway. """
    on_error: MonitorBulkCreateRequestOnError | Unset = UNSET
    """ Whether a failed item stops the run. "continue" (the default) attempts every item and reports each outcome
    separately; "stop" halts at the first refusal and reports every item that never ran as cancelled - which is what
    you want when the batch is one logical change. """
    on_overlimit: MonitorBulkCreateRequestOnOverlimit | Unset = UNSET
    """ What to do with an item the account's package will not fit. "fail" (the default) refuses that item and
    carries on; "disable" creates it disabled so nothing is lost; "stop" halts the run and reports the remainder as
    cancelled. Packages that bill overages as extras never refuse, so this has no effect on them. """

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        continue_on_error = self.continue_on_error

        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        on_duplicate: str | Unset = UNSET
        if not isinstance(self.on_duplicate, Unset):
            on_duplicate = self.on_duplicate

        on_error: str | Unset = UNSET
        if not isinstance(self.on_error, Unset):
            on_error = self.on_error

        on_overlimit: str | Unset = UNSET
        if not isinstance(self.on_overlimit, Unset):
            on_overlimit = self.on_overlimit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
            }
        )
        if callback is not UNSET:
            field_dict["callback"] = callback
        if continue_on_error is not UNSET:
            field_dict["continueOnError"] = continue_on_error
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if on_duplicate is not UNSET:
            field_dict["onDuplicate"] = on_duplicate
        if on_error is not UNSET:
            field_dict["onError"] = on_error
        if on_overlimit is not UNSET:
            field_dict["onOverlimit"] = on_overlimit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_callback import JobCallback
        from ..models.monitor_bulk_item import MonitorBulkItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = MonitorBulkItem.from_dict(items_item_data)

            items.append(items_item)

        _callback = d.pop("callback", UNSET)
        callback: JobCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = JobCallback.from_dict(_callback)

        continue_on_error = d.pop("continueOnError", UNSET)

        _defaults = d.pop("defaults", UNSET)
        defaults: MonitorBulkItem | Unset
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = MonitorBulkItem.from_dict(_defaults)

        _on_duplicate = d.pop("onDuplicate", UNSET)
        on_duplicate: MonitorBulkCreateRequestOnDuplicate | Unset
        if isinstance(_on_duplicate, Unset):
            on_duplicate = UNSET
        else:
            on_duplicate = check_monitor_bulk_create_request_on_duplicate(_on_duplicate)

        _on_error = d.pop("onError", UNSET)
        on_error: MonitorBulkCreateRequestOnError | Unset
        if isinstance(_on_error, Unset):
            on_error = UNSET
        else:
            on_error = check_monitor_bulk_create_request_on_error(_on_error)

        _on_overlimit = d.pop("onOverlimit", UNSET)
        on_overlimit: MonitorBulkCreateRequestOnOverlimit | Unset
        if isinstance(_on_overlimit, Unset):
            on_overlimit = UNSET
        else:
            on_overlimit = check_monitor_bulk_create_request_on_overlimit(_on_overlimit)

        monitor_bulk_create_request = cls(
            items=items,
            callback=callback,
            continue_on_error=continue_on_error,
            defaults=defaults,
            on_duplicate=on_duplicate,
            on_error=on_error,
            on_overlimit=on_overlimit,
        )

        return monitor_bulk_create_request
