from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_expiration_settings import CertificateExpirationSettings
    from ..models.database_check_settings import DatabaseCheckSettings
    from ..models.dnsbl_check_settings import DNSBLCheckSettings
    from ..models.domain_expiration_settings import DomainExpirationSettings
    from ..models.fast_check_https_settings import FastCheckHttpsSettings
    from ..models.maintenance_view import MaintenanceView
    from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
    from ..models.monitor_incident_view import MonitorIncidentView
    from ..models.monitor_locations_view import MonitorLocationsView
    from ..models.monitor_recheck_view import MonitorRecheckView
    from ..models.monitor_subscription_view import MonitorSubscriptionView
    from ..models.page_speed_settings import PageSpeedSettings
    from ..models.ping_check_settings import PingCheckSettings
    from ..models.results_monitor_ref_view_attached_type_0 import ResultsMonitorRefViewAttachedType0
    from ..models.snmp_check_settings import SNMPCheckSettings
    from ..models.tcp_port_check_settings import TCPPortCheckSettings
    from ..models.text_analysis_settings import TextAnalysisSettings
    from ..models.transaction_check_settings import TransactionCheckSettings
    from ..models.web_content_check_settings import WebContentCheckSettings
    from ..models.web_risk_settings import WebRiskSettings


T = TypeVar("T", bound="ResultsMonitorRefView")


