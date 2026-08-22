from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IcCreateView")


@_attrs_define
class IcCreateView:
    id: UUID
    """ The check id. """
    db_id: int
    """ The federation the check was registered in. It is part of the result's address, not an internal detail the
    caller can drop - `GET /check/{dbId}/{id}` needs both halves. """
    retry_after: int
    """ Seconds to wait before the FIRST poll. """
    estimated_duration_sec: int
    """ How long this check type usually takes to finish, end to end. A hint, not a promise: it is what lets a
    client size its own timeout instead of inventing one. """
    result_url: str
    """ Where the result will be - the same URL as the `Location` header. Always present on the 202: the one
    construction site builds it from the `(dbId, id)` pair it has just been handed, so it is declared `required` and
    a client may follow it instead of assembling the path itself. """
    created: int
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        db_id = self.db_id

        retry_after = self.retry_after

        estimated_duration_sec = self.estimated_duration_sec

        result_url = self.result_url

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dbId": db_id,
                "retryAfter": retry_after,
                "estimatedDurationSec": estimated_duration_sec,
                "resultUrl": result_url,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        db_id = d.pop("dbId")

        retry_after = d.pop("retryAfter")

        estimated_duration_sec = d.pop("estimatedDurationSec")

        result_url = d.pop("resultUrl")

        created = d.pop("created")

        ic_create_view = cls(
            id=id,
            db_id=db_id,
            retry_after=retry_after,
            estimated_duration_sec=estimated_duration_sec,
            result_url=result_url,
            created=created,
        )

        ic_create_view.additional_properties = d
        return ic_create_view

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
