from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insufficient_agents_pool import InsufficientAgentsPool


T = TypeVar("T", bound="InsufficientAgentsError")


@_attrs_define
class InsufficientAgentsError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    required: str | Unset = UNSET
    """ What the operation needed. """
    matched: int | Unset = UNSET
    """ How many candidates matched. """
    per_pool: list[InsufficientAgentsPool] | Unset = UNSET
    """ The per-pool breakdown behind the match count. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        required = self.required

        matched = self.matched

        per_pool: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.per_pool, Unset):
            per_pool = []
            for per_pool_item_data in self.per_pool:
                per_pool_item = per_pool_item_data.to_dict()
                per_pool.append(per_pool_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if required is not UNSET:
            field_dict["required"] = required
        if matched is not UNSET:
            field_dict["matched"] = matched
        if per_pool is not UNSET:
            field_dict["perPool"] = per_pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insufficient_agents_pool import InsufficientAgentsPool

        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        required = d.pop("required", UNSET)

        matched = d.pop("matched", UNSET)

        _per_pool = d.pop("perPool", UNSET)
        per_pool: list[InsufficientAgentsPool] | Unset = UNSET
        if _per_pool is not UNSET:
            per_pool = []
            for per_pool_item_data in _per_pool:
                per_pool_item = InsufficientAgentsPool.from_dict(per_pool_item_data)

                per_pool.append(per_pool_item)

        insufficient_agents_error = cls(
            pointer=pointer,
            required=required,
            matched=matched,
            per_pool=per_pool,
        )

        insufficient_agents_error.additional_properties = d
        return insufficient_agents_error

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