@_attrs_define
class ResultsMonitorRefView:
    id: UUID
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    type_: None | str | Unset = UNSET
    interval: int | None | Unset = UNSET
    """ `monitor.settings`: how often the monitor runs, seconds. """
    sla_target: float | None | Unset = UNSET
    """ `monitor.settings`: the monitor's own SLA target, percent. """
    locations: MonitorLocationsView | None | Unset = UNSET
    """ `monitor.settings`: which pools check it, and which agents are excluded. """
    recheck: MonitorRecheckView | None | Unset = UNSET
    """ `monitor.settings`: the recheck policy behind a failure. """
    settings: (
        CertificateExpirationSettings
        | DatabaseCheckSettings
        | DNSBLCheckSettings
        | DomainExpirationSettings
        | FastCheckHttpsSettings
        | MonitorCPURAMHDDSettings
        | PageSpeedSettings
        | PingCheckSettings
        | SNMPCheckSettings
        | TCPPortCheckSettings
        | TextAnalysisSettings
        | TransactionCheckSettings
        | Unset
        | WebContentCheckSettings
        | WebRiskSettings
    ) = UNSET
    """ The settings object of every v2 monitor type. The branch is selected by the monitor resource's `type`
    property - settings itself carries no discriminating member, so there is no `discriminator` keyword here and the
    union is an `anyOf`: several branches accept the same object (every member is optional, so an empty settings
    object satisfies most of them), which an exclusive union would call invalid. To pick the branch that describes a
    given object, read `type` off the monitor and look it up in `x-htTypeMapping`; each branch also names its type
    in `x-htType`. 14 types; a Russian-registry blacklist check is expressed as type=http with
    settings.preset="bl:ru". """
    attached: None | ResultsMonitorRefViewAttachedType0 | Unset = UNSET
    """ `monitor.settings`: which sub-checks are switched on (booleans, never results). """
    created: int | None | Unset = UNSET
    """ `monitor.settings`: when the monitor was created. Unix seconds. """
    subscription: list[MonitorSubscriptionView] | None | Unset = UNSET
    """ `monitor.subscription`: the monitor's alert subscriptions with their contacts. """
    last_incident: MonitorIncidentView | None | Unset = UNSET
    """ `monitor.lastIncident`: the monitor's last up/down transition. """
    maintenance: list[MaintenanceView] | None | Unset = UNSET
    """ `monitor.maintenance`: the windows covering the monitor, as definitions. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_expiration_settings import CertificateExpirationSettings
        from ..models.database_check_settings import DatabaseCheckSettings
        from ..models.dnsbl_check_settings import DNSBLCheckSettings
        from ..models.domain_expiration_settings import DomainExpirationSettings
        from ..models.fast_check_https_settings import FastCheckHttpsSettings
        from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
        from ..models.monitor_incident_view import MonitorIncidentView
        from ..models.monitor_locations_view import MonitorLocationsView
        from ..models.monitor_recheck_view import MonitorRecheckView
        from ..models.page_speed_settings import PageSpeedSettings
        from ..models.ping_check_settings import PingCheckSettings
        from ..models.results_monitor_ref_view_attached_type_0 import ResultsMonitorRefViewAttachedType0
        from ..models.snmp_check_settings import SNMPCheckSettings
        from ..models.tcp_port_check_settings import TCPPortCheckSettings
        from ..models.text_analysis_settings import TextAnalysisSettings
        from ..models.web_content_check_settings import WebContentCheckSettings
        from ..models.web_risk_settings import WebRiskSettings

        id = str(self.id)

        name = self.name

        url = self.url

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        interval: int | None | Unset
        if isinstance(self.interval, Unset):
            interval = UNSET
        else:
            interval = self.interval

        sla_target: float | None | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        locations: dict[str, Any] | None | Unset
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, MonitorLocationsView):
            locations = self.locations.to_dict()
        else:
            locations = self.locations

        recheck: dict[str, Any] | None | Unset
        if isinstance(self.recheck, Unset):
            recheck = UNSET
        elif isinstance(self.recheck, MonitorRecheckView):
            recheck = self.recheck.to_dict()
        else:
            recheck = self.recheck

        settings: dict[str, Any] | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, FastCheckHttpsSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, PageSpeedSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, PingCheckSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, TCPPortCheckSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, DomainExpirationSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, CertificateExpirationSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, DNSBLCheckSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, WebRiskSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, MonitorCPURAMHDDSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, WebContentCheckSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, TextAnalysisSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, DatabaseCheckSettings):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, SNMPCheckSettings):
            settings = self.settings.to_dict()
        else:
            settings = self.settings.to_dict()

        attached: dict[str, Any] | None | Unset
        if isinstance(self.attached, Unset):
            attached = UNSET
        elif isinstance(self.attached, ResultsMonitorRefViewAttachedType0):
            attached = self.attached.to_dict()
        else:
            attached = self.attached

        created: int | None | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        else:
            created = self.created

        subscription: list[dict[str, Any]] | None | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        elif isinstance(self.subscription, list):
            subscription = []
            for subscription_type_0_item_data in self.subscription:
                subscription_type_0_item = subscription_type_0_item_data.to_dict()
                subscription.append(subscription_type_0_item)

        else:
            subscription = self.subscription

        last_incident: dict[str, Any] | None | Unset
        if isinstance(self.last_incident, Unset):
            last_incident = UNSET
        elif isinstance(self.last_incident, MonitorIncidentView):
            last_incident = self.last_incident.to_dict()
        else:
            last_incident = self.last_incident

        maintenance: list[dict[str, Any]] | None | Unset
        if isinstance(self.maintenance, Unset):
            maintenance = UNSET
        elif isinstance(self.maintenance, list):
            maintenance = []
            for maintenance_type_0_item_data in self.maintenance:
                maintenance_type_0_item = maintenance_type_0_item_data.to_dict()
                maintenance.append(maintenance_type_0_item)

        else:
            maintenance = self.maintenance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if interval is not UNSET:
            field_dict["interval"] = interval
        if sla_target is not UNSET:
            field_dict["slaTarget"] = sla_target
        if locations is not UNSET:
            field_dict["locations"] = locations
        if recheck is not UNSET:
            field_dict["recheck"] = recheck
        if settings is not UNSET:
            field_dict["settings"] = settings
        if attached is not UNSET:
            field_dict["attached"] = attached
        if created is not UNSET:
            field_dict["created"] = created
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if last_incident is not UNSET:
            field_dict["lastIncident"] = last_incident
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_expiration_settings import CertificateExpirationSettings
        from ..models.database_check_settings import DatabaseCheckSettings
        from ..models.dnsbl_check_settings import DNSBLCheckSettings
        from ..models.domain_expiration_settings import DomainExpirationSettings
        from ..models.fast_check_https_settings import FastCheckHttpsSettings
        from ..models.maintenance_view import MaintenanceView
        from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
        from ..models.monitor_incident_view import MonitorIncidentView
        from ..models.monitor_locations_view import MonitorLocationsView
        from ..models.monitor_recheck_view import MonitorRecheckView
        from ..models.monitor_subscription_view import MonitorSubscriptionView
        from ..models.page_speed_settings import PageSpeedSettings
        from ..models.ping_check_settings import PingCheckSettings
        from ..models.results_monitor_ref_view_attached_type_0 import ResultsMonitorRefViewAttachedType0
        from ..models.snmp_check_settings import SNMPCheckSettings
        from ..models.tcp_port_check_settings import TCPPortCheckSettings
        from ..models.text_analysis_settings import TextAnalysisSettings
        from ..models.transaction_check_settings import TransactionCheckSettings
        from ..models.web_content_check_settings import WebContentCheckSettings
        from ..models.web_risk_settings import WebRiskSettings

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        interval = _parse_interval(d.pop("interval", UNSET))

        def _parse_sla_target(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sla_target = _parse_sla_target(d.pop("slaTarget", UNSET))

        def _parse_locations(data: object) -> MonitorLocationsView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                locations_type_0 = MonitorLocationsView.from_dict(data)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorLocationsView | None | Unset, data)

        locations = _parse_locations(d.pop("locations", UNSET))

        def _parse_recheck(data: object) -> MonitorRecheckView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recheck_type_0 = MonitorRecheckView.from_dict(data)

                return recheck_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorRecheckView | None | Unset, data)

        recheck = _parse_recheck(d.pop("recheck", UNSET))

        def _parse_settings(
            data: object,
        ) -> (
            CertificateExpirationSettings
            | DatabaseCheckSettings
            | DNSBLCheckSettings
            | DomainExpirationSettings
            | FastCheckHttpsSettings
            | MonitorCPURAMHDDSettings
            | PageSpeedSettings
            | PingCheckSettings
            | SNMPCheckSettings
            | TCPPortCheckSettings
            | TextAnalysisSettings
            | TransactionCheckSettings
            | Unset
            | WebContentCheckSettings
            | WebRiskSettings
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_0 = FastCheckHttpsSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_1 = PageSpeedSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_2 = PingCheckSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_3 = TCPPortCheckSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_4 = DomainExpirationSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_5 = CertificateExpirationSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_6 = DNSBLCheckSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_7 = WebRiskSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_8 = MonitorCPURAMHDDSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_9 = WebContentCheckSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_10 = TextAnalysisSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_11 = DatabaseCheckSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_monitor_settings_type_12 = SNMPCheckSettings.from_dict(data)

                return componentsschemas_monitor_settings_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_monitor_settings_type_13 = TransactionCheckSettings.from_dict(data)

            return componentsschemas_monitor_settings_type_13

        settings = _parse_settings(d.pop("settings", UNSET))

        def _parse_attached(data: object) -> None | ResultsMonitorRefViewAttachedType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attached_type_0 = ResultsMonitorRefViewAttachedType0.from_dict(data)

                return attached_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultsMonitorRefViewAttachedType0 | Unset, data)

        attached = _parse_attached(d.pop("attached", UNSET))

        def _parse_created(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        def _parse_subscription(data: object) -> list[MonitorSubscriptionView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subscription_type_0 = []
                _subscription_type_0 = data
                for subscription_type_0_item_data in _subscription_type_0:
                    subscription_type_0_item = MonitorSubscriptionView.from_dict(subscription_type_0_item_data)

                    subscription_type_0.append(subscription_type_0_item)

                return subscription_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonitorSubscriptionView] | None | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_last_incident(data: object) -> MonitorIncidentView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_incident_type_0 = MonitorIncidentView.from_dict(data)

                return last_incident_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorIncidentView | None | Unset, data)

        last_incident = _parse_last_incident(d.pop("lastIncident", UNSET))

        def _parse_maintenance(data: object) -> list[MaintenanceView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                maintenance_type_0 = []
                _maintenance_type_0 = data
                for maintenance_type_0_item_data in _maintenance_type_0:
                    maintenance_type_0_item = MaintenanceView.from_dict(maintenance_type_0_item_data)

                    maintenance_type_0.append(maintenance_type_0_item)

                return maintenance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MaintenanceView] | None | Unset, data)

        maintenance = _parse_maintenance(d.pop("maintenance", UNSET))

        results_monitor_ref_view = cls(
            id=id,
            name=name,
            url=url,
            type_=type_,
            interval=interval,
            sla_target=sla_target,
            locations=locations,
            recheck=recheck,
            settings=settings,
            attached=attached,
            created=created,
            subscription=subscription,
            last_incident=last_incident,
            maintenance=maintenance,
        )

        results_monitor_ref_view.additional_properties = d
        return results_monitor_ref_view

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
