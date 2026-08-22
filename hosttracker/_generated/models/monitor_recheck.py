from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_recheck_strategy import MonitorRecheckStrategy, check_monitor_recheck_strategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorRecheck")


@_attrs_define
class MonitorRecheck:
    """How a suspected failure is re-verified before it becomes an incident. Send null to leave the type's default in
    place.

    """

    strategy: MonitorRecheckStrategy | Unset = UNSET
    """ The quorum rule. `noRecheck` concludes on the first failure; `fullAgreement` needs every location to agree;
    `downFullAgreement` needs full agreement only on the way down; `minNumDown` needs `minNumDown` locations to
    fail. An empty string is accepted too but is deliberately not part of the published vocabulary: it clears the
    rule back to the type's default. To leave an existing rule exactly as it is, omit `recheck` entirely. """
    min_num_down: int | Unset = UNSET
    """ How many locations must report a failure, for `strategy: "minNumDown"`. 1 to 10. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy: str | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy

        min_num_down = self.min_num_down

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if min_num_down is not UNSET:
            field_dict["minNumDown"] = min_num_down

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _strategy = d.pop("strategy", UNSET)
        strategy: MonitorRecheckStrategy | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = check_monitor_recheck_strategy(_strategy)

        min_num_down = d.pop("minNumDown", UNSET)

        monitor_recheck = cls(
            strategy=strategy,
            min_num_down=min_num_down,
        )

        monitor_recheck.additional_properties = d
        return monitor_recheck

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
