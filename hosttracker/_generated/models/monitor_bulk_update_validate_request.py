from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.monitor_bulk_update_validate_request_operation import (
    MonitorBulkUpdateValidateRequestOperation,
    check_monitor_bulk_update_validate_request_operation,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_bulk_filter import MonitorBulkFilter
    from ..models.monitor_bulk_item import MonitorBulkItem


T = TypeVar("T", bound="MonitorBulkUpdateValidateRequest")


@_attrs_define
class MonitorBulkUpdateValidateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    filter_: MonitorBulkFilter | Unset = UNSET
    """ Which monitors the deletion selects. Never optional - an absent filter would match the whole account. The
    member names are the PLURAL forms; the list endpoint's query string spells the same narrowings in the singular.
    """
    ids: list[UUID] | Unset = UNSET
    """ The resources this applies to, named explicitly. """
    operation: MonitorBulkUpdateValidateRequestOperation | Unset = UNSET
    """ Which operation to run over the selection, instead of - or alongside - a `patch`. At least one of the two is
    required. """
    patch: MonitorBulkItem | Unset = UNSET
    """ One monitor to create, in the same shape POST /monitor takes. A member this entry omits is taken from
    `defaults`; the two are merged before the entry is validated, so an entry may look incomplete on its own and
    still be valid. """

    def to_dict(self) -> dict[str, Any]:
        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = []
            for ids_item_data in self.ids:
                ids_item = str(ids_item_data)
                ids.append(ids_item)

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        patch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if ids is not UNSET:
            field_dict["ids"] = ids
        if operation is not UNSET:
            field_dict["operation"] = operation
        if patch is not UNSET:
            field_dict["patch"] = patch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_bulk_filter import MonitorBulkFilter
        from ..models.monitor_bulk_item import MonitorBulkItem

        d = dict(src_dict)
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

        _operation = d.pop("operation", UNSET)
        operation: MonitorBulkUpdateValidateRequestOperation | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_monitor_bulk_update_validate_request_operation(_operation)

        _patch = d.pop("patch", UNSET)
        patch: MonitorBulkItem | Unset
        if isinstance(_patch, Unset):
            patch = UNSET
        else:
            patch = MonitorBulkItem.from_dict(_patch)

        monitor_bulk_update_validate_request = cls(
            filter_=filter_,
            ids=ids,
            operation=operation,
            patch=patch,
        )

        return monitor_bulk_update_validate_request
