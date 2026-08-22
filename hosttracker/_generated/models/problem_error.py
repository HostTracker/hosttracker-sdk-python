from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemError")


@_attrs_define
class ProblemError:
    pointer: None | str | Unset = UNSET
    """ RFC 6901 JSON Pointer into the request body (`/interval`, `/contacts/1/address`) or the query-parameter name
    for a query failure (`/limit`). Null when the problem is document-scoped. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer: None | str | Unset
        if isinstance(self.pointer, Unset):
            pointer = UNSET
        else:
            pointer = self.pointer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_pointer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pointer = _parse_pointer(d.pop("pointer", UNSET))

        problem_error = cls(
            pointer=pointer,
        )

        problem_error.additional_properties = d
        return problem_error

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
