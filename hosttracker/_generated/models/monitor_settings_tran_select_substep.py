from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_settings_tran_select_substep_select_strategy import (
    MonitorSettingsTranSelectSubstepSelectStrategy,
    check_monitor_settings_tran_select_substep_select_strategy,
)
from ..models.monitor_settings_tran_select_substep_validation_strategy import (
    MonitorSettingsTranSelectSubstepValidationStrategy,
    check_monitor_settings_tran_select_substep_validation_strategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSettingsTranSelectSubstep")


@_attrs_define
class MonitorSettingsTranSelectSubstep:
    """An element selection embedded in a click/type/hover step. Identical to the `select` action's field set - one
    definition, four homes.

    """

    selector: str
    """ CSS selector to resolve. """
    delay: int | Unset = 1000
    """ Milliseconds to wait for the selector to appear, unless the step's own `timeout` overrides it. """
    only_visible: bool | Unset = True
    """ Only match elements the browser renders as visible. """
    select_strategy: MonitorSettingsTranSelectSubstepSelectStrategy | Unset = "all"
    """ Which of the matched elements the step acts on. The string shorthand implies `first`. """
    validation_strategy: MonitorSettingsTranSelectSubstepValidationStrategy | Unset = "oneOrMore"
    """ How many matches make the step pass. """

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector

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
                "selector": selector,
            }
        )
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
        d = dict(src_dict)
        selector = d.pop("selector")

        delay = d.pop("delay", UNSET)

        only_visible = d.pop("onlyVisible", UNSET)

        _select_strategy = d.pop("selectStrategy", UNSET)
        select_strategy: MonitorSettingsTranSelectSubstepSelectStrategy | Unset
        if isinstance(_select_strategy, Unset):
            select_strategy = UNSET
        else:
            select_strategy = check_monitor_settings_tran_select_substep_select_strategy(_select_strategy)

        _validation_strategy = d.pop("validationStrategy", UNSET)
        validation_strategy: MonitorSettingsTranSelectSubstepValidationStrategy | Unset
        if isinstance(_validation_strategy, Unset):
            validation_strategy = UNSET
        else:
            validation_strategy = check_monitor_settings_tran_select_substep_validation_strategy(_validation_strategy)

        monitor_settings_tran_select_substep = cls(
            selector=selector,
            delay=delay,
            only_visible=only_visible,
            select_strategy=select_strategy,
            validation_strategy=validation_strategy,
        )

        return monitor_settings_tran_select_substep
