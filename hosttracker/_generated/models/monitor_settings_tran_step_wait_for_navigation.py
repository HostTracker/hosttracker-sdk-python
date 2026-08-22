from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_settings_tran_step_wait_for_navigation_action import (
    MonitorSettingsTranStepWaitForNavigationAction,
    check_monitor_settings_tran_step_wait_for_navigation_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep


T = TypeVar("T", bound="MonitorSettingsTranStepWaitForNavigation")


@_attrs_define
class MonitorSettingsTranStepWaitForNavigation:
    """Wait for the page to navigate, as a step of its own."""

    action: MonitorSettingsTranStepWaitForNavigationAction
    """ The step's action - the discriminator. All ten are available here, including `hover` and the primary
    `screenshot`/`waitForNavigation` steps that the web editor does not offer: the check engine executes them, so
    the API accepts them. """
    name: str | Unset = UNSET
    """ Label used in error messages and results. At most 19 characters; 20 or more is refused. """
    timeout: int | Unset = UNSET
    """ Per-step timeout override, milliseconds. """
    screenshot: MonitorSettingsTranScreenshotSubstep | Unset = UNSET
    """ Capture a screenshot AFTER this step. Carries no settable fields today. """
    synthesized: bool | Unset = False
    """ True on the implicit step 0 that navigates to the monitor's own url. v2 publishes that step EXPLICITLY,
    read-only, so a step index in a result means the same step index in the configuration. Ignored on write either
    way, so pasting a read back is safe: sending it back false leaves the step it is on untouched, and sending step
    0 back true is dropped whole rather than duplicated - only the steps you author yourself are stored. """
    delay: int | Unset = 1000
    """ Milliseconds to wait for navigation to start. """
    fail_when_no_nav: bool | Unset = False
    """ Fail the step when no navigation happened within `delay`. """

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        name = self.name

        timeout = self.timeout

        screenshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screenshot, Unset):
            screenshot = self.screenshot.to_dict()

        synthesized = self.synthesized

        delay = self.delay

        fail_when_no_nav = self.fail_when_no_nav

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
        if synthesized is not UNSET:
            field_dict["synthesized"] = synthesized
        if delay is not UNSET:
            field_dict["delay"] = delay
        if fail_when_no_nav is not UNSET:
            field_dict["failWhenNoNav"] = fail_when_no_nav

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep

        d = dict(src_dict)
        action = check_monitor_settings_tran_step_wait_for_navigation_action(d.pop("action"))

        name = d.pop("name", UNSET)

        timeout = d.pop("timeout", UNSET)

        _screenshot = d.pop("screenshot", UNSET)
        screenshot: MonitorSettingsTranScreenshotSubstep | Unset
        if isinstance(_screenshot, Unset):
            screenshot = UNSET
        else:
            screenshot = MonitorSettingsTranScreenshotSubstep.from_dict(_screenshot)

        synthesized = d.pop("synthesized", UNSET)

        delay = d.pop("delay", UNSET)

        fail_when_no_nav = d.pop("failWhenNoNav", UNSET)

        monitor_settings_tran_step_wait_for_navigation = cls(
            action=action,
            name=name,
            timeout=timeout,
            screenshot=screenshot,
            synthesized=synthesized,
            delay=delay,
            fail_when_no_nav=fail_when_no_nav,
        )

        return monitor_settings_tran_step_wait_for_navigation
