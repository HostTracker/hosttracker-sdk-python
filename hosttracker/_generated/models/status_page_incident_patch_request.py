from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.status_page_incident_patch_request_kind import (
    StatusPageIncidentPatchRequestKind,
    check_status_page_incident_patch_request_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageIncidentPatchRequest")


@_attrs_define
class StatusPageIncidentPatchRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    component_ids: list[UUID] | Unset = UNSET
    """ The corrected set of affected components - a replacement, not a diff. """
    kind: StatusPageIncidentPatchRequestKind | Unset = UNSET
    """ A corrected kind. """
    postmortem: None | str | Unset = UNSET
    """ The write-up published after the fact. Send null to clear it. """
    title: str | Unset = UNSET
    """ A corrected title. """

    def to_dict(self) -> dict[str, Any]:
        component_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = []
            for component_ids_item_data in self.component_ids:
                component_ids_item = str(component_ids_item_data)
                component_ids.append(component_ids_item)

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        postmortem: None | str | Unset
        if isinstance(self.postmortem, Unset):
            postmortem = UNSET
        else:
            postmortem = self.postmortem

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if component_ids is not UNSET:
            field_dict["componentIds"] = component_ids
        if kind is not UNSET:
            field_dict["kind"] = kind
        if postmortem is not UNSET:
            field_dict["postmortem"] = postmortem
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _component_ids = d.pop("componentIds", UNSET)
        component_ids: list[UUID] | Unset = UNSET
        if _component_ids is not UNSET:
            component_ids = []
            for component_ids_item_data in _component_ids:
                component_ids_item = UUID(component_ids_item_data)

                component_ids.append(component_ids_item)

        _kind = d.pop("kind", UNSET)
        kind: StatusPageIncidentPatchRequestKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_status_page_incident_patch_request_kind(_kind)

        def _parse_postmortem(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postmortem = _parse_postmortem(d.pop("postmortem", UNSET))

        title = d.pop("title", UNSET)

        status_page_incident_patch_request = cls(
            component_ids=component_ids,
            kind=kind,
            postmortem=postmortem,
            title=title,
        )

        return status_page_incident_patch_request
