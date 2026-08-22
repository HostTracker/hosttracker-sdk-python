from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_delete_cascade import ContactDeleteCascade


T = TypeVar("T", bound="ContactDeleteReceipt")


@_attrs_define
class ContactDeleteReceipt:
    id: UUID
    deleted: bool
    type_: str | Unset = UNSET
    address: None | str | Unset = UNSET
    webhook: bool | None | Unset = UNSET
    """ ** `true` when the row deleted was also a webhook** - `GET /webhook` lost an entry and an integration
    stopped receiving deliveries. A webhook **is** an `http` contact (O-16R): one row, two doors, and the delete is
    the same delete either way. That is a deliberate design, but until this member the receipt described the
    consequence in contact vocabulary only - so routine contact-list hygiene ("remove these `http` rows I do not
    recognise") tore down a live integration and said nothing about it. The delete is NOT refused: both doors
    address the same row by design, and refusing one of them would make the shared identity harder to understand,
    not easier. It is **named** instead. Absent - never `false` - for an ordinary contact, so every other receipt on
    the surface is unchanged and the member's presence is itself the signal. """
    cascaded: ContactDeleteCascade | Unset = UNSET
    """ What went with the contact. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deleted = self.deleted

        type_ = self.type_

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        webhook: bool | None | Unset
        if isinstance(self.webhook, Unset):
            webhook = UNSET
        else:
            webhook = self.webhook

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
        if address is not UNSET:
            field_dict["address"] = address
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if cascaded is not UNSET:
            field_dict["cascaded"] = cascaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_delete_cascade import ContactDeleteCascade

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deleted = d.pop("deleted")

        type_ = d.pop("type", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_webhook(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        webhook = _parse_webhook(d.pop("webhook", UNSET))

        _cascaded = d.pop("cascaded", UNSET)
        cascaded: ContactDeleteCascade | Unset
        if isinstance(_cascaded, Unset):
            cascaded = UNSET
        else:
            cascaded = ContactDeleteCascade.from_dict(_cascaded)

        contact_delete_receipt = cls(
            id=id,
            deleted=deleted,
            type_=type_,
            address=address,
            webhook=webhook,
            cascaded=cascaded,
        )

        contact_delete_receipt.additional_properties = d
        return contact_delete_receipt

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
