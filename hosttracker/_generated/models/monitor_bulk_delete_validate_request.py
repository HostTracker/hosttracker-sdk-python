from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.monitor_bulk_filter import MonitorBulkFilter


T = TypeVar("T", bound="MonitorBulkDeleteValidateRequest")


@_attrs_define
class MonitorBulkDeleteValidateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    filter_: MonitorBulkFilter
    """ Which monitors the deletion selects. Never optional - an absent filter would match the whole account. The
    member names are the PLURAL forms; the list endpoint's query string spells the same narrowings in the singular.
    """

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_bulk_filter import MonitorBulkFilter

        d = dict(src_dict)
        filter_ = MonitorBulkFilter.from_dict(d.pop("filter"))

        monitor_bulk_delete_validate_request = cls(
            filter_=filter_,
        )

        return monitor_bulk_delete_validate_request
