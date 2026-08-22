from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContactBulkValidateSummary")


@_attrs_define
class ContactBulkValidateSummary:
    """The per-leg item counts of a validation run."""

    create: int
    update: int
    delete: int
    invalid: int
    """ Items that would NOT be applied. Zero when `valid` is true. """
    would_disable: int
    """ Items that would be created PAUSED because the package is full - the number that turns "will it work?" into
    "it will work, but N of them arrive disabled". """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create = self.create

        update = self.update

        delete = self.delete

        invalid = self.invalid

        would_disable = self.would_disable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create": create,
                "update": update,
                "delete": delete,
                "invalid": invalid,
                "wouldDisable": would_disable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create = d.pop("create")

        update = d.pop("update")

        delete = d.pop("delete")

        invalid = d.pop("invalid")

        would_disable = d.pop("wouldDisable")

        contact_bulk_validate_summary = cls(
            create=create,
            update=update,
            delete=delete,
            invalid=invalid,
            would_disable=would_disable,
        )

        contact_bulk_validate_summary.additional_properties = d
        return contact_bulk_validate_summary

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
