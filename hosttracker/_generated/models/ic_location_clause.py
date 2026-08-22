from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IcLocationClause")


@_attrs_define
class IcLocationClause:
    """One constraint clause. Its members are ANDed and the values within a member ORed; a clause with no member at all is
    refused.

    """

    countries: list[str] | Unset = UNSET
    """ Match locations in these countries. """
    states: list[str] | Unset = UNSET
    """ Match locations in these states or regions. """
    cities: list[str] | Unset = UNSET
    """ Match locations in these cities. """
    agents: list[UUID] | Unset = UNSET
    """ Match these specific monitoring locations. """
    ips: list[str] | Unset = UNSET
    """ Match locations at these addresses. """

    def to_dict(self) -> dict[str, Any]:
        countries: list[str] | Unset = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        states: list[str] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = self.states

        cities: list[str] | Unset = UNSET
        if not isinstance(self.cities, Unset):
            cities = self.cities

        agents: list[str] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = str(agents_item_data)
                agents.append(agents_item)

        ips: list[str] | Unset = UNSET
        if not isinstance(self.ips, Unset):
            ips = self.ips

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if countries is not UNSET:
            field_dict["countries"] = countries
        if states is not UNSET:
            field_dict["states"] = states
        if cities is not UNSET:
            field_dict["cities"] = cities
        if agents is not UNSET:
            field_dict["agents"] = agents
        if ips is not UNSET:
            field_dict["ips"] = ips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        countries = cast(list[str], d.pop("countries", UNSET))

        states = cast(list[str], d.pop("states", UNSET))

        cities = cast(list[str], d.pop("cities", UNSET))

        _agents = d.pop("agents", UNSET)
        agents: list[UUID] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = UUID(agents_item_data)

                agents.append(agents_item)

        ips = cast(list[str], d.pop("ips", UNSET))

        ic_location_clause = cls(
            countries=countries,
            states=states,
            cities=cities,
            agents=agents,
            ips=ips,
        )

        return ic_location_clause
