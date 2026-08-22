from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.contact_bulk_delete_request_on_error import (
    ContactBulkDeleteRequestOnError,
    check_contact_bulk_delete_request_on_error,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_bulk_filter import ContactBulkFilter
    from ..models.job_callback import JobCallback


T = TypeVar("T", bound="ContactBulkDeleteRequest")


@_attrs_define
class ContactBulkDeleteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    expected_count: int
    """ How many contacts the matching bulk-delete-validate call reported for this filter. The server re-resolves
    the filter and refuses if the number has changed, so a deletion can never be wider than what was shown to the
    caller. Re-run the validate call and resubmit with its number. """
    filter_: ContactBulkFilter
    """ Which contacts the deletion selects. A filter that narrows by nothing is REFUSED - it would select every
    contact on the account. The member names are the plural forms; the list endpoint's query string spells the same
    narrowings in the singular. """
    callback: JobCallback | Unset = UNSET
    """ A webhook to call when the job finishes, carrying the terminal job document and its first page of results.
    Send null for none. """
    on_error: ContactBulkDeleteRequestOnError | Unset = UNSET
    """ Whether a failed item stops the run. "continue" (the default) attempts every item and reports each outcome
    separately; "stop" halts at the first refusal and reports every item that never ran as cancelled - which is what
    you want when the batch is one logical change. """

    def to_dict(self) -> dict[str, Any]:
        expected_count = self.expected_count

        filter_ = self.filter_.to_dict()

        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        on_error: str | Unset = UNSET
        if not isinstance(self.on_error, Unset):
            on_error = self.on_error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedCount": expected_count,
                "filter": filter_,
            }
        )
        if callback is not UNSET:
            field_dict["callback"] = callback
        if on_error is not UNSET:
            field_dict["onError"] = on_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_bulk_filter import ContactBulkFilter
        from ..models.job_callback import JobCallback

        d = dict(src_dict)
        expected_count = d.pop("expectedCount")

        filter_ = ContactBulkFilter.from_dict(d.pop("filter"))

        _callback = d.pop("callback", UNSET)
        callback: JobCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = JobCallback.from_dict(_callback)

        _on_error = d.pop("onError", UNSET)
        on_error: ContactBulkDeleteRequestOnError | Unset
        if isinstance(_on_error, Unset):
            on_error = UNSET
        else:
            on_error = check_contact_bulk_delete_request_on_error(_on_error)

        contact_bulk_delete_request = cls(
            expected_count=expected_count,
            filter_=filter_,
            callback=callback,
            on_error=on_error,
        )

        return contact_bulk_delete_request
