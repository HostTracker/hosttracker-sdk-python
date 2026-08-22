from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookJobResult")


@_attrs_define
class WebhookJobResult:
    """One item's receipt."""

    index: int
    """ The item's position in the submitted array. """
    status: str
    """ What the job did with this item: created, updated, skipped, deleted, failed, … """
    item_ref: str | Unset = UNSET
    """ The caller's own reference for the item, when the request supplied one. """
    entity_id: UUID | Unset = UNSET
    """ The resource the item produced or touched. Absent for a failure. """
    error: str | Unset = UNSET
    """ Why the item failed. Absent otherwise. """

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        status = self.status

        item_ref = self.item_ref

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "index": index,
                "status": status,
            }
        )
        if item_ref is not UNSET:
            field_dict["itemRef"] = item_ref
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        status = d.pop("status")

        item_ref = d.pop("itemRef", UNSET)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        error = d.pop("error", UNSET)

        webhook_job_result = cls(
            index=index,
            status=status,
            item_ref=item_ref,
            entity_id=entity_id,
            error=error,
        )

        return webhook_job_result
