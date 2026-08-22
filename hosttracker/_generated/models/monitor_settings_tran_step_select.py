from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_settings_tran_step_select_action import (
    MonitorSettingsTranStepSelectAction,
    check_monitor_settings_tran_step_select_action,
)
from ..models.monitor_settings_tran_step_select_select_strategy import (
    MonitorSettingsTranStepSelectSelectStrategy,
    check_monitor_settings_tran_step_select_select_strategy,
)
from ..models.monitor_settings_tran_step_select_validation_strategy import (
    MonitorSettingsTranStepSelectValidationStrategy,
    check_monitor_settings_tran_step_select_validation_strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep
    from ..models.monitor_settings_tran_wait_for_navigation_substep import MonitorSettingsTranWaitForNavigationSubstep


T = TypeVar("T", bound="MonitorSettingsTranStepSelect")


@_attrs_define
class MonitorSettingsTranStepSelect:
    """Assert on the presence/cardinality of a selector. The same field set is reused as the `select` sub-step of
    click/type/hover.

    """

    action: MonitorSettingsTranStepSelectAction
    """ The step's action - the discriminator. All ten are available here, including `hover` and the primary
    `screenshot`/`waitForNavigation` steps that the web editor does not offer: the check engine executes them, so
    the API accepts them. """
    selector: str
    """ CSS selector to resolve. """
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
    delay: int | Unset = 1000
    """ Milliseconds to wait for the selector to appear, unless the step's own `timeout` overrides it. """
    only_visible: bool | Unset = True
    """ Only match elements the browser renders as visible. """
    select_strategy: MonitorSettingsTranStepSelectSelectStrategy | Unset = "all"
    """ Which of the matched elements the step acts on. The string shorthand implies `first`. """
    validation_strategy: MonitorSettingsTranStepSelectValidationStrategy | Unset = "oneOrMore"
    """ How many matches make the step pass. """

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        selector = self.selector

        name = self.name

        timeout = self.timeout

        screenshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screenshot, Unset):
            screenshot = self.screenshot.to_dict()

        wait_for_navigation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wait_for_navigation, Unset):
            wait_for_navigation = self.wait_for_navigation.to_dict()

        synthesized = self.synthesized

        delay = self.delay

        only_visible = self.only_visible

        select_strategy: str | Unset = UNSET
        if not isinstance(self.select_strategy, Unset):
            select_strategy = self.select_strategy

        validation_strategy: str | Unset = UNSET
        if not isinstance(self.validation_strategy, Unset):
            validation_strategy = self.validation_strategy

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "selector": selector,
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
        if delay is not UNSET:
            field_dict["delay"] = delay
        if only_visible is not UNSET:
            field_dict["onlyVisible"] = only_visible
        if select_strategy is not UNSET:
            field_dict["selectStrategy"] = select_strategy
        if validation_strategy is not UNSET:
            field_dict["validationStrategy"] = validation_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_tran_screenshot_substep import MonitorSettingsTranScreenshotSubstep
        from ..models.monitor_settings_tran_wait_for_navigation_substep import (
            MonitorSettingsTranWaitForNavigationSubstep,
        )

        d = dict(src_dict)
        action = check_monitor_settings_tran_step_select_action(d.pop("action"))

        selector = d.pop("selector")

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

        delay = d.pop("delay", UNSET)

        only_visible = d.pop("onlyVisible", UNSET)

        _select_strategy = d.pop("selectStrategy", UNSET)
        select_strategy: MonitorSettingsTranStepSelectSelectStrategy | Unset
        if isinstance(_select_strategy, Unset):
            select_strategy = UNSET
        else:
            select_strategy = check_monitor_settings_tran_step_select_select_strategy(_select_strategy)

        _validation_strategy = d.pop("validationStrategy", UNSET)
        validation_strategy: MonitorSettingsTranStepSelectValidationStrategy | Unset
        if isinstance(_validation_strategy, Unset):
            validation_strategy = UNSET
        else:
            validation_strategy = check_monitor_settings_tran_step_select_validation_strategy(_validation_strategy)

        monitor_settings_tran_step_select = cls(
            action=action,
            selector=selector,
            name=name,
            timeout=timeout,
            screenshot=screenshot,
            wait_for_navigation=wait_for_navigation,
            synthesized=synthesized,
            delay=delay,
            only_visible=only_visible,
            select_strategy=select_strategy,
            validation_strategy=validation_strategy,
        )

        return monitor_settings_tran_step_select
