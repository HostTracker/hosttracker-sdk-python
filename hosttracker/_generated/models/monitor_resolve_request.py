from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MonitorResolveRequest")


@_attrs_define
class MonitorResolveRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    url: str
    """ The address to resolve. A bare host name is read as http, exactly as a monitor's target is; an address no
    check could be pointed at (loopback, 0.0.0.0) is refused. """

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        monitor_resolve_request = cls(
            url=url,
        )

        return monitor_resolve_request
