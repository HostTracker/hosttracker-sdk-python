from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.status_page_component_manual_state import (
    StatusPageComponentManualState,
    check_status_page_component_manual_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageComponent")


@_attrs_define
class StatusPageComponent:
    """One component. A component is either MONITORED (it names a `monitorId`, which must be the account's own, and its
    state comes from that monitor's checks) or THIRD-PARTY (`thirdParty: true`, its own `name`, and an optional
    `manualState` the owner pins by hand). Sending the members of both is refused rather than resolved.

    """

    id: UUID | Unset = UNSET
    """ The existing row's id. Carry it so per-component subscriptions survive the save; omit it to add a new
    component. """
    monitor_id: UUID | Unset = UNSET
    """ The monitor whose state this component shows. Required unless `thirdParty`. """
    third_party: bool | Unset = UNSET
    """ True for a component this account does not monitor - a dependency you report on by hand. """
    name: str | Unset = UNSET
    """ The label shown on the page. Required on a third-party component; a monitored one inherits its monitor's
    name when this is absent. """
    group: str | Unset = UNSET
    """ The heading this component is listed under. Components with no group are listed first. """
    manual_state: StatusPageComponentManualState | Unset = UNSET
    """ The state to pin on a THIRD-PARTY component. A monitored component's state comes from its checks and this is
    refused there. """

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        monitor_id: str | Unset = UNSET
        if not isinstance(self.monitor_id, Unset):
            monitor_id = str(self.monitor_id)

        third_party = self.third_party

        name = self.name

        group = self.group

        manual_state: str | Unset = UNSET
        if not isinstance(self.manual_state, Unset):
            manual_state = self.manual_state

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if monitor_id is not UNSET:
            field_dict["monitorId"] = monitor_id
        if third_party is not UNSET:
            field_dict["thirdParty"] = third_party
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
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _monitor_id = d.pop("monitorId", UNSET)
        monitor_id: UUID | Unset
        if isinstance(_monitor_id, Unset):
            monitor_id = UNSET
        else:
            monitor_id = UUID(_monitor_id)

        third_party = d.pop("thirdParty", UNSET)

        name = d.pop("name", UNSET)

        group = d.pop("group", UNSET)

        _manual_state = d.pop("manualState", UNSET)
        manual_state: StatusPageComponentManualState | Unset
        if isinstance(_manual_state, Unset):
            manual_state = UNSET
        else:
            manual_state = check_status_page_component_manual_state(_manual_state)

        status_page_component = cls(
            id=id,
            monitor_id=monitor_id,
            third_party=third_party,
            name=name,
            group=group,
            manual_state=manual_state,
        )

        return status_page_component
