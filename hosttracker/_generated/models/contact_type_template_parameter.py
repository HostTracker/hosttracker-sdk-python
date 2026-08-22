from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactTypeTemplateParameter")


@_attrs_define
class ContactTypeTemplateParameter:
    """One token a custom template body may contain."""

    name: str | Unset = UNSET
    """ The token's name, written `[[name]]` in the template body. """
    description: str | Unset = UNSET
    """ What the renderer substitutes for it. """
    events: list[str] | Unset = UNSET
    """ The alert types the token resolves on; the others render it blank. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        contact_type_template_parameter = cls(
            name=name,
            description=description,
            events=events,
        )

        contact_type_template_parameter.additional_properties = d
        return contact_type_template_parameter

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
