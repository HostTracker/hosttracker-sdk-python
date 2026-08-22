from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultErrorView")


@_attrs_define
class ResultErrorView:
    """The error taxonomy of a failed check - typed members, never a prose blob."""

    code: int
    type_: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    """ The technical message the agent reported. """
    description: None | str | Unset = UNSET
    """ The human rendering of `(type, code)`. """
    codename: None | str | Unset = UNSET
    """ A short, stable English codename - the value a client switches on. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        codename: None | str | Unset
        if isinstance(self.codename, Unset):
            codename = UNSET
        else:
            codename = self.codename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if message is not UNSET:
            field_dict["message"] = message
        if description is not UNSET:
            field_dict["description"] = description
        if codename is not UNSET:
            field_dict["codename"] = codename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_codename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codename = _parse_codename(d.pop("codename", UNSET))

        result_error_view = cls(
            code=code,
            type_=type_,
            message=message,
            description=description,
            codename=codename,
        )

        result_error_view.additional_properties = d
        return result_error_view

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
