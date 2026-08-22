from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_component_row import StatusPageComponentRow
    from ..models.status_page_settings_view import StatusPageSettingsView


T = TypeVar("T", bound="StatusPageView")


@_attrs_define
class StatusPageView:
    """The full page - everything the list row carries, plus the `settings` object and the component set. **A superset of
    the list row, deliberately**. It used to carry FEWER members than the row it details: `created`, `componentCount`
    and `unresolvedIncidents` were listed and then disappeared on the item read, so a client that rendered a list and
    then opened one page had to keep the list row to redraw the same fields - and a client that read a page it had just
    created had no way to get them at all. An item read is the FULLER view of a row by definition; anything else is a
    shape a caller has to special-case.

    """

    id: UUID
    component_count: int
    """ How many components the page publishes - the same count the list row carries. """
    unresolved_incidents: int
    """ How many of the page's declared incidents are still open (any status but resolved), so a page that is
    currently reporting trouble is visible without a second read. """
    has_password: bool
    created: int
    """ When the page was created, Unix seconds. Unix seconds. """
    slug: str | Unset = UNSET
    title: str | Unset = UNSET
    settings: StatusPageSettingsView | Unset = UNSET
    """ The page's appearance + behaviour block - every member owner-writable through the PATCH. """
    components: list[StatusPageComponentRow] | Unset = UNSET
    custom_domain: None | str | Unset = UNSET
    """ The custom domain as CONFIGURED, when one is - activation is Cloudflare bookkeeping the dashboard owns; the
    member is informational here. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        component_count = self.component_count

        unresolved_incidents = self.unresolved_incidents

        has_password = self.has_password

        created = self.created

        slug = self.slug

        title = self.title

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        custom_domain: None | str | Unset
        if isinstance(self.custom_domain, Unset):
            custom_domain = UNSET
        else:
            custom_domain = self.custom_domain

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
        if settings is not UNSET:
            field_dict["settings"] = settings
        if components is not UNSET:
            field_dict["components"] = components
        if custom_domain is not UNSET:
            field_dict["customDomain"] = custom_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_component_row import StatusPageComponentRow
        from ..models.status_page_settings_view import StatusPageSettingsView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        component_count = d.pop("componentCount")

        unresolved_incidents = d.pop("unresolvedIncidents")

        has_password = d.pop("hasPassword")

        created = d.pop("created")

        slug = d.pop("slug", UNSET)

        title = d.pop("title", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: StatusPageSettingsView | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = StatusPageSettingsView.from_dict(_settings)

        _components = d.pop("components", UNSET)
        components: list[StatusPageComponentRow] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = StatusPageComponentRow.from_dict(components_item_data)

                components.append(components_item)

        def _parse_custom_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_domain = _parse_custom_domain(d.pop("customDomain", UNSET))

        status_page_view = cls(
            id=id,
            component_count=component_count,
            unresolved_incidents=unresolved_incidents,
            has_password=has_password,
            created=created,
            slug=slug,
            title=title,
            settings=settings,
            components=components,
            custom_domain=custom_domain,
        )

        status_page_view.additional_properties = d
        return status_page_view

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
