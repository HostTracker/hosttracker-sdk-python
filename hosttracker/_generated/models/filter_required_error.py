from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterRequiredError")


@_attrs_define
class FilterRequiredError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    parameter: str | Unset = UNSET
    """ The query parameter involved. """
    operation: str | Unset = UNSET
    """ The operation that refused. """
    hint: str | Unset = UNSET
    """ What to send to make the request acceptable. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    preview: str | Unset = UNSET
    """ The dry-run call that shows what the filter would select before anything acts on it. """
    expected: bool | float | str | Unset = UNSET
    """ The value the two sides of this comparison disagree on. On a selection mismatch it is the count YOUR preview
    reported and `actual` is what the server counts NOW - the drift is the point. Where the refusal is about a token
    or a flag instead, it is the value the server required. """
    value: bool | float | str | Unset = UNSET
    """ The value that was rejected, echoed back. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        parameter = self.parameter

        operation = self.operation

        hint = self.hint

        reason = self.reason

        preview = self.preview

        expected: bool | float | str | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected

        value: bool | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if operation is not UNSET:
            field_dict["operation"] = operation
        if hint is not UNSET:
            field_dict["hint"] = hint
        if reason is not UNSET:
            field_dict["reason"] = reason
        if preview is not UNSET:
            field_dict["preview"] = preview
        if expected is not UNSET:
            field_dict["expected"] = expected
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        parameter = d.pop("parameter", UNSET)

        operation = d.pop("operation", UNSET)

        hint = d.pop("hint", UNSET)

        reason = d.pop("reason", UNSET)

        preview = d.pop("preview", UNSET)

        def _parse_expected(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))

        def _parse_value(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        filter_required_error = cls(
            pointer=pointer,
            parameter=parameter,
            operation=operation,
            hint=hint,
            reason=reason,
            preview=preview,
            expected=expected,
            value=value,
        )

        filter_required_error.additional_properties = d
        return filter_required_error

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
