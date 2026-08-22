from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_settings_view_density import (
    StatusPageSettingsViewDensity,
    check_status_page_settings_view_density,
)
from ..models.status_page_settings_view_features_item import (
    StatusPageSettingsViewFeaturesItem,
    check_status_page_settings_view_features_item,
)
from ..models.status_page_settings_view_logo_alignment import (
    StatusPageSettingsViewLogoAlignment,
    check_status_page_settings_view_logo_alignment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageSettingsView")


@_attrs_define
class StatusPageSettingsView:
    """The page's appearance + behaviour block - every member owner-writable through the PATCH."""

    show_groups: bool
    robots_index: bool
    hide_branding: bool
    auto_add_monitors: bool
    homepage_url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    dark_logo_url: None | str | Unset = UNSET
    favicon_url: None | str | Unset = UNSET
    theme: None | str | Unset = UNSET
    theme_color: None | str | Unset = UNSET
    header_bg_color: None | str | Unset = UNSET
    header_text_color: None | str | Unset = UNSET
    announcement: None | str | Unset = UNSET
    density: StatusPageSettingsViewDensity | Unset = UNSET
    logo_alignment: StatusPageSettingsViewLogoAlignment | Unset = UNSET
    language: None | str | Unset = UNSET
    google_analytics_id: None | str | Unset = UNSET
    features: list[StatusPageSettingsViewFeaturesItem] | Unset = UNSET
    sla_target: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        show_groups = self.show_groups

        robots_index = self.robots_index

        hide_branding = self.hide_branding

        auto_add_monitors = self.auto_add_monitors

        homepage_url: None | str | Unset
        if isinstance(self.homepage_url, Unset):
            homepage_url = UNSET
        else:
            homepage_url = self.homepage_url

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        dark_logo_url: None | str | Unset
        if isinstance(self.dark_logo_url, Unset):
            dark_logo_url = UNSET
        else:
            dark_logo_url = self.dark_logo_url

        favicon_url: None | str | Unset
        if isinstance(self.favicon_url, Unset):
            favicon_url = UNSET
        else:
            favicon_url = self.favicon_url

        theme: None | str | Unset
        if isinstance(self.theme, Unset):
            theme = UNSET
        else:
            theme = self.theme

        theme_color: None | str | Unset
        if isinstance(self.theme_color, Unset):
            theme_color = UNSET
        else:
            theme_color = self.theme_color

        header_bg_color: None | str | Unset
        if isinstance(self.header_bg_color, Unset):
            header_bg_color = UNSET
        else:
            header_bg_color = self.header_bg_color

        header_text_color: None | str | Unset
        if isinstance(self.header_text_color, Unset):
            header_text_color = UNSET
        else:
            header_text_color = self.header_text_color

        announcement: None | str | Unset
        if isinstance(self.announcement, Unset):
            announcement = UNSET
        else:
            announcement = self.announcement

        density: str | Unset = UNSET
        if not isinstance(self.density, Unset):
            density = self.density

        logo_alignment: str | Unset = UNSET
        if not isinstance(self.logo_alignment, Unset):
            logo_alignment = self.logo_alignment

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        google_analytics_id: None | str | Unset
        if isinstance(self.google_analytics_id, Unset):
            google_analytics_id = UNSET
        else:
            google_analytics_id = self.google_analytics_id

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item: str = features_item_data
                features.append(features_item)

        sla_target: float | None | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "showGroups": show_groups,
                "robotsIndex": robots_index,
                "hideBranding": hide_branding,
                "autoAddMonitors": auto_add_monitors,
            }
        )
        if homepage_url is not UNSET:
            field_dict["homepageUrl"] = homepage_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if dark_logo_url is not UNSET:
            field_dict["darkLogoUrl"] = dark_logo_url
        if favicon_url is not UNSET:
            field_dict["faviconUrl"] = favicon_url
        if theme is not UNSET:
            field_dict["theme"] = theme
        if theme_color is not UNSET:
            field_dict["themeColor"] = theme_color
        if header_bg_color is not UNSET:
            field_dict["headerBgColor"] = header_bg_color
        if header_text_color is not UNSET:
            field_dict["headerTextColor"] = header_text_color
        if announcement is not UNSET:
            field_dict["announcement"] = announcement
        if density is not UNSET:
            field_dict["density"] = density
        if logo_alignment is not UNSET:
            field_dict["logoAlignment"] = logo_alignment
        if language is not UNSET:
            field_dict["language"] = language
        if google_analytics_id is not UNSET:
            field_dict["googleAnalyticsId"] = google_analytics_id
        if features is not UNSET:
            field_dict["features"] = features
        if sla_target is not UNSET:
            field_dict["slaTarget"] = sla_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        show_groups = d.pop("showGroups")

        robots_index = d.pop("robotsIndex")

        hide_branding = d.pop("hideBranding")

        auto_add_monitors = d.pop("autoAddMonitors")

        def _parse_homepage_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        homepage_url = _parse_homepage_url(d.pop("homepageUrl", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_dark_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dark_logo_url = _parse_dark_logo_url(d.pop("darkLogoUrl", UNSET))

        def _parse_favicon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        favicon_url = _parse_favicon_url(d.pop("faviconUrl", UNSET))

        def _parse_theme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        theme = _parse_theme(d.pop("theme", UNSET))

        def _parse_theme_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        theme_color = _parse_theme_color(d.pop("themeColor", UNSET))

        def _parse_header_bg_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_bg_color = _parse_header_bg_color(d.pop("headerBgColor", UNSET))

        def _parse_header_text_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_text_color = _parse_header_text_color(d.pop("headerTextColor", UNSET))

        def _parse_announcement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        announcement = _parse_announcement(d.pop("announcement", UNSET))

        _density = d.pop("density", UNSET)
        density: StatusPageSettingsViewDensity | Unset
        if isinstance(_density, Unset):
            density = UNSET
        else:
            density = check_status_page_settings_view_density(_density)

        _logo_alignment = d.pop("logoAlignment", UNSET)
        logo_alignment: StatusPageSettingsViewLogoAlignment | Unset
        if isinstance(_logo_alignment, Unset):
            logo_alignment = UNSET
        else:
            logo_alignment = check_status_page_settings_view_logo_alignment(_logo_alignment)

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_google_analytics_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_analytics_id = _parse_google_analytics_id(d.pop("googleAnalyticsId", UNSET))

        _features = d.pop("features", UNSET)
        features: list[StatusPageSettingsViewFeaturesItem] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = check_status_page_settings_view_features_item(features_item_data)

                features.append(features_item)

        def _parse_sla_target(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sla_target = _parse_sla_target(d.pop("slaTarget", UNSET))

        status_page_settings_view = cls(
            show_groups=show_groups,
            robots_index=robots_index,
            hide_branding=hide_branding,
            auto_add_monitors=auto_add_monitors,
            homepage_url=homepage_url,
            logo_url=logo_url,
            dark_logo_url=dark_logo_url,
            favicon_url=favicon_url,
            theme=theme,
            theme_color=theme_color,
            header_bg_color=header_bg_color,
            header_text_color=header_text_color,
            announcement=announcement,
            density=density,
            logo_alignment=logo_alignment,
            language=language,
            google_analytics_id=google_analytics_id,
            features=features,
            sla_target=sla_target,
        )

        status_page_settings_view.additional_properties = d
        return status_page_settings_view

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
