from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MonitorSettingsHttpHeader")


@_attrs_define
class MonitorSettingsHttpHeader:
    """One request header."""

    name: str
    """ Header name. Stored as element 0 of the [name, value] pair. """
    value: str
    """ Header value. Stored as element 1 of the pair. """

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        monitor_settings_http_header = cls(
            name=name,
            value=value,
        )

        return monitor_settings_http_header
