from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.status_page_incident_timeline_request_state import (
    StatusPageIncidentTimelineRequestState,
    check_status_page_incident_timeline_request_state,
)

T = TypeVar("T", bound="StatusPageIncidentTimelineRequest")


@_attrs_define
class StatusPageIncidentTimelineRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    message: str
    """ What subscribers are told this time. """
    state: StatusPageIncidentTimelineRequestState
    """ The lifecycle position this entry moves the incident to. `resolved` stamps the resolution time the first
    time it is sent; appending after that reads as a follow-up note. """

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        state: str = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        state = check_status_page_incident_timeline_request_state(d.pop("state"))

        status_page_incident_timeline_request = cls(
            message=message,
            state=state,
        )

        return status_page_incident_timeline_request
