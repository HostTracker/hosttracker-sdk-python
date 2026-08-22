from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSpanView")


@_attrs_define
class MonitorSpanView:
    """One up/down span, clipped to nothing - the raw stored boundaries, in Unix seconds."""

    from_: int
    """ Unix seconds. """
    to: int
    """ Unix seconds. """
    up: bool
    """ True for an UP span, false for a DOWN one. """
    event_count: int
    first_check_number: int
    """ The check number the span OPENS at - the first check that saw this state. """
    last_check_number: int
    """ The check number the span ENDS at. For the still-open span this is the newest check so far, so it moves;
    `firstCheckNumber` never does. """
    incident_id: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    """ The note left on this span (`POST /monitor/incident/{id}/comment`), when it has one. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        up = self.up

        event_count = self.event_count

        first_check_number = self.first_check_number

        last_check_number = self.last_check_number

        incident_id: None | str | Unset
        if isinstance(self.incident_id, Unset):
            incident_id = UNSET
        else:
            incident_id = self.incident_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "up": up,
                "eventCount": event_count,
                "firstCheckNumber": first_check_number,
                "lastCheckNumber": last_check_number,
            }
        )
        if incident_id is not UNSET:
            field_dict["incidentId"] = incident_id
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        up = d.pop("up")

        event_count = d.pop("eventCount")

        first_check_number = d.pop("firstCheckNumber")

        last_check_number = d.pop("lastCheckNumber")

        def _parse_incident_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incident_id = _parse_incident_id(d.pop("incidentId", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        monitor_span_view = cls(
            from_=from_,
            to=to,
            up=up,
            event_count=event_count,
            first_check_number=first_check_number,
            last_check_number=last_check_number,
            incident_id=incident_id,
            comment=comment,
        )

        monitor_span_view.additional_properties = d
        return monitor_span_view

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
