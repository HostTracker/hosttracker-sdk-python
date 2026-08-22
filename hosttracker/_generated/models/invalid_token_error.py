from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidTokenError")


@_attrs_define
class InvalidTokenError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    expired_at: int | Unset = UNSET
    """ When the token expired, in Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        reason = self.reason

        expired_at = self.expired_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if reason is not UNSET:
            field_dict["reason"] = reason
        if expired_at is not UNSET:
            field_dict["expiredAt"] = expired_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        reason = d.pop("reason", UNSET)

        expired_at = d.pop("expiredAt", UNSET)

        invalid_token_error = cls(
            pointer=pointer,
            reason=reason,
            expired_at=expired_at,
        )

        invalid_token_error.additional_properties = d
        return invalid_token_error

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
