from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.status_page_component import StatusPageComponent


T = TypeVar("T", bound="StatusPageComponentSetRequest")


@_attrs_define
class StatusPageComponentSetRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    components: list[StatusPageComponent]
    """ Every component to keep, in display order. This is a SNAPSHOT, not a diff: a component the array omits is
    removed. Carry each existing row's `id` so its per-component subscriptions survive the save. """

    def to_dict(self) -> dict[str, Any]:
        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_component import StatusPageComponent

        d = dict(src_dict)
        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = StatusPageComponent.from_dict(components_item_data)

            components.append(components_item)

        status_page_component_set_request = cls(
            components=components,
        )

        return status_page_component_set_request
