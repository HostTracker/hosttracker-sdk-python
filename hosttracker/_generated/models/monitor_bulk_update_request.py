from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.monitor_bulk_update_request_on_error import (
    MonitorBulkUpdateRequestOnError,
    check_monitor_bulk_update_request_on_error,
)
from ..models.monitor_bulk_update_request_on_overlimit import (
    MonitorBulkUpdateRequestOnOverlimit,
    check_monitor_bulk_update_request_on_overlimit,
)
from ..models.monitor_bulk_update_request_operation import (
    MonitorBulkUpdateRequestOperation,
    check_monitor_bulk_update_request_operation,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_callback import JobCallback
    from ..models.monitor_bulk_filter import MonitorBulkFilter
    from ..models.monitor_bulk_item import MonitorBulkItem


T = TypeVar("T", bound="MonitorBulkUpdateRequest")


@_attrs_define
class MonitorBulkUpdateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    callback: JobCallback | Unset = UNSET
    """ A webhook to call when the job finishes, carrying the terminal job document and its first page of results.
    Send null for none. """
    continue_on_error: bool | Unset = UNSET
    """ The older spelling of `onError`, still accepted: true means "continue", false means "stop". Sending both
    with different meanings is refused rather than resolved for you. """
    filter_: MonitorBulkFilter | Unset = UNSET
    """ Which monitors the deletion selects. Never optional - an absent filter would match the whole account. The
    member names are the PLURAL forms; the list endpoint's query string spells the same narrowings in the singular.
    """
    ids: list[UUID] | Unset = UNSET
    """ The resources this applies to, named explicitly. """
    on_error: MonitorBulkUpdateRequestOnError | Unset = UNSET
    """ Whether a failed item stops the run. "continue" (the default) attempts every item and reports each outcome
    separately; "stop" halts at the first refusal and reports every item that never ran as cancelled - which is what
    you want when the batch is one logical change. """
    on_overlimit: MonitorBulkUpdateRequestOnOverlimit | Unset = UNSET
    """ What to do with an item the account's package will not fit. "fail" (the default) refuses that item and
    carries on; "disable" creates it disabled so nothing is lost; "stop" halts the run and reports the remainder as
    cancelled. Packages that bill overages as extras never refuse, so this has no effect on them. """
    operation: MonitorBulkUpdateRequestOperation | Unset = UNSET
    """ Which operation to run over the selection, instead of - or alongside - a `patch`. At least one of the two is
    required. """
    patch: MonitorBulkItem | Unset = UNSET
    """ One monitor to create, in the same shape POST /monitor takes. A member this entry omits is taken from
    `defaults`; the two are merged before the entry is validated, so an entry may look incomplete on its own and
    still be valid. """

    def to_dict(self) -> dict[str, Any]:
        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        continue_on_error = self.continue_on_error

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = []
            for ids_item_data in self.ids:
                ids_item = str(ids_item_data)
                ids.append(ids_item)

        on_error: str | Unset = UNSET
        if not isinstance(self.on_error, Unset):
            on_error = self.on_error

        on_overlimit: str | Unset = UNSET
        if not isinstance(self.on_overlimit, Unset):
            on_overlimit = self.on_overlimit

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        patch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if callback is not UNSET:
            field_dict["callback"] = callback
        if continue_on_error is not UNSET:
            field_dict["continueOnError"] = continue_on_error
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if ids is not UNSET:
            field_dict["ids"] = ids
        if on_error is not UNSET:
            field_dict["onError"] = on_error
        if on_overlimit is not UNSET:
            field_dict["onOverlimit"] = on_overlimit
        if operation is not UNSET:
            field_dict["operation"] = operation
        if patch is not UNSET:
            field_dict["patch"] = patch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_callback import JobCallback
        from ..models.monitor_bulk_filter import MonitorBulkFilter
        from ..models.monitor_bulk_item import MonitorBulkItem

        d = dict(src_dict)
        _callback = d.pop("callback", UNSET)
        callback: JobCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = JobCallback.from_dict(_callback)

        continue_on_error = d.pop("continueOnError", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: MonitorBulkFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = MonitorBulkFilter.from_dict(_filter_)

        _ids = d.pop("ids", UNSET)
        ids: list[UUID] | Unset = UNSET
        if _ids is not UNSET:
            ids = []
            for ids_item_data in _ids:
                ids_item = UUID(ids_item_data)

                ids.append(ids_item)

        _on_error = d.pop("onError", UNSET)
        on_error: MonitorBulkUpdateRequestOnError | Unset
        if isinstance(_on_error, Unset):
            on_error = UNSET
        else:
            on_error = check_monitor_bulk_update_request_on_error(_on_error)

        _on_overlimit = d.pop("onOverlimit", UNSET)
        on_overlimit: MonitorBulkUpdateRequestOnOverlimit | Unset
        if isinstance(_on_overlimit, Unset):
            on_overlimit = UNSET
        else:
            on_overlimit = check_monitor_bulk_update_request_on_overlimit(_on_overlimit)

        _operation = d.pop("operation", UNSET)
        operation: MonitorBulkUpdateRequestOperation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_monitor_bulk_update_request_operation(_operation)

        _patch = d.pop("patch", UNSET)
        patch: MonitorBulkItem | Unset
        if isinstance(_patch, Unset):
            patch = UNSET
        else:
            patch = MonitorBulkItem.from_dict(_patch)

        monitor_bulk_update_request = cls(
            callback=callback,
            continue_on_error=continue_on_error,
            filter_=filter_,
            ids=ids,
            on_error=on_error,
            on_overlimit=on_overlimit,
            operation=operation,
            patch=patch,
        )

        return monitor_bulk_update_request
