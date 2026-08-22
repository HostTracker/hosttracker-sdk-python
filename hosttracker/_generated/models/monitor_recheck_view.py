from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorRecheckView")


@_attrs_define
class MonitorRecheckView:
    """The recheck strategy - persisted inside the settings blob, a monitor-level concept on the wire."""

    strategy: None | str | Unset = UNSET
    min_num_down: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy: None | str | Unset
        if isinstance(self.strategy, Unset):
            strategy = UNSET
        else:
            strategy = self.strategy

        min_num_down: int | None | Unset
        if isinstance(self.min_num_down, Unset):
            min_num_down = UNSET
        else:
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

        def _parse_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strategy = _parse_strategy(d.pop("strategy", UNSET))

        def _parse_min_num_down(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_num_down = _parse_min_num_down(d.pop("minNumDown", UNSET))

        monitor_recheck_view = cls(
            strategy=strategy,
            min_num_down=min_num_down,
        )

        monitor_recheck_view.additional_properties = d
        return monitor_recheck_view

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
