from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_template_view_default_impact import (
    StatusPageTemplateViewDefaultImpact,
    check_status_page_template_view_default_impact,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageTemplateView")


@_attrs_define
class StatusPageTemplateView:
    """One incident template."""

    id: UUID
    created: int
    """ Unix seconds. """
    title: str | Unset = UNSET
    message: str | Unset = UNSET
    default_impact: StatusPageTemplateViewDefaultImpact | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created = self.created

        title = self.title

        message = self.message

        default_impact: str | Unset = UNSET
        if not isinstance(self.default_impact, Unset):
            default_impact = self.default_impact

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
        if message is not UNSET:
            field_dict["message"] = message
        if default_impact is not UNSET:
            field_dict["defaultImpact"] = default_impact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = d.pop("created")

        title = d.pop("title", UNSET)

        message = d.pop("message", UNSET)

        _default_impact = d.pop("defaultImpact", UNSET)
        default_impact: StatusPageTemplateViewDefaultImpact | Unset
        if isinstance(_default_impact, Unset):
            default_impact = UNSET
        else:
            default_impact = check_status_page_template_view_default_impact(_default_impact)

        status_page_template_view = cls(
            id=id,
            created=created,
            title=title,
            message=message,
            default_impact=default_impact,
        )

        status_page_template_view.additional_properties = d
        return status_page_template_view

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
