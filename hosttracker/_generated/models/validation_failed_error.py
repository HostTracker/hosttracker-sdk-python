from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationFailedError")


@_attrs_define
class ValidationFailedError:
    pointer: str | Unset = UNSET
    """ Where the offending value is. """
    parameter: str | Unset = UNSET
    """ The query parameter involved. """
    detail: str | Unset = UNSET
    """ Further detail about this entry. """
    value: bool | float | str | Unset = UNSET
    """ The value that was rejected, echoed back. """
    allowed: list[str] | Unset = UNSET
    """ The values that would have been accepted. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    min_: float | Unset = UNSET
    """ The smallest accepted value. """
    max_: float | Unset = UNSET
    """ The largest accepted value. """
    did_you_mean: str | Unset = UNSET
    """ The name this one is probably a misspelling of. """
    expires_in: int | Unset = UNSET
    """ Seconds the token was valid for. """
    expected: bool | float | str | Unset = UNSET
    """ The value the two sides of this comparison disagree on. On a selection mismatch it is the count YOUR preview
    reported and `actual` is what the server counts NOW - the drift is the point. Where the refusal is about a token
    or a flag instead, it is the value the server required. """
    min_items: int | Unset = UNSET
    """ The fewest items this operation accepts in one request. """
    max_items: int | Unset = UNSET
    """ The most items this operation accepts in one request - the same fact as `limit`, under the spelling this
    endpoint uses. """
    alternatives: list[str] | Unset = UNSET
    """ Other ways to express the same request that this operation does accept. """
    one_of: list[str] | Unset = UNSET
    """ Members of which exactly one satisfies the requirement - send any single one of them. """
    existing_id: str | Unset = UNSET
    """ The id of the resource that already holds this key. """
    retry_after_seconds: int | Unset = UNSET
    """ Seconds to wait before retrying. Mirrors the Retry-After header. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        parameter = self.parameter

        detail = self.detail

        value: bool | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        allowed: list[str] | Unset = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed

        reason = self.reason

        min_ = self.min_

        max_ = self.max_

        did_you_mean = self.did_you_mean

        expires_in = self.expires_in

        expected: bool | float | str | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected

        min_items = self.min_items

        max_items = self.max_items

        alternatives: list[str] | Unset = UNSET
        if not isinstance(self.alternatives, Unset):
            alternatives = self.alternatives

        one_of: list[str] | Unset = UNSET
        if not isinstance(self.one_of, Unset):
            one_of = self.one_of

        existing_id = self.existing_id

        retry_after_seconds = self.retry_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if detail is not UNSET:
            field_dict["detail"] = detail
        if value is not UNSET:
            field_dict["value"] = value
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if reason is not UNSET:
            field_dict["reason"] = reason
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if did_you_mean is not UNSET:
            field_dict["didYouMean"] = did_you_mean
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in
        if expected is not UNSET:
            field_dict["expected"] = expected
        if min_items is not UNSET:
            field_dict["minItems"] = min_items
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if alternatives is not UNSET:
            field_dict["alternatives"] = alternatives
        if one_of is not UNSET:
            field_dict["oneOf"] = one_of
        if existing_id is not UNSET:
            field_dict["existingId"] = existing_id
        if retry_after_seconds is not UNSET:
            field_dict["retryAfterSeconds"] = retry_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        parameter = d.pop("parameter", UNSET)

        detail = d.pop("detail", UNSET)

        def _parse_value(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        allowed = cast(list[str], d.pop("allowed", UNSET))

        reason = d.pop("reason", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        did_you_mean = d.pop("didYouMean", UNSET)

        expires_in = d.pop("expiresIn", UNSET)

        def _parse_expected(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))

        min_items = d.pop("minItems", UNSET)

        max_items = d.pop("maxItems", UNSET)

        alternatives = cast(list[str], d.pop("alternatives", UNSET))

        one_of = cast(list[str], d.pop("oneOf", UNSET))

        existing_id = d.pop("existingId", UNSET)

        retry_after_seconds = d.pop("retryAfterSeconds", UNSET)

        validation_failed_error = cls(
            pointer=pointer,
            parameter=parameter,
            detail=detail,
            value=value,
            allowed=allowed,
            reason=reason,
            min_=min_,
            max_=max_,
            did_you_mean=did_you_mean,
            expires_in=expires_in,
            expected=expected,
            min_items=min_items,
            max_items=max_items,
            alternatives=alternatives,
            one_of=one_of,
            existing_id=existing_id,
            retry_after_seconds=retry_after_seconds,
        )

        validation_failed_error.additional_properties = d
        return validation_failed_error

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
