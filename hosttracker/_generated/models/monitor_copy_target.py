from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorCopyTarget")


@_attrs_define
class MonitorCopyTarget:
    """The address and the name for this one copy."""

    url: str
    """ The address. """
    name: str | Unset = UNSET
    """ This copy's name. Overrides the request's shared `name`. """

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        name = d.pop("name", UNSET)

        monitor_copy_target = cls(
            url=url,
            name=name,
        )

        return monitor_copy_target
