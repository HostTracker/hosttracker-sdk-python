from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceUnavailableError")


@_attrs_define
class ServiceUnavailableError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    service: str | Unset = UNSET
    """ The dependency involved. """
    retry_after: int | Unset = UNSET
    """ Seconds to wait before retrying. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    retry_after_seconds: int | Unset = UNSET
    """ Seconds to wait before retrying. Mirrors the Retry-After header. """
    detail: str | Unset = UNSET
    """ Further detail about this entry. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        service = self.service

        retry_after = self.retry_after

        reason = self.reason

        retry_after_seconds = self.retry_after_seconds

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if service is not UNSET:
            field_dict["service"] = service
        if retry_after is not UNSET:
            field_dict["retryAfter"] = retry_after
        if reason is not UNSET:
            field_dict["reason"] = reason
        if retry_after_seconds is not UNSET:
            field_dict["retryAfterSeconds"] = retry_after_seconds
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        service = d.pop("service", UNSET)

        retry_after = d.pop("retryAfter", UNSET)

        reason = d.pop("reason", UNSET)

        retry_after_seconds = d.pop("retryAfterSeconds", UNSET)

        detail = d.pop("detail", UNSET)

        service_unavailable_error = cls(
            pointer=pointer,
            service=service,
            retry_after=retry_after,
            reason=reason,
            retry_after_seconds=retry_after_seconds,
            detail=detail,
        )

        service_unavailable_error.additional_properties = d
        return service_unavailable_error

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
