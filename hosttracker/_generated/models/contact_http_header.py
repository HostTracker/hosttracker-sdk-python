from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactHttpHeader")


@_attrs_define
class ContactHttpHeader:
    """One header to send with the webhook-style delivery."""

    header: str
    """ The header name. """
    value: None | str | Unset = UNSET
    """ The header value. """

    def to_dict(self) -> dict[str, Any]:
        header = self.header

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
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

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        contact_http_header = cls(
            header=header,
            value=value,
        )

        return contact_http_header
