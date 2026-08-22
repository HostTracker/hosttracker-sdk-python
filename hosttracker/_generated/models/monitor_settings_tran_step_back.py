from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_settings_tran_step_back_action import (
    MonitorSettingsTranStepBackAction,
    check_monitor_settings_tran_step_back_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep
    from ..models.monitor_settings_tran_wait_for_navigation_substep import MonitorSettingsTranWaitForNavigationSubstep


T = TypeVar("T", bound="MonitorSettingsTranStepBack")


@_attrs_define
class MonitorSettingsTranStepBack:
    """Go back one entry in the browser history."""

    action: MonitorSettingsTranStepBackAction
    """ The step's action - the discriminator. All ten are available here, including `hover` and the primary
    `screenshot`/`waitForNavigation` steps that the web editor does not offer: the check engine executes them, so
    the API accepts them. """
    name: str | Unset = UNSET
    """ Label used in error messages and results. At most 19 characters; 20 or more is refused. """
    timeout: int | Unset = 20000
    """ Navigation timeout for the history step, milliseconds. """
    screenshot: MonitorSettingsTranScreenshotSubstep | Unset = UNSET
    """ Capture a screenshot AFTER this step. Carries no settable fields today. """
    wait_for_navigation: MonitorSettingsTranWaitForNavigationSubstep | Unset = UNSET
    """ Wait for navigation AFTER this step. """
    synthesized: bool | Unset = False
    """ True on the implicit step 0 that navigates to the monitor's own url. v2 publishes that step EXPLICITLY,
    read-only, so a step index in a result means the same step index in the configuration. Ignored on write either
    way, so pasting a read back is safe: sending it back false leaves the step it is on untouched, and sending step
    0 back true is dropped whole rather than duplicated - only the steps you author yourself are stored. """

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        name = self.name

        timeout = self.timeout

        screenshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screenshot, Unset):
            screenshot = self.screenshot.to_dict()

        wait_for_navigation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wait_for_navigation, Unset):
            wait_for_navigation = self.wait_for_navigation.to_dict()

        synthesized = self.synthesized

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep
        from ..models.monitor_settings_tran_wait_for_navigation_substep import (
            MonitorSettingsTranWaitForNavigationSubstep,
        )

        d = dict(src_dict)
        action = check_monitor_settings_tran_step_back_action(d.pop("action"))

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

        monitor_settings_tran_step_back = cls(
            action=action,
            name=name,
            timeout=timeout,
            screenshot=screenshot,
            wait_for_navigation=wait_for_navigation,
            synthesized=synthesized,
        )

        return monitor_settings_tran_step_back
