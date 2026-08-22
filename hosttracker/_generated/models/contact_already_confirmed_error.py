from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactAlreadyConfirmedError")


@_attrs_define
class ContactAlreadyConfirmedError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    contact_id: str | Unset = UNSET
    """ The contact involved. """
    confirmed_at: int | Unset = UNSET
    """ When the contact was confirmed, in Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        contact_id = self.contact_id

        confirmed_at = self.confirmed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if confirmed_at is not UNSET:
            field_dict["confirmedAt"] = confirmed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        contact_id = d.pop("contactId", UNSET)

        confirmed_at = d.pop("confirmedAt", UNSET)

        contact_already_confirmed_error = cls(
            pointer=pointer,
            contact_id=contact_id,
            confirmed_at=confirmed_at,
        )

        contact_already_confirmed_error.additional_properties = d
        return contact_already_confirmed_error

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
