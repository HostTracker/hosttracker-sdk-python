from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_bulk_delete_request_on_error import (
    MonitorBulkDeleteRequestOnError,
    check_monitor_bulk_delete_request_on_error,
)
from ..models.monitor_bulk_delete_request_on_overlimit import (
    MonitorBulkDeleteRequestOnOverlimit,
    check_monitor_bulk_delete_request_on_overlimit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_callback import JobCallback
    from ..models.monitor_bulk_filter import MonitorBulkFilter


T = TypeVar("T", bound="MonitorBulkDeleteRequest")


@_attrs_define
class MonitorBulkDeleteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    expected_count: int
    """ How many monitors the matching bulk-delete-validate call reported for this filter. The server re-resolves
    the filter and refuses if the number has changed, so a deletion can never be wider than what was shown to the
    caller. Re-run the validate call and resubmit with its number. """
    filter_: MonitorBulkFilter
    """ Which monitors the deletion selects. Never optional - an absent filter would match the whole account. The
    member names are the PLURAL forms; the list endpoint's query string spells the same narrowings in the singular.
    """
    callback: JobCallback | Unset = UNSET
    """ A webhook to call when the job finishes, carrying the terminal job document and its first page of results.
    Send null for none. """
    continue_on_error: bool | Unset = UNSET
    """ The older spelling of `onError`, still accepted: true means "continue", false means "stop". Sending both
    with different meanings is refused rather than resolved for you. """
    on_error: MonitorBulkDeleteRequestOnError | Unset = UNSET
    """ Whether a failed item stops the run. "continue" (the default) attempts every item and reports each outcome
    separately; "stop" halts at the first refusal and reports every item that never ran as cancelled - which is what
    you want when the batch is one logical change. """
    on_overlimit: MonitorBulkDeleteRequestOnOverlimit | Unset = UNSET
    """ What to do with an item the account's package will not fit. "fail" (the default) refuses that item and
    carries on; "disable" creates it disabled so nothing is lost; "stop" halts the run and reports the remainder as
    cancelled. Packages that bill overages as extras never refuse, so this has no effect on them. """

    def to_dict(self) -> dict[str, Any]:
        expected_count = self.expected_count

        filter_ = self.filter_.to_dict()

        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        continue_on_error = self.continue_on_error

        on_error: str | Unset = UNSET
        if not isinstance(self.on_error, Unset):
            on_error = self.on_error

        on_overlimit: str | Unset = UNSET
        if not isinstance(self.on_overlimit, Unset):
            on_overlimit = self.on_overlimit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedCount": expected_count,
                "filter": filter_,
            }
        )
        if callback is not UNSET:
            field_dict["callback"] = callback
        if continue_on_error is not UNSET:
            field_dict["continueOnError"] = continue_on_error
        if on_error is not UNSET:
            field_dict["onError"] = on_error
        if on_overlimit is not UNSET:
            field_dict["onOverlimit"] = on_overlimit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_callback import JobCallback
        from ..models.monitor_bulk_filter import MonitorBulkFilter

        d = dict(src_dict)
        expected_count = d.pop("expectedCount")

        filter_ = MonitorBulkFilter.from_dict(d.pop("filter"))

        _callback = d.pop("callback", UNSET)
        callback: JobCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = JobCallback.from_dict(_callback)

        continue_on_error = d.pop("continueOnError", UNSET)

        _on_error = d.pop("onError", UNSET)
        on_error: MonitorBulkDeleteRequestOnError | Unset
        if isinstance(_on_error, Unset):
            on_error = UNSET
        else:
            on_error = check_monitor_bulk_delete_request_on_error(_on_error)

        _on_overlimit = d.pop("onOverlimit", UNSET)
        on_overlimit: MonitorBulkDeleteRequestOnOverlimit | Unset
        if isinstance(_on_overlimit, Unset):
            on_overlimit = UNSET
        else:
            on_overlimit = check_monitor_bulk_delete_request_on_overlimit(_on_overlimit)

        monitor_bulk_delete_request = cls(
            expected_count=expected_count,
            filter_=filter_,
            callback=callback,
            continue_on_error=continue_on_error,
            on_error=on_error,
            on_overlimit=on_overlimit,
        )

        return monitor_bulk_delete_request
