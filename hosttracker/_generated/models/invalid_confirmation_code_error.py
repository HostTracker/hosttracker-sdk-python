from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidConfirmationCodeError")


@_attrs_define
class InvalidConfirmationCodeError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    attempts_left: int | Unset = UNSET
    """ How many further attempts are allowed. """
    expires_at: int | Unset = UNSET
    """ When the code expires, in Unix seconds. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        attempts_left = self.attempts_left

        expires_at = self.expires_at

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if attempts_left is not UNSET:
            field_dict["attemptsLeft"] = attempts_left
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        attempts_left = d.pop("attemptsLeft", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        reason = d.pop("reason", UNSET)

        invalid_confirmation_code_error = cls(
            pointer=pointer,
            attempts_left=attempts_left,
            expires_at=expires_at,
            reason=reason,
        )

        invalid_confirmation_code_error.additional_properties = d
        return invalid_confirmation_code_error

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
