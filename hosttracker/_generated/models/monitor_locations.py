from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_locations_fallback import MonitorLocationsFallback, check_monitor_locations_fallback
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorLocations")


@_attrs_define
class MonitorLocations:
    """Where the check runs from."""

    pools: list[str] | Unset = UNSET
    """ A monitoring-location pool to run from. Send at least one; for everywhere send ["allworld"], and to leave
    the current pinning alone omit the member. """
    fallback: MonitorLocationsFallback | Unset = UNSET
    """ What to do when no location in the chosen pools is available. Send null to clear it. """
    excluded_agents: list[UUID] | Unset = UNSET
    """ A specific monitoring location to keep this check off. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pools: list[str] | Unset = UNSET
        if not isinstance(self.pools, Unset):
            pools = self.pools

        fallback: str | Unset = UNSET
        if not isinstance(self.fallback, Unset):
            fallback = self.fallback

        excluded_agents: list[str] | Unset = UNSET
        if not isinstance(self.excluded_agents, Unset):
            excluded_agents = []
            for excluded_agents_item_data in self.excluded_agents:
                excluded_agents_item = str(excluded_agents_item_data)
                excluded_agents.append(excluded_agents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pools is not UNSET:
            field_dict["pools"] = pools
        if fallback is not UNSET:
            field_dict["fallback"] = fallback
        if excluded_agents is not UNSET:
            field_dict["excludedAgents"] = excluded_agents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pools = cast(list[str], d.pop("pools", UNSET))

        _fallback = d.pop("fallback", UNSET)
        fallback: MonitorLocationsFallback | Unset
        if isinstance(_fallback, Unset):
            fallback = UNSET
        else:
            fallback = check_monitor_locations_fallback(_fallback)

        _excluded_agents = d.pop("excludedAgents", UNSET)
        excluded_agents: list[UUID] | Unset = UNSET
        if _excluded_agents is not UNSET:
            excluded_agents = []
            for excluded_agents_item_data in _excluded_agents:
                excluded_agents_item = UUID(excluded_agents_item_data)

                excluded_agents.append(excluded_agents_item)

        monitor_locations = cls(
            pools=pools,
            fallback=fallback,
            excluded_agents=excluded_agents,
        )

        monitor_locations.additional_properties = d
        return monitor_locations

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
