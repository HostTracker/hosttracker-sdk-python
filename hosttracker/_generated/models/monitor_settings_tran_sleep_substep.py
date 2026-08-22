from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSettingsTranSleepSubstep")


@_attrs_define
class MonitorSettingsTranSleepSubstep:
    """A pause embedded in a click/type/hover step. Identical to the `sleep` action's field set."""

    delay: int = 1000
    """ Milliseconds to pause. Must be at least 1: a sleep with no delay is refused, so the 1000 default applies to
    the runner rather than making the field optional. """
    dispersion: int | Unset = 0
    """ Random jitter added to `delay`, in milliseconds. """

    def to_dict(self) -> dict[str, Any]:
        delay = self.delay

        dispersion = self.dispersion

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delay": delay,
            }
        )
        if dispersion is not UNSET:
            field_dict["dispersion"] = dispersion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay = d.pop("delay")

        dispersion = d.pop("dispersion", UNSET)

        monitor_settings_tran_sleep_substep = cls(
            delay=delay,
            dispersion=dispersion,
        )

        return monitor_settings_tran_sleep_substep
