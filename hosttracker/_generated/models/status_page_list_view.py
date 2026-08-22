from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageListView")


@_attrs_define
class StatusPageListView:
    id: UUID
    component_count: int
    unresolved_incidents: int
    has_password: bool
    created: int
    """ Unix seconds. """
    slug: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        component_count = self.component_count

        unresolved_incidents = self.unresolved_incidents

        has_password = self.has_password

        created = self.created

        slug = self.slug

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "componentCount": component_count,
                "unresolvedIncidents": unresolved_incidents,
                "hasPassword": has_password,
                "created": created,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        component_count = d.pop("componentCount")

        unresolved_incidents = d.pop("unresolvedIncidents")

        has_password = d.pop("hasPassword")

        created = d.pop("created")

        slug = d.pop("slug", UNSET)

        title = d.pop("title", UNSET)

        status_page_list_view = cls(
            id=id,
            component_count=component_count,
            unresolved_incidents=unresolved_incidents,
            has_password=has_password,
            created=created,
            slug=slug,
            title=title,
        )

        status_page_list_view.additional_properties = d
        return status_page_list_view

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
