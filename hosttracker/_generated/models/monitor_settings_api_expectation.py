from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.monitor_settings_api_expectation_func import (
    MonitorSettingsApiExpectationFunc,
    check_monitor_settings_api_expectation_func,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSettingsApiExpectation")


@_attrs_define
class MonitorSettingsApiExpectation:
    """An API response expectation - the pre-AssertRuleLang predicate the `api` type has always had."""

    func: MonitorSettingsApiExpectationFunc
    """ The comparison to apply. """
    args: list[str] | Unset = UNSET
    """ Operands. Cardinality follows `func`: 1 for eq/neq/ls/le/ge/gt, at least 1 for in/out, exactly 2 ascending
    numbers for inr/outr. """
    change: int | Unset = 0
    """ Legacy delta mode - compare against the previous run rather than the literal. """
    cpt: str | Unset = ""
    """ Legacy capture name for the extracted value. """

    def to_dict(self) -> dict[str, Any]:
        func: str = self.func

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        change = self.change

        cpt = self.cpt

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "func": func,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if change is not UNSET:
            field_dict["change"] = change
        if cpt is not UNSET:
            field_dict["cpt"] = cpt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        func = check_monitor_settings_api_expectation_func(d.pop("func"))

        args = cast(list[str], d.pop("args", UNSET))

        change = d.pop("change", UNSET)

        cpt = d.pop("cpt", UNSET)

        monitor_settings_api_expectation = cls(
            func=func,
            args=args,
            change=change,
            cpt=cpt,
        )

        return monitor_settings_api_expectation
