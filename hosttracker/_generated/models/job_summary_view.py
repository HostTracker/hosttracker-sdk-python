from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JobSummaryView")


@_attrs_define
class JobSummaryView:
    created: int
    updated: int
    skipped: int
    failed: int
    deleted: int
    """ How many items were removed. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        updated = self.updated

        skipped = self.skipped

        failed = self.failed

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "skipped": skipped,
                "failed": failed,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        updated = d.pop("updated")

        skipped = d.pop("skipped")

        failed = d.pop("failed")

        deleted = d.pop("deleted")

        job_summary_view = cls(
            created=created,
            updated=updated,
            skipped=skipped,
            failed=failed,
            deleted=deleted,
        )

        job_summary_view.additional_properties = d
        return job_summary_view

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
