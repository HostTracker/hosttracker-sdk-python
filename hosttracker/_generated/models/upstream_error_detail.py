from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpstreamErrorDetail")


@_attrs_define
class UpstreamErrorDetail:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    service: str | Unset = UNSET
    """ The dependency involved. """
    retry_after: int | Unset = UNSET
    """ Seconds to wait before retrying. """
    origin: str | Unset = UNSET
    """ Which delivery path handled the attempt, for example `core` or `api2-fallback`. """
    outcome: str | Unset = UNSET
    """ How the delivery or test attempt ended, as the pipeline reported it. """
    notification_id: str | Unset = UNSET
    """ The id of the notification record this attempt created. """
    external_id: str | Unset = UNSET
    """ The id the downstream channel assigned to this attempt, when it returned one. """
    error: str | Unset = UNSET
    """ The downstream failure message, when the dependency that was called returned one. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        service = self.service

        retry_after = self.retry_after

        origin = self.origin

        outcome = self.outcome

        notification_id = self.notification_id

        external_id = self.external_id

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if service is not UNSET:
            field_dict["service"] = service
        if retry_after is not UNSET:
            field_dict["retryAfter"] = retry_after
        if origin is not UNSET:
            field_dict["origin"] = origin
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if notification_id is not UNSET:
            field_dict["notificationId"] = notification_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        service = d.pop("service", UNSET)

        retry_after = d.pop("retryAfter", UNSET)

        origin = d.pop("origin", UNSET)

        outcome = d.pop("outcome", UNSET)

        notification_id = d.pop("notificationId", UNSET)

        external_id = d.pop("externalId", UNSET)

        error = d.pop("error", UNSET)

        upstream_error_detail = cls(
            pointer=pointer,
            service=service,
            retry_after=retry_after,
            origin=origin,
            outcome=outcome,
            notification_id=notification_id,
            external_id=external_id,
            error=error,
        )

        upstream_error_detail.additional_properties = d
        return upstream_error_detail

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
