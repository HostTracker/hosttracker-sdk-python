from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.idempotency_key_conflict_error_key_type_1 import IdempotencyKeyConflictErrorKeyType1


T = TypeVar("T", bound="IdempotencyKeyConflictError")


@_attrs_define
class IdempotencyKeyConflictError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    key: IdempotencyKeyConflictErrorKeyType1 | str | Unset = UNSET
    """ The members that make up the conflicting key. """
    first_seen_at: int | Unset = UNSET
    """ When this key was first used, in Unix seconds. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    retry_after_seconds: int | Unset = UNSET
    """ Seconds to wait before retrying. Mirrors the Retry-After header. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.idempotency_key_conflict_error_key_type_1 import IdempotencyKeyConflictErrorKeyType1

        pointer = self.pointer

        key: dict[str, Any] | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        elif isinstance(self.key, IdempotencyKeyConflictErrorKeyType1):
            key = self.key.to_dict()
        else:
            key = self.key

        first_seen_at = self.first_seen_at

        reason = self.reason

        retry_after_seconds = self.retry_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if key is not UNSET:
            field_dict["key"] = key
        if first_seen_at is not UNSET:
            field_dict["firstSeenAt"] = first_seen_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if retry_after_seconds is not UNSET:
            field_dict["retryAfterSeconds"] = retry_after_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.idempotency_key_conflict_error_key_type_1 import IdempotencyKeyConflictErrorKeyType1

        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        def _parse_key(data: object) -> IdempotencyKeyConflictErrorKeyType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_type_1 = IdempotencyKeyConflictErrorKeyType1.from_dict(data)

                return key_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IdempotencyKeyConflictErrorKeyType1 | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        first_seen_at = d.pop("firstSeenAt", UNSET)

        reason = d.pop("reason", UNSET)

        retry_after_seconds = d.pop("retryAfterSeconds", UNSET)

        idempotency_key_conflict_error = cls(
            pointer=pointer,
            key=key,
            first_seen_at=first_seen_at,
            reason=reason,
            retry_after_seconds=retry_after_seconds,
        )

        idempotency_key_conflict_error.additional_properties = d
        return idempotency_key_conflict_error

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
