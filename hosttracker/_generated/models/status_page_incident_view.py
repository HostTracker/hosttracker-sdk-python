from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_incident_view_impact import (
    StatusPageIncidentViewImpact,
    check_status_page_incident_view_impact,
)
from ..models.status_page_incident_view_kind import StatusPageIncidentViewKind, check_status_page_incident_view_kind
from ..models.status_page_incident_view_state import StatusPageIncidentViewState, check_status_page_incident_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_incident_timeline_entry_view import StatusPageIncidentTimelineEntryView


T = TypeVar("T", bound="StatusPageIncidentView")


@_attrs_define
class StatusPageIncidentView:
    """One declared incident, with its append-only update timeline."""

    id: UUID
    created: int
    """ Unix seconds. """
    title: str | Unset = UNSET
    state: StatusPageIncidentViewState | Unset = UNSET
    """ `investigating` | `identified` | `monitoring` | `resolved` - where the incident is in its lifecycle. """
    kind: StatusPageIncidentViewKind | Unset = UNSET
    impact: StatusPageIncidentViewImpact | Unset = UNSET
    resolved_at: int | None | Unset = UNSET
    """ Unix seconds. """
    scheduled_start: int | None | Unset = UNSET
    """ Unix seconds. """
    scheduled_end: int | None | Unset = UNSET
    """ Unix seconds. """
    component_ids: list[UUID] | Unset = UNSET
    component_names: list[str] | Unset = UNSET
    """ The affected components' NAMES, positionally matching `componentIds` - so a reader need not join against the
    page to render the incident. """
    postmortem: None | str | Unset = UNSET
    timeline: list[StatusPageIncidentTimelineEntryView] | Unset = UNSET
    """ The append-only timeline, oldest first - the same resource `POST .../incident/{incidentId}/timeline` appends
    to. Named for what it IS rather than for the verb that grows it, so the collection and its own write door share
    one word. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created = self.created

        title = self.title

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        impact: str | Unset = UNSET
        if not isinstance(self.impact, Unset):
            impact = self.impact

        resolved_at: int | None | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        scheduled_start: int | None | Unset
        if isinstance(self.scheduled_start, Unset):
            scheduled_start = UNSET
        else:
            scheduled_start = self.scheduled_start

        scheduled_end: int | None | Unset
        if isinstance(self.scheduled_end, Unset):
            scheduled_end = UNSET
        else:
            scheduled_end = self.scheduled_end

        component_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = []
            for component_ids_item_data in self.component_ids:
                component_ids_item = str(component_ids_item_data)
                component_ids.append(component_ids_item)

        component_names: list[str] | Unset = UNSET
        if not isinstance(self.component_names, Unset):
            component_names = self.component_names

        postmortem: None | str | Unset
        if isinstance(self.postmortem, Unset):
            postmortem = UNSET
        else:
            postmortem = self.postmortem

        timeline: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timeline, Unset):
            timeline = []
            for timeline_item_data in self.timeline:
                timeline_item = timeline_item_data.to_dict()
                timeline.append(timeline_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if state is not UNSET:
            field_dict["state"] = state
        if kind is not UNSET:
            field_dict["kind"] = kind
        if impact is not UNSET:
            field_dict["impact"] = impact
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if scheduled_start is not UNSET:
            field_dict["scheduledStart"] = scheduled_start
        if scheduled_end is not UNSET:
            field_dict["scheduledEnd"] = scheduled_end
        if component_ids is not UNSET:
            field_dict["componentIds"] = component_ids
        if component_names is not UNSET:
            field_dict["componentNames"] = component_names
        if postmortem is not UNSET:
            field_dict["postmortem"] = postmortem
        if timeline is not UNSET:
            field_dict["timeline"] = timeline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_incident_timeline_entry_view import StatusPageIncidentTimelineEntryView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = d.pop("created")

        title = d.pop("title", UNSET)

        _state = d.pop("state", UNSET)
        state: StatusPageIncidentViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_status_page_incident_view_state(_state)

        _kind = d.pop("kind", UNSET)
        kind: StatusPageIncidentViewKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_status_page_incident_view_kind(_kind)

        _impact = d.pop("impact", UNSET)
        impact: StatusPageIncidentViewImpact | Unset
        if isinstance(_impact, Unset):
            impact = UNSET
        else:
            impact = check_status_page_incident_view_impact(_impact)

        def _parse_resolved_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt", UNSET))

        def _parse_scheduled_start(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scheduled_start = _parse_scheduled_start(d.pop("scheduledStart", UNSET))

        def _parse_scheduled_end(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scheduled_end = _parse_scheduled_end(d.pop("scheduledEnd", UNSET))

        _component_ids = d.pop("componentIds", UNSET)
        component_ids: list[UUID] | Unset = UNSET
        if _component_ids is not UNSET:
            component_ids = []
            for component_ids_item_data in _component_ids:
                component_ids_item = UUID(component_ids_item_data)

                component_ids.append(component_ids_item)

        component_names = cast(list[str], d.pop("componentNames", UNSET))

        def _parse_postmortem(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postmortem = _parse_postmortem(d.pop("postmortem", UNSET))

        _timeline = d.pop("timeline", UNSET)
        timeline: list[StatusPageIncidentTimelineEntryView] | Unset = UNSET
        if _timeline is not UNSET:
            timeline = []
            for timeline_item_data in _timeline:
                timeline_item = StatusPageIncidentTimelineEntryView.from_dict(timeline_item_data)

                timeline.append(timeline_item)

        status_page_incident_view = cls(
            id=id,
            created=created,
            title=title,
            state=state,
            kind=kind,
            impact=impact,
            resolved_at=resolved_at,
            scheduled_start=scheduled_start,
            scheduled_end=scheduled_end,
            component_ids=component_ids,
            component_names=component_names,
            postmortem=postmortem,
            timeline=timeline,
        )

        status_page_incident_view.additional_properties = d
        return status_page_incident_view

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
