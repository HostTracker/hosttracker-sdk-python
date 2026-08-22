from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidUrlError")


@_attrs_define
class InvalidUrlError:
    pointer: str | Unset = UNSET
    """ Where the offending value is. """
    value: bool | float | str | Unset = UNSET
    """ The value that was rejected, echoed back. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    allowed: list[str] | Unset = UNSET
    """ The values that would have been accepted. """
    detail: str | Unset = UNSET
    """ Further detail about this entry. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        value: bool | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        reason = self.reason

        allowed: list[str] | Unset = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if value is not UNSET:
            field_dict["value"] = value
        if reason is not UNSET:
            field_dict["reason"] = reason
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        def _parse_value(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        reason = d.pop("reason", UNSET)

        allowed = cast(list[str], d.pop("allowed", UNSET))

        detail = d.pop("detail", UNSET)

        invalid_url_error = cls(
            pointer=pointer,
            value=value,
            reason=reason,
            allowed=allowed,
            detail=detail,
        )

        invalid_url_error.additional_properties = d
        return invalid_url_error

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
