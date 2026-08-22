from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_pool_preset_view import AgentPoolPresetView
    from ..models.agent_pool_summary_view_defaults import AgentPoolSummaryViewDefaults
    from ..models.agent_pool_summary_view_min_agents import AgentPoolSummaryViewMinAgents
    from ..models.agent_pool_summary_view_min_intervals import AgentPoolSummaryViewMinIntervals


T = TypeVar("T", bound="AgentPoolSummaryView")


@_attrs_define
class AgentPoolSummaryView:
    min_agents: AgentPoolSummaryViewMinAgents | Unset = UNSET
    """ The agent minimum a selection must meet, per monitor type plus a `default` key. Published so a client can
    check the count BEFORE submitting and getting `insufficient_agents`. """
    defaults: AgentPoolSummaryViewDefaults | Unset = UNSET
    """ The account's default pool selection per service type, when it has configured one. """
    presets: list[AgentPoolPresetView] | Unset = UNSET
    """ The named presets. """
    min_intervals: AgentPoolSummaryViewMinIntervals | Unset = UNSET
    """ **The shortest interval each monitor type may run at, in SECONDS** - the same floor the create and update
    validators enforce, keyed by monitor type with a `default` entry for every type that has no floor of its own.
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_agents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_agents, Unset):
            min_agents = self.min_agents.to_dict()

        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        presets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.presets, Unset):
            presets = []
            for presets_item_data in self.presets:
                presets_item = presets_item_data.to_dict()
                presets.append(presets_item)

        min_intervals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_intervals, Unset):
            min_intervals = self.min_intervals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_agents is not UNSET:
            field_dict["minAgents"] = min_agents
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if presets is not UNSET:
            field_dict["presets"] = presets
        if min_intervals is not UNSET:
            field_dict["minIntervals"] = min_intervals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_pool_preset_view import AgentPoolPresetView
        from ..models.agent_pool_summary_view_defaults import AgentPoolSummaryViewDefaults
        from ..models.agent_pool_summary_view_min_agents import AgentPoolSummaryViewMinAgents
        from ..models.agent_pool_summary_view_min_intervals import AgentPoolSummaryViewMinIntervals

        d = dict(src_dict)
        _min_agents = d.pop("minAgents", UNSET)
        min_agents: AgentPoolSummaryViewMinAgents | Unset
        if isinstance(_min_agents, Unset):
            min_agents = UNSET
        else:
            min_agents = AgentPoolSummaryViewMinAgents.from_dict(_min_agents)

        _defaults = d.pop("defaults", UNSET)
        defaults: AgentPoolSummaryViewDefaults | Unset
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = AgentPoolSummaryViewDefaults.from_dict(_defaults)

        _presets = d.pop("presets", UNSET)
        presets: list[AgentPoolPresetView] | Unset = UNSET
        if _presets is not UNSET:
            presets = []
            for presets_item_data in _presets:
                presets_item = AgentPoolPresetView.from_dict(presets_item_data)

                presets.append(presets_item)

        _min_intervals = d.pop("minIntervals", UNSET)
        min_intervals: AgentPoolSummaryViewMinIntervals | Unset
        if isinstance(_min_intervals, Unset):
            min_intervals = UNSET
        else:
            min_intervals = AgentPoolSummaryViewMinIntervals.from_dict(_min_intervals)

        agent_pool_summary_view = cls(
            min_agents=min_agents,
            defaults=defaults,
            presets=presets,
            min_intervals=min_intervals,
        )

        agent_pool_summary_view.additional_properties = d
        return agent_pool_summary_view

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
