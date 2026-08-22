from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportTypeView")


@_attrs_define
class ReportTypeView:
    type_: str | Unset = UNSET
    label: str | Unset = UNSET
    formats: list[str] | Unset = UNSET
    sections: list[str] | Unset = UNSET
    """ The content blocks a caller may include. """
    frequencies: list[str] | Unset = UNSET
    """ The scheduling frequencies, as WORDS - the DB's single-char storage never appears. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        label = self.label

        formats: list[str] | Unset = UNSET
        if not isinstance(self.formats, Unset):
            formats = self.formats

        sections: list[str] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections

        frequencies: list[str] | Unset = UNSET
        if not isinstance(self.frequencies, Unset):
            frequencies = self.frequencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if formats is not UNSET:
            field_dict["formats"] = formats
        if sections is not UNSET:
            field_dict["sections"] = sections
        if frequencies is not UNSET:
            field_dict["frequencies"] = frequencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        formats = cast(list[str], d.pop("formats", UNSET))

        sections = cast(list[str], d.pop("sections", UNSET))

        frequencies = cast(list[str], d.pop("frequencies", UNSET))

        report_type_view = cls(
            type_=type_,
            label=label,
            formats=formats,
            sections=sections,
            frequencies=frequencies,
        )

        report_type_view.additional_properties = d
        return report_type_view

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
