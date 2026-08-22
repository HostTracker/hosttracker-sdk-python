from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_provider_view import AgentProviderView


T = TypeVar("T", bound="AgentView")


@_attrs_define
class AgentView:
    id: UUID
    ipv6: bool
    """ **Whether this location can reach IPv6 targets** - a capability, NOT an address. The fleet records one
    egress address per machine plus this flag; a location's IPv6 addresses, where it has them, are in `GET
    /agent/ip` under `family: "ipv6"`. """
    visible: bool
    """ **Whether this location is offered in a location picker.** A running, selectable location that is
    deliberately not advertised (a partner box under evaluation, a region being drained) answers `false`: it still
    runs the checks already pinned to it, and a UI building a tree should leave it out of the list it offers rather
    than hide the fact that it exists. """
    name: str | Unset = UNSET
    """ The human label - `"Country, State, City"`, the SAME string an instant-check event carries as its
    `location`. The machine's host name is deliberately not published: it identifies the box, and the caller's
    question is "where", not "which server". """
    city: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    """ The first-level administrative division the city sits in - a US state, a Canadian province, a German Land.
    Spelled `region`, never `state`: on this surface `state` is the LIFECYCLE word (a monitor's, a job's, an
    incident's), and one word may not carry two concepts. """
    country: None | str | Unset = UNSET
    lat: float | None | Unset = UNSET
    lon: float | None | Unset = UNSET
    provider: AgentProviderView | None | Unset = UNSET
    """ The provider identity a location is published under. """
    version: None | str | Unset = UNSET
    up_from: int | None | Unset = UNSET
    """ Up since, Unix seconds. Null for an agent that has never reported. Unix seconds. """
    capabilities: list[str] | Unset = UNSET
    """ The capabilities this location offers - `icmp` (ping/trace), `browser` (the Waterfall fleet), `internal`
    (the private-network executor). What a client filters on with `?capability=`. """
    pools: list[str] | Unset = UNSET
    """ The pools this location belongs to. """
    ip: None | str | Unset = UNSET
    """ **The address this location's checks go out from** - what an allow-list entry for THIS location looks like,
    as opposed to `GET /agent/ip`'s whole-fleet answer. It is published to every caller, anonymous included, because
    it already is: the fleet's egress addresses are the one v2 endpoint that takes no token at all (an allow-listing
    script usually runs before any credential exists). This member says which of those addresses belongs to which
    location; it discloses no address that endpoint does not. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_provider_view import AgentProviderView

        id = str(self.id)

        ipv6 = self.ipv6

        visible = self.visible

        name = self.name

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        lat: float | None | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lon: float | None | Unset
        if isinstance(self.lon, Unset):
            lon = UNSET
        else:
            lon = self.lon

        provider: dict[str, Any] | None | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, AgentProviderView):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        up_from: int | None | Unset
        if isinstance(self.up_from, Unset):
            up_from = UNSET
        else:
            up_from = self.up_from

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        pools: list[str] | Unset = UNSET
        if not isinstance(self.pools, Unset):
            pools = self.pools

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ipv6": ipv6,
                "visible": visible,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if region is not UNSET:
            field_dict["region"] = region
        if country is not UNSET:
            field_dict["country"] = country
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if provider is not UNSET:
            field_dict["provider"] = provider
        if version is not UNSET:
            field_dict["version"] = version
        if up_from is not UNSET:
            field_dict["upFrom"] = up_from
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if pools is not UNSET:
            field_dict["pools"] = pools
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_provider_view import AgentProviderView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        ipv6 = d.pop("ipv6")

        visible = d.pop("visible")

        name = d.pop("name", UNSET)

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_lon(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lon = _parse_lon(d.pop("lon", UNSET))

        def _parse_provider(data: object) -> AgentProviderView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_0 = AgentProviderView.from_dict(data)

                return provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentProviderView | None | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_up_from(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        up_from = _parse_up_from(d.pop("upFrom", UNSET))

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        pools = cast(list[str], d.pop("pools", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        agent_view = cls(
            id=id,
            ipv6=ipv6,
            visible=visible,
            name=name,
            city=city,
            region=region,
            country=country,
            lat=lat,
            lon=lon,
            provider=provider,
            version=version,
            up_from=up_from,
            capabilities=capabilities,
            pools=pools,
            ip=ip,
        )

        agent_view.additional_properties = d
        return agent_view

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
