from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnsupportedReportChannelError")


@_attrs_define
class UnsupportedReportChannelError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    contact_type: str | Unset = UNSET
    """ The contact type involved. """
    supported: list[str] | Unset = UNSET
    """ The values that are supported here. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        contact_type = self.contact_type

        supported: list[str] | Unset = UNSET
        if not isinstance(self.supported, Unset):
            supported = self.supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if contact_type is not UNSET:
            field_dict["contactType"] = contact_type
        if supported is not UNSET:
            field_dict["supported"] = supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        contact_type = d.pop("contactType", UNSET)

        supported = cast(list[str], d.pop("supported", UNSET))

        unsupported_report_channel_error = cls(
            pointer=pointer,
            contact_type=contact_type,
            supported=supported,
        )

        unsupported_report_channel_error.additional_properties = d
        return unsupported_report_channel_error

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
