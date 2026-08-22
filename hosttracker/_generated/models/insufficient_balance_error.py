from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsufficientBalanceError")


@_attrs_define
class InsufficientBalanceError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    balance: float | Unset = UNSET
    """ The current balance. """
    required: str | Unset = UNSET
    """ What the operation needed. """
    currency: str | Unset = UNSET
    """ The currency the balance and requirement are in. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        balance = self.balance

        required = self.required

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if balance is not UNSET:
            field_dict["balance"] = balance
        if required is not UNSET:
            field_dict["required"] = required
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        balance = d.pop("balance", UNSET)

        required = d.pop("required", UNSET)

        currency = d.pop("currency", UNSET)

        insufficient_balance_error = cls(
            pointer=pointer,
            balance=balance,
            required=required,
            currency=currency,
        )

        insufficient_balance_error.additional_properties = d
        return insufficient_balance_error

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
