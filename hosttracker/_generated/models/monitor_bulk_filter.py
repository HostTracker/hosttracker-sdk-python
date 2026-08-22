from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.monitor_bulk_filter_types_item import MonitorBulkFilterTypesItem, check_monitor_bulk_filter_types_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorBulkFilter")


@_attrs_define
class MonitorBulkFilter:
    """Which monitors the deletion selects. Never optional - an absent filter would match the whole account. The member
    names are the PLURAL forms; the list endpoint's query string spells the same narrowings in the singular.

    """

    monitor_ids: list[UUID] | Unset = UNSET
    """ A monitor to select, named explicitly. """
    types: list[MonitorBulkFilterTypesItem] | Unset = UNSET
    """ Select by monitor type. """
    tags: list[str] | Unset = UNSET
    """ A tag to select by. A monitor carrying any of them matches. """
    states: list[str] | Unset = UNSET
    """ A monitor state to select by. """
    enabled: bool | None | Unset = UNSET
    """ Select only enabled, or only disabled, monitors. """
    q: None | str | Unset = UNSET
    """ A case-insensitive substring match over name and address. """

    def to_dict(self) -> dict[str, Any]:
        monitor_ids: list[str] | Unset = UNSET
        if not isinstance(self.monitor_ids, Unset):
            monitor_ids = []
            for monitor_ids_item_data in self.monitor_ids:
                monitor_ids_item = str(monitor_ids_item_data)
                monitor_ids.append(monitor_ids_item)

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item: str = types_item_data
                types.append(types_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        states: list[str] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = self.states

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        q: None | str | Unset
        if isinstance(self.q, Unset):
            q = UNSET
        else:
            q = self.q

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if monitor_ids is not UNSET:
            field_dict["monitorIds"] = monitor_ids
        if types is not UNSET:
            field_dict["types"] = types
        if tags is not UNSET:
            field_dict["tags"] = tags
        if states is not UNSET:
            field_dict["states"] = states
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if q is not UNSET:
            field_dict["q"] = q

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _monitor_ids = d.pop("monitorIds", UNSET)
        monitor_ids: list[UUID] | Unset = UNSET
        if _monitor_ids is not UNSET:
            monitor_ids = []
            for monitor_ids_item_data in _monitor_ids:
                monitor_ids_item = UUID(monitor_ids_item_data)

                monitor_ids.append(monitor_ids_item)

        _types = d.pop("types", UNSET)
        types: list[MonitorBulkFilterTypesItem] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = check_monitor_bulk_filter_types_item(types_item_data)

                types.append(types_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        states = cast(list[str], d.pop("states", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_q(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        q = _parse_q(d.pop("q", UNSET))

        monitor_bulk_filter = cls(
            monitor_ids=monitor_ids,
            types=types,
            tags=tags,
            states=states,
            enabled=enabled,
            q=q,
        )

        return monitor_bulk_filter
