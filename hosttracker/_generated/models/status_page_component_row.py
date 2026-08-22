from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_component_row_manual_state import (
    StatusPageComponentRowManualState,
    check_status_page_component_row_manual_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageComponentRow")


@_attrs_define
class StatusPageComponentRow:
    """One component row - the array's ORDER is the display order."""

    id: UUID
    third_party: bool
    monitor_id: None | Unset | UUID = UNSET
    """ The monitored task, or null for a third-party component. """
    name: str | Unset = UNSET
    """ The component's display name. `name`, not `label`: a component is an ENTITY on this page and every entity
    here carries a `name` (`label` stays the word for a catalogue ROW - a monitor type, a contact type - which is a
    choice a client renders, not a thing it owns). """
    group: None | str | Unset = UNSET
    manual_state: StatusPageComponentRowManualState | Unset = UNSET
    """ `operational` | `degraded` | `down` - the state an owner pins on a THIRD-PARTY component by hand (a
    monitored one takes its state from its checks). Absent when nothing is pinned. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        third_party = self.third_party

        monitor_id: None | str | Unset
        if isinstance(self.monitor_id, Unset):
            monitor_id = UNSET
        elif isinstance(self.monitor_id, UUID):
            monitor_id = str(self.monitor_id)
        else:
            monitor_id = self.monitor_id

        name = self.name

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        manual_state: str | Unset = UNSET
        if not isinstance(self.manual_state, Unset):
            manual_state = self.manual_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "thirdParty": third_party,
            }
        )
        if monitor_id is not UNSET:
            field_dict["monitorId"] = monitor_id
        if name is not UNSET:
            field_dict["name"] = name
        if group is not UNSET:
            field_dict["group"] = group
        if manual_state is not UNSET:
            field_dict["manualState"] = manual_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        third_party = d.pop("thirdParty")

        def _parse_monitor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                monitor_id_type_0 = UUID(data)

                return monitor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        monitor_id = _parse_monitor_id(d.pop("monitorId", UNSET))

        name = d.pop("name", UNSET)

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))

        _manual_state = d.pop("manualState", UNSET)
        manual_state: StatusPageComponentRowManualState | Unset
        if isinstance(_manual_state, Unset):
            manual_state = UNSET
        else:
            manual_state = check_status_page_component_row_manual_state(_manual_state)

        status_page_component_row = cls(
            id=id,
            third_party=third_party,
            monitor_id=monitor_id,
            name=name,
            group=group,
            manual_state=manual_state,
        )

        status_page_component_row.additional_properties = d
        return status_page_component_row

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
