from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusPageDeleteCascade")


@_attrs_define
class StatusPageDeleteCascade:
    """What went with the page. Counted BEFORE the delete runs - the store removes the rows and reports nothing, so this is
    the caller's only chance to learn it.

    """

    components: int
    """ The components the page published, monitored and third-party alike. """
    incidents: int
    """ The incidents and maintenances declared on the page, with their timelines. """
    subscribers: int
    """ The subscribers who were following the page - email addresses and push channels together. They are not
    notified, and an email subscriber would have to opt in again. """
    templates: int
    """ The saved incident templates. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components = self.components

        incidents = self.incidents

        subscribers = self.subscribers

        templates = self.templates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
                "incidents": incidents,
                "subscribers": subscribers,
                "templates": templates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        components = d.pop("components")

        incidents = d.pop("incidents")

        subscribers = d.pop("subscribers")

        templates = d.pop("templates")

        status_page_delete_cascade = cls(
            components=components,
            incidents=incidents,
            subscribers=subscribers,
            templates=templates,
        )

        status_page_delete_cascade.additional_properties = d
        return status_page_delete_cascade

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
