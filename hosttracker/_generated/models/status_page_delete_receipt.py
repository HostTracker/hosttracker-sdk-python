from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_delete_cascade import StatusPageDeleteCascade


T = TypeVar("T", bound="StatusPageDeleteReceipt")


@_attrs_define
class StatusPageDeleteReceipt:
    """**The status-page family's deletion receipts** - the shape every other v2 delete already answered with, and these
    four did not. A bare `{"deleted": true}` tells the caller nothing it did not already know: not WHICH row went (a
    client deleting several in a loop cannot pair a response with its request), not WHAT KIND of thing it was (a receipt
    read on its own, or logged beside a sibling's, is unreadable), and above all not what went WITH it - information
    that has no other source, because the rows are gone by the time anyone could ask. The family's shape is `{id,
    deleted, type, …identity, cascaded}`; these join it.

    """

    id: UUID
    deleted: bool
    type_: str | Unset = UNSET
    """ The resource kind this receipt describes - always `"statusPage"`, the same token the family's 404s use. """
    slug: str | Unset = UNSET
    """ The page's slug at the moment it was deleted - its public address, and the identity a human recognises it
    by. The slug is free again after this. """
    title: None | str | Unset = UNSET
    cascaded: StatusPageDeleteCascade | Unset = UNSET
    """ What went with the page. Counted BEFORE the delete runs - the store removes the rows and reports nothing, so
    this is the caller's only chance to learn it. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deleted = self.deleted

        type_ = self.type_

        slug = self.slug

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        cascaded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cascaded, Unset):
            cascaded = self.cascaded.to_dict()

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
        if slug is not UNSET:
            field_dict["slug"] = slug
        if title is not UNSET:
            field_dict["title"] = title
        if cascaded is not UNSET:
            field_dict["cascaded"] = cascaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_delete_cascade import StatusPageDeleteCascade

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deleted = d.pop("deleted")

        type_ = d.pop("type", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _cascaded = d.pop("cascaded", UNSET)
        cascaded: StatusPageDeleteCascade | Unset
        if isinstance(_cascaded, Unset):
            cascaded = UNSET
        else:
            cascaded = StatusPageDeleteCascade.from_dict(_cascaded)

        status_page_delete_receipt = cls(
            id=id,
            deleted=deleted,
            type_=type_,
            slug=slug,
            title=title,
            cascaded=cascaded,
        )

        status_page_delete_receipt.additional_properties = d
        return status_page_delete_receipt

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
