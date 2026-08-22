from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookMonitorRef")


@_attrs_define
class WebhookMonitorRef:
    """The monitor, in the same identifying projection every v2 read renders: id, name, url and type."""

    id: UUID
    """ The monitor's id - what GET /monitor/{id} takes. """
    name: str
    """ The monitor's name. """
    url: str
    """ The monitored address, as GET /monitor/{id} renders it. """
    type_: str | Unset = UNSET
    """ The monitor type token (http, ping, sslExp, …). Absent when the emitting path does not know it. """

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        url = self.url

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        url = d.pop("url")

        type_ = d.pop("type", UNSET)

        webhook_monitor_ref = cls(
            id=id,
            name=name,
            url=url,
            type_=type_,
        )

        return webhook_monitor_ref
