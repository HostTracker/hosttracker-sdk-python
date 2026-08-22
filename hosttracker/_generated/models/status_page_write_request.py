from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_component import StatusPageComponent
    from ..models.status_page_settings import StatusPageSettings


T = TypeVar("T", bound="StatusPageWriteRequest")


@_attrs_define
class StatusPageWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    slug: str
    """ The page's permanent public address - lowercase letters, digits and single hyphens, unique across the
    product, and not changeable afterwards. """
    title: str
    """ The heading the public page carries. """
    components: list[StatusPageComponent] | Unset = UNSET
    """ The page's initial components, in display order. The same shape the component-set endpoint takes, so a page
    can be created complete in one call. """
    settings: StatusPageSettings | Unset = UNSET
    """ How the public page looks and behaves. Only the members you send change; an explicit null clears a clearable
    one. """

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        title = self.title

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
                "title": title,
            }
        )
        if components is not UNSET:
            field_dict["components"] = components
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_component import StatusPageComponent
        from ..models.status_page_settings import StatusPageSettings

        d = dict(src_dict)
        slug = d.pop("slug")

        title = d.pop("title")

        _components = d.pop("components", UNSET)
        components: list[StatusPageComponent] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = StatusPageComponent.from_dict(components_item_data)

                components.append(components_item)

        _settings = d.pop("settings", UNSET)
        settings: StatusPageSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = StatusPageSettings.from_dict(_settings)

        status_page_write_request = cls(
            slug=slug,
            title=title,
            components=components,
            settings=settings,
        )

        return status_page_write_request
