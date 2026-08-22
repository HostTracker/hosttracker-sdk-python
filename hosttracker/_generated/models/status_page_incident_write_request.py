from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.status_page_incident_write_request_impact import (
    StatusPageIncidentWriteRequestImpact,
    check_status_page_incident_write_request_impact,
)
from ..models.status_page_incident_write_request_kind import (
    StatusPageIncidentWriteRequestKind,
    check_status_page_incident_write_request_kind,
)
from ..models.status_page_incident_write_request_state import (
    StatusPageIncidentWriteRequestState,
    check_status_page_incident_write_request_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageIncidentWriteRequest")


@_attrs_define
class StatusPageIncidentWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    message: str
    """ The first timeline entry's text - what subscribers are told. """
    state: StatusPageIncidentWriteRequestState
    """ Where the incident starts in its lifecycle. It seeds the timeline with `message`; progress is reported by
    appending further timeline entries, never by patching this. """
    title: str
    """ What is happening, in one line. """
    component_ids: list[UUID] | Unset = UNSET
    """ Which of THIS page's components are affected. It also scopes the subscriber notification. """
    impact: StatusPageIncidentWriteRequestImpact | Unset = UNSET
    """ How badly the service is affected. Defaults to `minor`. """
    kind: StatusPageIncidentWriteRequestKind | Unset = UNSET
    """ Whether this is an unplanned incident or a scheduled maintenance. `maintenance` is what makes the scheduled
    window meaningful. Defaults to `incident`. """
    scheduled_end: int | Unset = UNSET
    """ When a scheduled maintenance ends, in Unix seconds. Must be after `scheduledStart`. """
    scheduled_start: int | Unset = UNSET
    """ When a scheduled maintenance begins, in Unix seconds. On `kind: maintenance` it is sent together with
    `scheduledEnd` or not at all. """

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        state: str = self.state

        title = self.title

        component_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = []
            for component_ids_item_data in self.component_ids:
                component_ids_item = str(component_ids_item_data)
                component_ids.append(component_ids_item)

        impact: str | Unset = UNSET
        if not isinstance(self.impact, Unset):
            impact = self.impact

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        scheduled_end = self.scheduled_end

        scheduled_start = self.scheduled_start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
                "state": state,
                "title": title,
            }
        )
        if component_ids is not UNSET:
            field_dict["componentIds"] = component_ids
        if impact is not UNSET:
            field_dict["impact"] = impact
        if kind is not UNSET:
            field_dict["kind"] = kind
        if scheduled_end is not UNSET:
            field_dict["scheduledEnd"] = scheduled_end
        if scheduled_start is not UNSET:
            field_dict["scheduledStart"] = scheduled_start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        state = check_status_page_incident_write_request_state(d.pop("state"))

        title = d.pop("title")

        _component_ids = d.pop("componentIds", UNSET)
        component_ids: list[UUID] | Unset = UNSET
        if _component_ids is not UNSET:
            component_ids = []
            for component_ids_item_data in _component_ids:
                component_ids_item = UUID(component_ids_item_data)

                component_ids.append(component_ids_item)

        _impact = d.pop("impact", UNSET)
        impact: StatusPageIncidentWriteRequestImpact | Unset
        if isinstance(_impact, Unset):
            impact = UNSET
        else:
            impact = check_status_page_incident_write_request_impact(_impact)

        _kind = d.pop("kind", UNSET)
        kind: StatusPageIncidentWriteRequestKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_status_page_incident_write_request_kind(_kind)

        scheduled_end = d.pop("scheduledEnd", UNSET)

        scheduled_start = d.pop("scheduledStart", UNSET)

        status_page_incident_write_request = cls(
            message=message,
            state=state,
            title=title,
            component_ids=component_ids,
            impact=impact,
            kind=kind,
            scheduled_end=scheduled_end,
            scheduled_start=scheduled_start,
        )

        return status_page_incident_write_request
