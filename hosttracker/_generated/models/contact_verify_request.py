from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactVerifyRequest")


@_attrs_define
class ContactVerifyRequest:
    """The confirmation code a contact received."""

    code: str | Unset = UNSET
    """ The code, exactly as it was delivered. """

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        contact_verify_request = cls(
            code=code,
        )

        return contact_verify_request
