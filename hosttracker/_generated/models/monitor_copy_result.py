from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.monitor_copy_summary import MonitorCopySummary
    from ..models.monitor_view import MonitorView


T = TypeVar("T", bound="MonitorCopyResult")


@_attrs_define
class MonitorCopyResult:
    """The monitors a copy created, and what it carried over with them."""

    summary: MonitorCopySummary
    """ How much the copy reproduced. """
    data: list[MonitorView]
    """ The created monitors, in the order the addresses were sent, each in exactly the shape GET /monitor/{id}
    renders it. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_copy_summary import MonitorCopySummary
        from ..models.monitor_view import MonitorView

        d = dict(src_dict)
        summary = MonitorCopySummary.from_dict(d.pop("summary"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MonitorView.from_dict(data_item_data)

            data.append(data_item)

        monitor_copy_result = cls(
            summary=summary,
            data=data,
        )

        monitor_copy_result.additional_properties = d
        return monitor_copy_result

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
