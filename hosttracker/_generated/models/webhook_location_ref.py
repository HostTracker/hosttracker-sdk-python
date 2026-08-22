from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookLocationRef")


@_attrs_define
class WebhookLocationRef:
    """A check location - the same members the results feed renders as `location`."""

    id: UUID | Unset = UNSET
    """ The agent that ran the check. Absent when no fleet agent was involved. """
    country: str | Unset = UNSET
    """ The location's country. """
    region: str | Unset = UNSET
    """ The location's state, province or region. """
    city: str | Unset = UNSET
    """ The location's city. """
    ip: str | Unset = UNSET
    """ The address the check was made from. """

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        country = self.country

        region = self.region

        city = self.city

        ip = self.ip

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if country is not UNSET:
            field_dict["country"] = country
        if region is not UNSET:
            field_dict["region"] = region
        if city is not UNSET:
            field_dict["city"] = city
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        country = d.pop("country", UNSET)

        region = d.pop("region", UNSET)

        city = d.pop("city", UNSET)

        ip = d.pop("ip", UNSET)

        webhook_location_ref = cls(
            id=id,
            country=country,
            region=region,
            city=city,
            ip=ip,
        )

        return webhook_location_ref
