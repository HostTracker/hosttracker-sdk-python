from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_incident_delete_cascade import StatusPageIncidentDeleteCascade


T = TypeVar("T", bound="StatusPageIncidentDeleteReceipt")


@_attrs_define
class StatusPageIncidentDeleteReceipt:
    """The receipt a declared-incident delete answers with. Its cascade is the timeline: an incident IS its timeline, and
    deleting it removes every entry.

    """

    id: UUID
    deleted: bool
    type_: str | Unset = UNSET
    title: None | str | Unset = UNSET
    cascaded: StatusPageIncidentDeleteCascade | Unset = UNSET
    """ What went with the incident. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deleted = self.deleted

        type_ = self.type_

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        cascaded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cascaded, Unset):
            cascaded = self.cascaded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deleted": deleted,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if cascaded is not UNSET:
            field_dict["cascaded"] = cascaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_incident_delete_cascade import StatusPageIncidentDeleteCascade

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deleted = d.pop("deleted")

        type_ = d.pop("type", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _cascaded = d.pop("cascaded", UNSET)
        cascaded: StatusPageIncidentDeleteCascade | Unset
        if isinstance(_cascaded, Unset):
            cascaded = UNSET
        else:
            cascaded = StatusPageIncidentDeleteCascade.from_dict(_cascaded)

        status_page_incident_delete_receipt = cls(
            id=id,
            deleted=deleted,
            type_=type_,
            title=title,
            cascaded=cascaded,
        )

        status_page_incident_delete_receipt.additional_properties = d
        return status_page_incident_delete_receipt

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
