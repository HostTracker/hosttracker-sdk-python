from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_tran_step_back import MonitorSettingsTranStepBack
    from ..models.monitor_settings_tran_step_check_content import MonitorSettingsTranStepCheckContent
    from ..models.monitor_settings_tran_step_click import MonitorSettingsTranStepClick
    from ..models.monitor_settings_tran_step_hover import MonitorSettingsTranStepHover
    from ..models.monitor_settings_tran_step_navigate import MonitorSettingsTranStepNavigate
    from ..models.monitor_settings_tran_step_screenshot import MonitorSettingsTranStepScreenshot
    from ..models.monitor_settings_tran_step_select import MonitorSettingsTranStepSelect
    from ..models.monitor_settings_tran_step_sleep import MonitorSettingsTranStepSleep
    from ..models.monitor_settings_tran_step_type import MonitorSettingsTranStepType
    from ..models.monitor_settings_tran_step_wait_for_navigation import MonitorSettingsTranStepWaitForNavigation


T = TypeVar("T", bound="TransactionCheckSettings")


@_attrs_define
class TransactionCheckSettings:
    """Automates a multi-step web transaction - form submission, login, site traversal - in a real browser, asserting on
    each step. The richest configuration on the surface.

    """

    steps: list[
        MonitorSettingsTranStepBack
        | MonitorSettingsTranStepCheckContent
        | MonitorSettingsTranStepClick
        | MonitorSettingsTranStepHover
        | MonitorSettingsTranStepNavigate
        | MonitorSettingsTranStepScreenshot
        | MonitorSettingsTranStepSelect
        | MonitorSettingsTranStepSleep
        | MonitorSettingsTranStepType
        | MonitorSettingsTranStepWaitForNavigation
    ]
    """ The transaction, in order. At least one step; at most 10. Sequential and fail-fast - the first failing step
    ends the check. """
    timeout: int | Unset = 40000
    """ Whole-check timeout in milliseconds. A value above 40000 is REFUSED with invalid_settings, never silently
    clamped to the cap. """
    skip_media: bool | Unset = True
    """ Skip images and media downloads. `true` is the default and is deliberately not written to storage, so an
    absent key means true. """
    final_screenshot: bool | Unset = True
    """ Capture a screenshot after the last step. """
    console_error: bool | Unset = False
    """ Fail the check when the browser logs a console error. """
    expected_console_errors: list[str] | Unset = UNSET
    """ Console-error substrings to tolerate when `consoleError` is on. Max 10 entries, each at most 127 characters.
    Upper-cased by the executor before matching. """

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_settings_tran_step_check_content import MonitorSettingsTranStepCheckContent
        from ..models.monitor_settings_tran_step_click import MonitorSettingsTranStepClick
        from ..models.monitor_settings_tran_step_hover import MonitorSettingsTranStepHover
        from ..models.monitor_settings_tran_step_navigate import MonitorSettingsTranStepNavigate
        from ..models.monitor_settings_tran_step_screenshot import MonitorSettingsTranStepScreenshot
        from ..models.monitor_settings_tran_step_select import MonitorSettingsTranStepSelect
        from ..models.monitor_settings_tran_step_sleep import MonitorSettingsTranStepSleep
        from ..models.monitor_settings_tran_step_type import MonitorSettingsTranStepType
        from ..models.monitor_settings_tran_step_wait_for_navigation import MonitorSettingsTranStepWaitForNavigation

        steps = []
        for steps_item_data in self.steps:
            steps_item: dict[str, Any]
            if isinstance(steps_item_data, MonitorSettingsTranStepNavigate):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepClick):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepType):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepSelect):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepHover):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepCheckContent):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepSleep):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepScreenshot):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MonitorSettingsTranStepWaitForNavigation):
                steps_item = steps_item_data.to_dict()
            else:
                steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        timeout = self.timeout

        skip_media = self.skip_media

        final_screenshot = self.final_screenshot

        console_error = self.console_error

        expected_console_errors: list[str] | Unset = UNSET
        if not isinstance(self.expected_console_errors, Unset):
            expected_console_errors = self.expected_console_errors

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "steps": steps,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if skip_media is not UNSET:
            field_dict["skipMedia"] = skip_media
        if final_screenshot is not UNSET:
            field_dict["finalScreenshot"] = final_screenshot
        if console_error is not UNSET:
            field_dict["consoleError"] = console_error
        if expected_console_errors is not UNSET:
            field_dict["expectedConsoleErrors"] = expected_console_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_tran_step_back import MonitorSettingsTranStepBack
        from ..models.monitor_settings_tran_step_check_content import MonitorSettingsTranStepCheckContent
        from ..models.monitor_settings_tran_step_click import MonitorSettingsTranStepClick
        from ..models.monitor_settings_tran_step_hover import MonitorSettingsTranStepHover
        from ..models.monitor_settings_tran_step_navigate import MonitorSettingsTranStepNavigate
        from ..models.monitor_settings_tran_step_screenshot import MonitorSettingsTranStepScreenshot
        from ..models.monitor_settings_tran_step_select import MonitorSettingsTranStepSelect
        from ..models.monitor_settings_tran_step_sleep import MonitorSettingsTranStepSleep
        from ..models.monitor_settings_tran_step_type import MonitorSettingsTranStepType
        from ..models.monitor_settings_tran_step_wait_for_navigation import MonitorSettingsTranStepWaitForNavigation

        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:

            def _parse_steps_item(
                data: object,
            ) -> (
                MonitorSettingsTranStepBack
                | MonitorSettingsTranStepCheckContent
                | MonitorSettingsTranStepClick
                | MonitorSettingsTranStepHover
                | MonitorSettingsTranStepNavigate
                | MonitorSettingsTranStepScreenshot
                | MonitorSettingsTranStepSelect
                | MonitorSettingsTranStepSleep
                | MonitorSettingsTranStepType
                | MonitorSettingsTranStepWaitForNavigation
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_0 = MonitorSettingsTranStepNavigate.from_dict(
                        data
                    )

                    return componentsschemas_monitor_settings_tran_step_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_1 = MonitorSettingsTranStepClick.from_dict(data)

                    return componentsschemas_monitor_settings_tran_step_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_2 = MonitorSettingsTranStepType.from_dict(data)

                    return componentsschemas_monitor_settings_tran_step_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_3 = MonitorSettingsTranStepSelect.from_dict(data)

                    return componentsschemas_monitor_settings_tran_step_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_4 = MonitorSettingsTranStepHover.from_dict(data)

                    return componentsschemas_monitor_settings_tran_step_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_5 = MonitorSettingsTranStepCheckContent.from_dict(
                        data
                    )

                    return componentsschemas_monitor_settings_tran_step_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_6 = MonitorSettingsTranStepSleep.from_dict(data)

                    return componentsschemas_monitor_settings_tran_step_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_7 = MonitorSettingsTranStepScreenshot.from_dict(
                        data
                    )

                    return componentsschemas_monitor_settings_tran_step_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_monitor_settings_tran_step_type_8 = (
                        MonitorSettingsTranStepWaitForNavigation.from_dict(data)
                    )

                    return componentsschemas_monitor_settings_tran_step_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_tran_step_type_9 = MonitorSettingsTranStepBack.from_dict(data)

                return componentsschemas_monitor_settings_tran_step_type_9

            steps_item = _parse_steps_item(steps_item_data)

            steps.append(steps_item)

        timeout = d.pop("timeout", UNSET)

        skip_media = d.pop("skipMedia", UNSET)

        final_screenshot = d.pop("finalScreenshot", UNSET)

        console_error = d.pop("consoleError", UNSET)

        expected_console_errors = cast(list[str], d.pop("expectedConsoleErrors", UNSET))

        transaction_check_settings = cls(
            steps=steps,
            timeout=timeout,
            skip_media=skip_media,
            final_screenshot=final_screenshot,
            console_error=console_error,
            expected_console_errors=expected_console_errors,
        )

        return transaction_check_settings
