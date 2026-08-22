from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookSecretView")


@_attrs_define
class WebhookSecretView:
    set_: bool
    updated_at: int | None | Unset = UNSET
    """ Unix seconds. """
    value: None | str | Unset = UNSET
    """ THE reveal. Present only at mint and at rotate. """
    previous_valid_until: int | None | Unset = UNSET
    """ When a rotation grace window is open, the instant the PREVIOUS secret stops signing. Both signatures ride
    the same `HT-Signature` header until then, so rotation is not a hard cutover. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_ = self.set_

        updated_at: int | None | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        previous_valid_until: int | None | Unset
        if isinstance(self.previous_valid_until, Unset):
            previous_valid_until = UNSET
        else:
            previous_valid_until = self.previous_valid_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "set": set_,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if value is not UNSET:
            field_dict["value"] = value
        if previous_valid_until is not UNSET:
            field_dict["previousValidUntil"] = previous_valid_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_ = d.pop("set")

        def _parse_updated_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_previous_valid_until(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        previous_valid_until = _parse_previous_valid_until(d.pop("previousValidUntil", UNSET))

        webhook_secret_view = cls(
            set_=set_,
            updated_at=updated_at,
            value=value,
            previous_valid_until=previous_valid_until,
        )

        webhook_secret_view.additional_properties = d
        return webhook_secret_view

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
