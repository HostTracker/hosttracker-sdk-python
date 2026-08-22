from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnsupportedMediaTypeError")


@_attrs_define
class UnsupportedMediaTypeError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    content_type: str | Unset = UNSET
    """ The media type that was sent. """
    supported: list[str] | Unset = UNSET
    """ The values that are supported here. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        content_type = self.content_type

        supported: list[str] | Unset = UNSET
        if not isinstance(self.supported, Unset):
            supported = self.supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if supported is not UNSET:
            field_dict["supported"] = supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        content_type = d.pop("contentType", UNSET)

        supported = cast(list[str], d.pop("supported", UNSET))

        unsupported_media_type_error = cls(
            pointer=pointer,
            content_type=content_type,
            supported=supported,
        )

        unsupported_media_type_error.additional_properties = d
        return unsupported_media_type_error

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
