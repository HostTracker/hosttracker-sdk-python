from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.monitor_settings_tran_step_check_content_action import (
    MonitorSettingsTranStepCheckContentAction,
    check_monitor_settings_tran_step_check_content_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep
    from ..models.monitor_settings_tran_wait_for_navigation_substep import MonitorSettingsTranWaitForNavigationSubstep


T = TypeVar("T", bound="MonitorSettingsTranStepCheckContent")


@_attrs_define
class MonitorSettingsTranStepCheckContent:
    """Assert on the rendered page's text."""

    action: MonitorSettingsTranStepCheckContentAction
    """ The step's action - the discriminator. All ten are available here, including `hover` and the primary
    `screenshot`/`waitForNavigation` steps that the web editor does not offer: the check engine executes them, so
    the API accepts them. """
    keywords: list[str]
    """ Keywords to look for in the rendered page. 1-10 entries, each at most 127 characters. """
    name: str | Unset = UNSET
    """ Label used in error messages and results. At most 19 characters; 20 or more is refused. """
    timeout: int | Unset = UNSET
    """ Per-step timeout override in milliseconds. Absent ⇒ the action's own default. """
    screenshot: MonitorSettingsTranScreenshotSubstep | Unset = UNSET
    """ Capture a screenshot AFTER this step. Carries no settable fields today. """
    wait_for_navigation: MonitorSettingsTranWaitForNavigationSubstep | Unset = UNSET
    """ Wait for navigation AFTER this step. """
    synthesized: bool | Unset = False
    """ True on the implicit step 0 that navigates to the monitor's own url. v2 publishes that step EXPLICITLY,
    read-only, so a step index in a result means the same step index in the configuration. Ignored on write either
    way, so pasting a read back is safe: sending it back false leaves the step it is on untouched, and sending step
    0 back true is dropped whole rather than duplicated - only the steps you author yourself are stored. """
    case_sensitive: bool | Unset = False
    """ Match the keywords case-sensitively. """
    reverse: bool | Unset = False
    """ Pass when the keywords are ABSENT. """
    all_: bool | Unset = False
    """ Require every keyword rather than any one. """
    only_visible: bool | Unset = False
    """ Search only the visible rendered text. """
    highlight_keywords: bool | Unset = True
    """ Highlight the matches in the step's screenshot. """

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        keywords = self.keywords

        name = self.name

        timeout = self.timeout

        screenshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screenshot, Unset):
            screenshot = self.screenshot.to_dict()

        wait_for_navigation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wait_for_navigation, Unset):
            wait_for_navigation = self.wait_for_navigation.to_dict()

        synthesized = self.synthesized

        case_sensitive = self.case_sensitive

        reverse = self.reverse

        all_ = self.all_

        only_visible = self.only_visible

        highlight_keywords = self.highlight_keywords

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "keywords": keywords,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if screenshot is not UNSET:
            field_dict["screenshot"] = screenshot
        if wait_for_navigation is not UNSET:
            field_dict["waitForNavigation"] = wait_for_navigation
        if synthesized is not UNSET:
            field_dict["synthesized"] = synthesized
        if case_sensitive is not UNSET:
            field_dict["caseSensitive"] = case_sensitive
        if reverse is not UNSET:
            field_dict["reverse"] = reverse
        if all_ is not UNSET:
            field_dict["all"] = all_
        if only_visible is not UNSET:
            field_dict["onlyVisible"] = only_visible
        if highlight_keywords is not UNSET:
            field_dict["highlightKeywords"] = highlight_keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep
        from ..models.monitor_settings_tran_wait_for_navigation_substep import (
            MonitorSettingsTranWaitForNavigationSubstep,
        )

        d = dict(src_dict)
        action = check_monitor_settings_tran_step_check_content_action(d.pop("action"))

        keywords = cast(list[str], d.pop("keywords"))

        name = d.pop("name", UNSET)

        timeout = d.pop("timeout", UNSET)

        _screenshot = d.pop("screenshot", UNSET)
        screenshot: MonitorSettingsTranScreenshotSubstep | Unset
        if isinstance(_screenshot, Unset):
            screenshot = UNSET
        else:
            screenshot = MonitorSettingsTranScreenshotSubstep.from_dict(_screenshot)

        _wait_for_navigation = d.pop("waitForNavigation", UNSET)
        wait_for_navigation: MonitorSettingsTranWaitForNavigationSubstep | Unset
        if isinstance(_wait_for_navigation, Unset):
            wait_for_navigation = UNSET
        else:
            wait_for_navigation = MonitorSettingsTranWaitForNavigationSubstep.from_dict(_wait_for_navigation)

        synthesized = d.pop("synthesized", UNSET)

        case_sensitive = d.pop("caseSensitive", UNSET)

        reverse = d.pop("reverse", UNSET)

        all_ = d.pop("all", UNSET)

        only_visible = d.pop("onlyVisible", UNSET)

        highlight_keywords = d.pop("highlightKeywords", UNSET)

        monitor_settings_tran_step_check_content = cls(
            action=action,
            keywords=keywords,
            name=name,
            timeout=timeout,
            screenshot=screenshot,
            wait_for_navigation=wait_for_navigation,
            synthesized=synthesized,
            case_sensitive=case_sensitive,
            reverse=reverse,
            all_=all_,
            only_visible=only_visible,
            highlight_keywords=highlight_keywords,
        )

        return monitor_settings_tran_step_check_content
