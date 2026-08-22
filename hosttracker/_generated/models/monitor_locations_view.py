from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorLocationsView")


@_attrs_define
class MonitorLocationsView:
    """Where a monitor is checked from. Folds in `GET /Sites/{id}/agents/excluded`."""

    pools: list[str] | Unset = UNSET
    """ The agent pools. An empty stored value means "everywhere", which the wire spells `["allworld"]` rather than
    `[]` - the same normalisation the current surface performs, so the two agree. """
    fallback: None | str | Unset = UNSET
    """ `geo` | `world` | `starve` - what happens when the selected locations have no available agent. Absent means
    "use the service default"; a default is never written into storage, so it is never invented here either. """
    excluded_agents: list[UUID] | Unset = UNSET
    """ Agents explicitly excluded from this monitor's checks. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pools: list[str] | Unset = UNSET
        if not isinstance(self.pools, Unset):
            pools = self.pools

        fallback: None | str | Unset
        if isinstance(self.fallback, Unset):
            fallback = UNSET
        else:
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

        def _parse_fallback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fallback = _parse_fallback(d.pop("fallback", UNSET))

        _excluded_agents = d.pop("excludedAgents", UNSET)
        excluded_agents: list[UUID] | Unset = UNSET
        if _excluded_agents is not UNSET:
            excluded_agents = []
            for excluded_agents_item_data in _excluded_agents:
                excluded_agents_item = UUID(excluded_agents_item_data)

                excluded_agents.append(excluded_agents_item)

        monitor_locations_view = cls(
            pools=pools,
            fallback=fallback,
            excluded_agents=excluded_agents,
        )

        monitor_locations_view.additional_properties = d
        return monitor_locations_view

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
