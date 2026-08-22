from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.status_page_subscriber_write_request_kind import (
    StatusPageSubscriberWriteRequestKind,
    check_status_page_subscriber_write_request_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageSubscriberWriteRequest")


@_attrs_define
class StatusPageSubscriberWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    kind: StatusPageSubscriberWriteRequestKind
    """ Which channel to deliver through. An EMAIL subscriber cannot be added here by design - an address joins only
    through the public page's own double opt-in. """
    url: str
    """ Where updates are posted - the channel's absolute http(s) endpoint. """
    component_id: UUID | Unset = UNSET
    """ Deliver only updates affecting this one component. Absent means every update on the page. """

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        url = self.url

        component_id: str | Unset = UNSET
        if not isinstance(self.component_id, Unset):
            component_id = str(self.component_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "url": url,
            }
        )
        if component_id is not UNSET:
            field_dict["componentId"] = component_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_status_page_subscriber_write_request_kind(d.pop("kind"))

        url = d.pop("url")

        _component_id = d.pop("componentId", UNSET)
        component_id: UUID | Unset
        if isinstance(_component_id, Unset):
            component_id = UNSET
        else:
            component_id = UUID(_component_id)

        status_page_subscriber_write_request = cls(
            kind=kind,
            url=url,
            component_id=component_id,
        )

        return status_page_subscriber_write_request
