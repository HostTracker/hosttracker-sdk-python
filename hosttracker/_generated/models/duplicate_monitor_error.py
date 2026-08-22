from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duplicate_monitor_error_key_type_1 import DuplicateMonitorErrorKeyType1


T = TypeVar("T", bound="DuplicateMonitorError")


@_attrs_define
class DuplicateMonitorError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    existing_id: str | Unset = UNSET
    """ The id of the resource that already holds this key. """
    key: DuplicateMonitorErrorKeyType1 | str | Unset = UNSET
    """ The members that make up the conflicting key. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.duplicate_monitor_error_key_type_1 import DuplicateMonitorErrorKeyType1

        pointer = self.pointer

        existing_id = self.existing_id

        key: dict[str, Any] | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        elif isinstance(self.key, DuplicateMonitorErrorKeyType1):
            key = self.key.to_dict()
        else:
            key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if existing_id is not UNSET:
            field_dict["existingId"] = existing_id
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duplicate_monitor_error_key_type_1 import DuplicateMonitorErrorKeyType1

        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        existing_id = d.pop("existingId", UNSET)

        def _parse_key(data: object) -> DuplicateMonitorErrorKeyType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_type_1 = DuplicateMonitorErrorKeyType1.from_dict(data)

                return key_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DuplicateMonitorErrorKeyType1 | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        duplicate_monitor_error = cls(
            pointer=pointer,
            existing_id=existing_id,
            key=key,
        )

        duplicate_monitor_error.additional_properties = d
        return duplicate_monitor_error

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
