from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidRangeError")


@_attrs_define
class InvalidRangeError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    parameter: str | Unset = UNSET
    """ The query parameter involved. """
    from_: int | Unset = UNSET
    """ The window start that was requested, in Unix seconds. """
    to: int | Unset = UNSET
    """ The window end that was requested, in Unix seconds. """
    max_span: int | Unset = UNSET
    """ The largest window this operation accepts, in seconds. """
    suggested_bucket: str | Unset = UNSET
    """ A bucket size that would make the requested window fit. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    value: bool | float | str | Unset = UNSET
    """ The value that was rejected, echoed back. """
    min_: float | Unset = UNSET
    """ The smallest accepted value. """
    max_: float | Unset = UNSET
    """ The largest accepted value. """
    buckets: int | Unset = UNSET
    """ How many buckets the requested granularity would produce over the requested range. """
    detail: str | Unset = UNSET
    """ Further detail about this entry. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        parameter = self.parameter

        from_ = self.from_

        to = self.to

        max_span = self.max_span

        suggested_bucket = self.suggested_bucket

        reason = self.reason

        value: bool | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        min_ = self.min_

        max_ = self.max_

        buckets = self.buckets

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if max_span is not UNSET:
            field_dict["maxSpan"] = max_span
        if suggested_bucket is not UNSET:
            field_dict["suggestedBucket"] = suggested_bucket
        if reason is not UNSET:
            field_dict["reason"] = reason
        if value is not UNSET:
            field_dict["value"] = value
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        parameter = d.pop("parameter", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        max_span = d.pop("maxSpan", UNSET)

        suggested_bucket = d.pop("suggestedBucket", UNSET)

        reason = d.pop("reason", UNSET)

        def _parse_value(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        buckets = d.pop("buckets", UNSET)

        detail = d.pop("detail", UNSET)

        invalid_range_error = cls(
            pointer=pointer,
            parameter=parameter,
            from_=from_,
            to=to,
            max_span=max_span,
            suggested_bucket=suggested_bucket,
            reason=reason,
            value=value,
            min_=min_,
            max_=max_,
            buckets=buckets,
            detail=detail,
        )

        invalid_range_error.additional_properties = d
        return invalid_range_error

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
