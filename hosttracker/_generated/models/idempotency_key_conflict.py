from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.idempotency_key_conflict_code import IdempotencyKeyConflictCode, check_idempotency_key_conflict_code
from ..models.idempotency_key_conflict_status import IdempotencyKeyConflictStatus, check_idempotency_key_conflict_status
from ..models.idempotency_key_conflict_type import IdempotencyKeyConflictType, check_idempotency_key_conflict_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.idempotency_key_conflict_error import IdempotencyKeyConflictError


T = TypeVar("T", bound="IdempotencyKeyConflict")


@_attrs_define
class IdempotencyKeyConflict:
    """This idempotency key is already in use for a different request."""

    type_: IdempotencyKeyConflictType
    """ This code's documentation address. """
    title: str
    """ This idempotency key is already in use for a different request. """
    status: IdempotencyKeyConflictStatus
    """ The status this code always carries. """
    code: IdempotencyKeyConflictCode
    """ The stable machine code. Branch on this. """
    detail: str | Unset = UNSET
    """ Human detail about this occurrence. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on. """
    errors: list[IdempotencyKeyConflictError] | Unset = UNSET
    """ One entry per offending value, carrying `key`, `firstSeenAt`, `reason` and `retryAfterSeconds`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        title = self.title

        status: int = self.status

        code: str = self.code

        detail = self.detail

        instance = self.instance

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "status": status,
                "code": code,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.idempotency_key_conflict_error import IdempotencyKeyConflictError

        d = dict(src_dict)
        type_ = check_idempotency_key_conflict_type(d.pop("type"))

        title = d.pop("title")

        status = check_idempotency_key_conflict_status(d.pop("status"))

        code = check_idempotency_key_conflict_code(d.pop("code"))

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[IdempotencyKeyConflictError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = IdempotencyKeyConflictError.from_dict(errors_item_data)

                errors.append(errors_item)

        idempotency_key_conflict = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        idempotency_key_conflict.additional_properties = d
        return idempotency_key_conflict

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
