from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageSubscriberDeleteReceipt")


@_attrs_define
class StatusPageSubscriberDeleteReceipt:
    """The receipt a subscriber removal answers with. Nothing hangs off a subscriber either; what a caller needs back is
    WHICH one it removed, since the id alone identifies neither the channel nor the address behind it.

    """

    id: UUID
    deleted: bool
    type_: str | Unset = UNSET
    kind: str | Unset = UNSET
    """ Which kind of subscriber it was - `email`, `webhook`, `slack` or `teams`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deleted = self.deleted

        type_ = self.type_

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deleted": deleted,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deleted = d.pop("deleted")

        type_ = d.pop("type", UNSET)

        kind = d.pop("kind", UNSET)

        status_page_subscriber_delete_receipt = cls(
            id=id,
            deleted=deleted,
            type_=type_,
            kind=kind,
        )

        status_page_subscriber_delete_receipt.additional_properties = d
        return status_page_subscriber_delete_receipt

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
