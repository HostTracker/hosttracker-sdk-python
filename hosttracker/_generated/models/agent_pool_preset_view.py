from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentPoolPresetView")


@_attrs_define
class AgentPoolPresetView:
    """**A named location preset** - the fold-in of v1's separately-served `GET /Sites/location-profiles`. A "preset" is
    not a stored entity: it is a DISTINCT pool selection the account already uses on one of its monitors, named after
    that monitor. Selections used by several monitors appear ONCE (deduplicated on the pool-id set), named after the
    first of them - v1 returns one row per monitor, which for an account that applies one selection to 300 monitors is
    300 identical rows.

    """

    id: UUID
    """ The monitor the preset is named after. """
    monitors: int
    """ How many of the account's monitors use exactly this selection. """
    name: None | str | Unset = UNSET
    pool_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        monitors = self.monitors

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        pool_ids: list[str] | Unset = UNSET
        if not isinstance(self.pool_ids, Unset):
            pool_ids = self.pool_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "monitors": monitors,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if pool_ids is not UNSET:
            field_dict["poolIds"] = pool_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        monitors = d.pop("monitors")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        pool_ids = cast(list[str], d.pop("poolIds", UNSET))

        agent_pool_preset_view = cls(
            id=id,
            monitors=monitors,
            name=name,
            pool_ids=pool_ids,
        )

        agent_pool_preset_view.additional_properties = d
        return agent_pool_preset_view

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
