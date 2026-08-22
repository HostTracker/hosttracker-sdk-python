from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactTestExchange")


@_attrs_define
class ContactTestExchange:
    """The raw HTTP exchange, for an `http` contact: what was sent to the endpoint and what came back. Absent for every
    other contact type. Both strings are capped by the sender's capture limit, so a large response cannot inflate this
    body.

    """

    request: str | Unset = UNSET
    """ The request line, headers and body that were sent. """
    response: str | Unset = UNSET
    """ The status line, headers and body that came back - or the transport error text when nothing did. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request = self.request

        response = self.response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request is not UNSET:
            field_dict["request"] = request
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request = d.pop("request", UNSET)

        response = d.pop("response", UNSET)

        contact_test_exchange = cls(
            request=request,
            response=response,
        )

        contact_test_exchange.additional_properties = d
        return contact_test_exchange

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
