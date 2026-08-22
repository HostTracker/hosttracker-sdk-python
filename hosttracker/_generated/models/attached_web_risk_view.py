from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachedWebRiskView")


@_attrs_define
class AttachedWebRiskView:
    """`attached.webRisk` - Google Web Risk's verdict for the monitor's url."""

    verdict: str | Unset = UNSET
    threats: list[str] | Unset = UNSET
    """ The reported threat types, verbatim as the upstream names them. Empty for a clean verdict. """
    checked_at: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verdict = self.verdict

        threats: list[str] | Unset = UNSET
        if not isinstance(self.threats, Unset):
            threats = self.threats

        checked_at: int | None | Unset
        if isinstance(self.checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = self.checked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verdict is not UNSET:
            field_dict["verdict"] = verdict
        if threats is not UNSET:
            field_dict["threats"] = threats
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verdict = d.pop("verdict", UNSET)

        threats = cast(list[str], d.pop("threats", UNSET))

        def _parse_checked_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checked_at = _parse_checked_at(d.pop("checkedAt", UNSET))

        attached_web_risk_view = cls(
            verdict=verdict,
            threats=threats,
            checked_at=checked_at,
        )

        attached_web_risk_view.additional_properties = d
        return attached_web_risk_view

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
