from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.status_page_settings_density import StatusPageSettingsDensity, check_status_page_settings_density
from ..models.status_page_settings_features_item import (
    StatusPageSettingsFeaturesItem,
    check_status_page_settings_features_item,
)
from ..models.status_page_settings_language import StatusPageSettingsLanguage, check_status_page_settings_language
from ..models.status_page_settings_logo_alignment import (
    StatusPageSettingsLogoAlignment,
    check_status_page_settings_logo_alignment,
)
from ..models.status_page_settings_theme import StatusPageSettingsTheme, check_status_page_settings_theme
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageSettings")


@_attrs_define
class StatusPageSettings:
    """How the public page looks and behaves. Only the members you send change; an explicit null clears a clearable one."""

    homepage_url: None | str | Unset = UNSET
    """ Where the page's logo and title link to. Send null to clear it. """
    logo_url: None | str | Unset = UNSET
    """ The logo shown at the top of the page. Send null to clear it. """
    dark_logo_url: None | str | Unset = UNSET
    """ The logo used when the page renders dark. Send null to clear it. """
    favicon_url: None | str | Unset = UNSET
    """ The icon browsers show for the page. Send null to clear it. """
    theme: StatusPageSettingsTheme | Unset = UNSET
    """ Which palette the page renders in. """
    theme_color: None | str | Unset = UNSET
    """ The page's accent colour. Spelled `#rrggbb`. """
    header_bg_color: None | str | Unset = UNSET
    """ The header's background colour. Spelled `#rrggbb`. """
    header_text_color: None | str | Unset = UNSET
    """ The header's text colour. Spelled `#rrggbb`. """
    announcement: None | str | Unset = UNSET
    """ A banner shown above the components. Send null or an empty string to remove it. """
    density: StatusPageSettingsDensity | Unset = UNSET
    """ How tightly the component rows are packed. """
    logo_alignment: StatusPageSettingsLogoAlignment | Unset = UNSET
    """ Where the logo sits in the header. """
    show_groups: bool | Unset = UNSET
    """ Render components under their group headings. """
    robots_index: bool | Unset = UNSET
    """ Allow search engines to index the public page. """
    language: StatusPageSettingsLanguage | Unset = UNSET
    """ The language the public page is rendered in. """
    google_analytics_id: None | str | Unset = UNSET
    """ A Google Analytics measurement id (`G-XXXXXXXX`). Send null to remove it. """
    hide_branding: bool | Unset = UNSET
    """ Hide the HostTracker attribution, where the plan allows it. """
    auto_add_monitors: bool | Unset = UNSET
    """ Add newly created monitors to this page automatically. """
    features: list[StatusPageSettingsFeaturesItem] | Unset = UNSET
    """ The page's WHOLE feature set - sending the array replaces it. A feature not listed is off. """
    sla_target: float | None | Unset = UNSET
    """ The uptime percentage the page measures its components against. Send null to fall back to each monitor's own
    target. """

    def to_dict(self) -> dict[str, Any]:
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

        theme: str | Unset = UNSET
        if not isinstance(self.theme, Unset):
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

        show_groups = self.show_groups

        robots_index = self.robots_index

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language

        google_analytics_id: None | str | Unset
        if isinstance(self.google_analytics_id, Unset):
            google_analytics_id = UNSET
        else:
            google_analytics_id = self.google_analytics_id

        hide_branding = self.hide_branding

        auto_add_monitors = self.auto_add_monitors

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

        field_dict.update({})
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
        if show_groups is not UNSET:
            field_dict["showGroups"] = show_groups
        if robots_index is not UNSET:
            field_dict["robotsIndex"] = robots_index
        if language is not UNSET:
            field_dict["language"] = language
        if google_analytics_id is not UNSET:
            field_dict["googleAnalyticsId"] = google_analytics_id
        if hide_branding is not UNSET:
            field_dict["hideBranding"] = hide_branding
        if auto_add_monitors is not UNSET:
            field_dict["autoAddMonitors"] = auto_add_monitors
        if features is not UNSET:
            field_dict["features"] = features
        if sla_target is not UNSET:
            field_dict["slaTarget"] = sla_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        _theme = d.pop("theme", UNSET)
        theme: StatusPageSettingsTheme | Unset
        if isinstance(_theme, Unset):
            theme = UNSET
        else:
            theme = check_status_page_settings_theme(_theme)

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
        density: StatusPageSettingsDensity | Unset
        if isinstance(_density, Unset):
            density = UNSET
        else:
            density = check_status_page_settings_density(_density)

        _logo_alignment = d.pop("logoAlignment", UNSET)
        logo_alignment: StatusPageSettingsLogoAlignment | Unset
        if isinstance(_logo_alignment, Unset):
            logo_alignment = UNSET
        else:
            logo_alignment = check_status_page_settings_logo_alignment(_logo_alignment)

        show_groups = d.pop("showGroups", UNSET)

        robots_index = d.pop("robotsIndex", UNSET)

        _language = d.pop("language", UNSET)
        language: StatusPageSettingsLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = check_status_page_settings_language(_language)

        def _parse_google_analytics_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_analytics_id = _parse_google_analytics_id(d.pop("googleAnalyticsId", UNSET))

        hide_branding = d.pop("hideBranding", UNSET)

        auto_add_monitors = d.pop("autoAddMonitors", UNSET)

        _features = d.pop("features", UNSET)
        features: list[StatusPageSettingsFeaturesItem] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = check_status_page_settings_features_item(features_item_data)

                features.append(features_item)

        def _parse_sla_target(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sla_target = _parse_sla_target(d.pop("slaTarget", UNSET))

        status_page_settings = cls(
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
            show_groups=show_groups,
            robots_index=robots_index,
            language=language,
            google_analytics_id=google_analytics_id,
            hide_branding=hide_branding,
            auto_add_monitors=auto_add_monitors,
            features=features,
            sla_target=sla_target,
        )

        return status_page_settings
