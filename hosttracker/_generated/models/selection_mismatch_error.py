from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectionMismatchError")


@_attrs_define
class SelectionMismatchError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    expected: bool | float | str | Unset = UNSET
    """ The value the two sides of this comparison disagree on. On a selection mismatch it is the count YOUR preview
    reported and `actual` is what the server counts NOW - the drift is the point. Where the refusal is about a token
    or a flag instead, it is the value the server required. """
    actual: bool | float | str | Unset = UNSET
    """ What it found instead. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        expected: bool | float | str | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected

        actual: bool | float | str | Unset
        if isinstance(self.actual, Unset):
            actual = UNSET
        else:
            actual = self.actual

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if expected is not UNSET:
            field_dict["expected"] = expected
        if actual is not UNSET:
            field_dict["actual"] = actual

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        def _parse_expected(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))

        def _parse_actual(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        actual = _parse_actual(d.pop("actual", UNSET))

        selection_mismatch_error = cls(
            pointer=pointer,
            expected=expected,
            actual=actual,
        )

        selection_mismatch_error.additional_properties = d
        return selection_mismatch_error

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
