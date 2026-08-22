from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSettingsTranWaitForNavigationSubstep")


@_attrs_define
class MonitorSettingsTranWaitForNavigationSubstep:
    """Wait for navigation AFTER this step."""

    delay: int | Unset = 1000
    """ Milliseconds to wait for navigation to start. """
    fail_when_no_nav: bool | Unset = False
    """ Fail the step when no navigation happened within `delay`. """
    timeout: int | Unset = UNSET
    """ Per-step timeout override, milliseconds. """

    def to_dict(self) -> dict[str, Any]:
        delay = self.delay

        fail_when_no_nav = self.fail_when_no_nav

        timeout = self.timeout

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if delay is not UNSET:
            field_dict["delay"] = delay
        if fail_when_no_nav is not UNSET:
            field_dict["failWhenNoNav"] = fail_when_no_nav
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay = d.pop("delay", UNSET)

        fail_when_no_nav = d.pop("failWhenNoNav", UNSET)

        timeout = d.pop("timeout", UNSET)

        monitor_settings_tran_wait_for_navigation_substep = cls(
            delay=delay,
            fail_when_no_nav=fail_when_no_nav,
            timeout=timeout,
        )

        return monitor_settings_tran_wait_for_navigation_substep
