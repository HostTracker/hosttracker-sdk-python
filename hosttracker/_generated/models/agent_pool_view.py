from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_pool_view_agents import AgentPoolViewAgents


T = TypeVar("T", bound="AgentPoolView")


@_attrs_define
class AgentPoolView:
    hidden: bool
    """ **Whether this pool is offered in a picker.** Hidden pools are real and selectable - a monitor can be pinned
    to one and the fleet honours it - they are simply not advertised in the tree a UI builds. They are listed only
    for an IDENTIFIED caller. The anonymous reference tier gets the advertised tree, where every row answers
    `false`; a credential adds the hidden rows, each saying so. That keeps a token from being a way to enumerate
    infrastructure nobody is meant to browse, while a client that renders the tree for a signed-in user can still
    show - and re-save - the pool that user's monitor is actually pinned to. Without them, opening such a monitor in
    an editor and saving it dropped the pin, because the pool was not in the tree the editor had loaded. """
    priority: int
    """ The pool's ordering weight - ascending, and the order the rows arrive in. It is what a picker sorts its tree
    by, so a client that re-sorts alphabetically loses the curation deliberately. """
    id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    agents: AgentPoolViewAgents | Unset = UNSET
    """ Agents per service type - `{ "net": 214, "waterfall": 12 }`, parents populated. """
    children: list[str] | Unset = UNSET
    """ Nested pool ids. """
    parents: list[str] | Unset = UNSET
    """ Pools that contain this one. """
    agent_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hidden = self.hidden

        priority = self.priority

        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        agents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = self.agents.to_dict()

        children: list[str] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children

        parents: list[str] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = self.parents

        agent_ids: list[str] | Unset = UNSET
        if not isinstance(self.agent_ids, Unset):
            agent_ids = []
            for agent_ids_item_data in self.agent_ids:
                agent_ids_item = str(agent_ids_item_data)
                agent_ids.append(agent_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hidden": hidden,
                "priority": priority,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if agents is not UNSET:
            field_dict["agents"] = agents
        if children is not UNSET:
            field_dict["children"] = children
        if parents is not UNSET:
            field_dict["parents"] = parents
        if agent_ids is not UNSET:
            field_dict["agentIds"] = agent_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_pool_view_agents import AgentPoolViewAgents

        d = dict(src_dict)
        hidden = d.pop("hidden")

        priority = d.pop("priority")

        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _agents = d.pop("agents", UNSET)
        agents: AgentPoolViewAgents | Unset
        if isinstance(_agents, Unset):
            agents = UNSET
        else:
            agents = AgentPoolViewAgents.from_dict(_agents)

        children = cast(list[str], d.pop("children", UNSET))

        parents = cast(list[str], d.pop("parents", UNSET))

        _agent_ids = d.pop("agentIds", UNSET)
        agent_ids: list[UUID] | Unset = UNSET
        if _agent_ids is not UNSET:
            agent_ids = []
            for agent_ids_item_data in _agent_ids:
                agent_ids_item = UUID(agent_ids_item_data)

                agent_ids.append(agent_ids_item)

        agent_pool_view = cls(
            hidden=hidden,
            priority=priority,
            id=id,
            name=name,
            agents=agents,
            children=children,
            parents=parents,
            agent_ids=agent_ids,
        )

        agent_pool_view.additional_properties = d
        return agent_pool_view

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
