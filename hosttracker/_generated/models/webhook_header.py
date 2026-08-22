from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookHeader")


@_attrs_define
class WebhookHeader:
    """One header."""

    header: str
    """ The header name. `HT-*` and `webhook-*` are reserved for the delivery's own headers and are refused. """
    value: str | Unset = UNSET
    """ The header value. """

    def to_dict(self) -> dict[str, Any]:
        header = self.header

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "header": header,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        header = d.pop("header")

        value = d.pop("value", UNSET)

        webhook_header = cls(
            header=header,
            value=value,
        )

        return webhook_header
