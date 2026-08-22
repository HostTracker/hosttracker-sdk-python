from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobAcceptedView")


@_attrs_define
class JobAcceptedView:
    job_id: UUID
    accepted: int
    """ How many items/targets the job carries - so a caller can confirm the selection it got is the one it meant
    before the first poll. """
    also_job_id: None | Unset | UUID = UNSET
    """ A SECOND job id, when one request produced two kinds (a patch plus `resetStats`). Absent otherwise. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        accepted = self.accepted

        also_job_id: None | str | Unset
        if isinstance(self.also_job_id, Unset):
            also_job_id = UNSET
        elif isinstance(self.also_job_id, UUID):
            also_job_id = str(self.also_job_id)
        else:
            also_job_id = self.also_job_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobId": job_id,
                "accepted": accepted,
            }
        )
        if also_job_id is not UNSET:
            field_dict["alsoJobId"] = also_job_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = UUID(d.pop("jobId"))

        accepted = d.pop("accepted")

        def _parse_also_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                also_job_id_type_0 = UUID(data)

                return also_job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        also_job_id = _parse_also_job_id(d.pop("alsoJobId", UNSET))

        job_accepted_view = cls(
            job_id=job_id,
            accepted=accepted,
            also_job_id=also_job_id,
        )

        job_accepted_view.additional_properties = d
        return job_accepted_view

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
