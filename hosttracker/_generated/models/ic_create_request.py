from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.ic_create_request_dns_query_item import (
    IcCreateRequestDnsQueryItem,
    check_ic_create_request_dns_query_item,
)
from ..models.ic_create_request_type import IcCreateRequestType, check_ic_create_request_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ic_location_clause import IcLocationClause


T = TypeVar("T", bound="IcCreateRequest")


@_attrs_define
class IcCreateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    url: str
    """ The address the check is aimed at. An absolute http(s) url for the types that fetch one
    (`https://example.com/health`); a bare host or IP for the types that do not (`example.com`, `203.0.113.7`);
    `host:port` for a port check. What each type accepts is stated on its catalogue row. """
    device_emulation: str | Unset = UNSET
    """ Which device profile the browser emulates. Waterfall checks only; absent means desktop. """
    dns_query: list[IcCreateRequestDnsQueryItem] | Unset = UNSET
    """ Which DNS record types to query. DNS checks only. """
    exclude_locations: list[IcLocationClause] | Unset = UNSET
    """ Where the check must NOT run from, in the same clause shape as `locations`. Exclusion wins over inclusion
    where the two overlap. Agent-routed types only. """
    locations: list[IcLocationClause] | Unset = UNSET
    """ Where the check runs from. Each clause's own members are ANDed and its values ORed; the clauses themselves
    are ORed. An empty clause is refused. Agent-routed types only. """
    pools: list[str] | Unset = UNSET
    """ Which monitoring-location pools to run from. Absent means every location the account may use. """
    type_: IcCreateRequestType | Unset = UNSET
    """ Which kind of check to run. Defaults to `http`. """

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        device_emulation = self.device_emulation

        dns_query: list[str] | Unset = UNSET
        if not isinstance(self.dns_query, Unset):
            dns_query = []
            for dns_query_item_data in self.dns_query:
                dns_query_item: str = dns_query_item_data
                dns_query.append(dns_query_item)

        exclude_locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exclude_locations, Unset):
            exclude_locations = []
            for exclude_locations_item_data in self.exclude_locations:
                exclude_locations_item = exclude_locations_item_data.to_dict()
                exclude_locations.append(exclude_locations_item)

        locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        pools: list[str] | Unset = UNSET
        if not isinstance(self.pools, Unset):
            pools = self.pools

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if device_emulation is not UNSET:
            field_dict["deviceEmulation"] = device_emulation
        if dns_query is not UNSET:
            field_dict["dnsQuery"] = dns_query
        if exclude_locations is not UNSET:
            field_dict["excludeLocations"] = exclude_locations
        if locations is not UNSET:
            field_dict["locations"] = locations
        if pools is not UNSET:
            field_dict["pools"] = pools
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ic_location_clause import IcLocationClause

        d = dict(src_dict)
        url = d.pop("url")

        device_emulation = d.pop("deviceEmulation", UNSET)

        _dns_query = d.pop("dnsQuery", UNSET)
        dns_query: list[IcCreateRequestDnsQueryItem] | Unset = UNSET
        if _dns_query is not UNSET:
            dns_query = []
            for dns_query_item_data in _dns_query:
                dns_query_item = check_ic_create_request_dns_query_item(dns_query_item_data)

                dns_query.append(dns_query_item)

        _exclude_locations = d.pop("excludeLocations", UNSET)
        exclude_locations: list[IcLocationClause] | Unset = UNSET
        if _exclude_locations is not UNSET:
            exclude_locations = []
            for exclude_locations_item_data in _exclude_locations:
                exclude_locations_item = IcLocationClause.from_dict(exclude_locations_item_data)

                exclude_locations.append(exclude_locations_item)

        _locations = d.pop("locations", UNSET)
        locations: list[IcLocationClause] | Unset = UNSET
        if _locations is not UNSET:
            locations = []
            for locations_item_data in _locations:
                locations_item = IcLocationClause.from_dict(locations_item_data)

                locations.append(locations_item)

        pools = cast(list[str], d.pop("pools", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: IcCreateRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_ic_create_request_type(_type_)

        ic_create_request = cls(
            url=url,
            device_emulation=device_emulation,
            dns_query=dns_query,
            exclude_locations=exclude_locations,
            locations=locations,
            pools=pools,
            type_=type_,
        )

        return ic_create_request
