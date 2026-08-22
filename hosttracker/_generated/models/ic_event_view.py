from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_provider_view import AgentProviderView
    from ..models.ic_event_view_metrics_type_0 import IcEventViewMetricsType0
    from ..models.result_error_view import ResultErrorView


T = TypeVar("T", bound="IcEventView")


@_attrs_define
class IcEventView:
    """One monitoring location's contribution to an instant check."""

    agent_id: UUID
    done_at: int
    """ When this location finished, Unix seconds. Unix seconds. """
    location: None | str | Unset = UNSET
    """ `"Country, State, City"`, resolved from the fleet. """
    ip: None | str | Unset = UNSET
    """ The address the agent actually resolved and dialled. """
    provider: AgentProviderView | None | Unset = UNSET
    """ **Who runs this location** - the monitoring partner whose network the check went out from, and their site.
    """
    error: None | ResultErrorView | Unset = UNSET
    """ **The failure, when this location failed** - the SAME typed error object a scheduled check's result carries
    (`type`, `code`, `message`, the human `description` and the stable `codename` a client switches on). Absent on
    success - never an empty object. ⚠ It used to be an untyped blob whose SHAPE depended on which of two sources
    the row happened to have: the event's own stored JSON came back verbatim (short keys - `t`/`c`/`m`), while the
    shared error table came back as `{type, code, message}` with no description and no codename. One member, two
    shapes, neither documented, and a client could not switch on either. """
    metrics: IcEventViewMetricsType0 | None | Unset = UNSET
    """ The per-type measurement blob (response time, codes, records …). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_provider_view import AgentProviderView
        from ..models.ic_event_view_metrics_type_0 import IcEventViewMetricsType0
        from ..models.result_error_view import ResultErrorView

        agent_id = str(self.agent_id)

        done_at = self.done_at

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        provider: dict[str, Any] | None | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, AgentProviderView):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ResultErrorView):
            error = self.error.to_dict()
        else:
            error = self.error

        metrics: dict[str, Any] | None | Unset
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, IcEventViewMetricsType0):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agentId": agent_id,
                "doneAt": done_at,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if ip is not UNSET:
            field_dict["ip"] = ip
        if provider is not UNSET:
            field_dict["provider"] = provider
        if error is not UNSET:
            field_dict["error"] = error
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_provider_view import AgentProviderView
        from ..models.ic_event_view_metrics_type_0 import IcEventViewMetricsType0
        from ..models.result_error_view import ResultErrorView

        d = dict(src_dict)
        agent_id = UUID(d.pop("agentId"))

        done_at = d.pop("doneAt")

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

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

        def _parse_error(data: object) -> None | ResultErrorView | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ResultErrorView.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultErrorView | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_metrics(data: object) -> IcEventViewMetricsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = IcEventViewMetricsType0.from_dict(data)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IcEventViewMetricsType0 | None | Unset, data)

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        ic_event_view = cls(
            agent_id=agent_id,
            done_at=done_at,
            location=location,
            ip=ip,
            provider=provider,
            error=error,
            metrics=metrics,
        )

        ic_event_view.additional_properties = d
        return ic_event_view

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
