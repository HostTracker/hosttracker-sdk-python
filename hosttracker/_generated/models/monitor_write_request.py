from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.monitor_write_request_on_overlimit import (
    MonitorWriteRequestOnOverlimit,
    check_monitor_write_request_on_overlimit,
)
from ..models.monitor_write_request_type import MonitorWriteRequestType, check_monitor_write_request_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_expiration_settings import CertificateExpirationSettings
    from ..models.database_check_settings import DatabaseCheckSettings
    from ..models.dnsbl_check_settings import DNSBLCheckSettings
    from ..models.domain_expiration_settings import DomainExpirationSettings
    from ..models.fast_check_https_settings import FastCheckHttpsSettings
    from ..models.monitor_alert_subscription import MonitorAlertSubscription
    from ..models.monitor_attached import MonitorAttached
    from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
    from ..models.monitor_inline_contact import MonitorInlineContact
    from ..models.monitor_locations import MonitorLocations
    from ..models.monitor_recheck import MonitorRecheck
    from ..models.monitor_report_subscription import MonitorReportSubscription
    from ..models.page_speed_settings import PageSpeedSettings
    from ..models.ping_check_settings import PingCheckSettings
    from ..models.snmp_check_settings import SNMPCheckSettings
    from ..models.tcp_port_check_settings import TCPPortCheckSettings
    from ..models.text_analysis_settings import TextAnalysisSettings
    from ..models.transaction_check_settings import TransactionCheckSettings
    from ..models.web_content_check_settings import WebContentCheckSettings
    from ..models.web_risk_settings import WebRiskSettings


T = TypeVar("T", bound="MonitorWriteRequest")


@_attrs_define
class MonitorWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    type_: MonitorWriteRequestType
    """ Which kind of check this is. It fixes which `settings` members are valid and cannot be changed after
    creation. """
    add_tags: list[str] | Unset = UNSET
    """ Tags to ADD to whatever this monitor already carries, leaving its other tags alone. Update only, and never
    together with `tags`, which REPLACES the set instead. On a bulk update every monitor starts from its own tags -
    which is the whole reason to send a delta. """
    alert_subscriptions: list[MonitorAlertSubscription] | Unset = UNSET
    """ Alert subscriptions to wire up in the same request. Each entry must name at least one of `contactIds` or
    `contactRefs`. """
    attached: MonitorAttached | Unset = UNSET
    """ The sub-checks that run alongside this monitor. A kind's value is `true`/`false` to switch it on or off, or
    an object carrying that kind's own settings (with `enabled: false` to keep it configured but off). Whatever is
    set here must agree with `settings.attached` if both name the same kind. """
    contacts: list[MonitorInlineContact] | Unset = UNSET
    """ Contacts to create or bind in the same request. """
    cron_schedule: str | Unset = UNSET
    """ A cron expression, replacing the fixed interval. Send null to go back to an interval. """
    enabled: bool | Unset = UNSET
    """ Whether this is currently running. """
    full_log: bool | Unset = UNSET
    """ Keep the full response body of every check, not only the verdict. """
    interval: int | Unset = UNSET
    """ How often the check runs, in SECONDS. Optional on a create: the types that publish a `fixedInterval`
    schedule themselves at that cadence, and the rest fall back to the account default. """
    locations: MonitorLocations | Unset = UNSET
    """ Where the check runs from. """
    name: str | Unset = UNSET
    """ A display name for the monitor. Never an identifier. """
    on_overlimit: MonitorWriteRequestOnOverlimit | Unset = UNSET
    """ What to do when the account's package will not fit this monitor. "fail" (the default) refuses the write;
    "disable" creates it disabled, with a package-limit reason, so nothing is lost. The bulk endpoints additionally
    accept "stop", which decides what happens to the items after this one. """
    open_stat: bool | Unset = UNSET
    """ Make this resource's statistics publicly readable. """
    recheck: MonitorRecheck | Unset = UNSET
    """ How a suspected failure is re-verified before it becomes an incident. Send null to leave the type's default
    in place. """
    remove_tags: list[str] | Unset = UNSET
    """ Tags to REMOVE from this monitor, matched exactly and case-sensitively; one that is not there is not an
    error. Update only, and never together with `tags`. A tag named in both deltas is removed. """
    report_subscriptions: list[MonitorReportSubscription] | Unset = UNSET
    """ Report subscriptions to wire up in the same request. Each entry must name at least one of `contactIds` or
    `contactRefs`. """
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
    sla_target: float | Unset = UNSET
    """ The uptime percentage this resource is measured against. """
    tags: list[str] | Unset = UNSET
    """ Free-form labels. A tag filter matches any of them. """
    url: str | Unset = UNSET
    """ The address the check is aimed at. An absolute http(s) url for the types that fetch one
    (`https://example.com/health`); a bare host or IP for the types that do not (`example.com`, `203.0.113.7`);
    `host:port` for a port check. What each type accepts is stated on its catalogue row. """

    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_expiration_settings import CertificateExpirationSettings
        from ..models.database_check_settings import DatabaseCheckSettings
        from ..models.dnsbl_check_settings import DNSBLCheckSettings
        from ..models.domain_expiration_settings import DomainExpirationSettings
        from ..models.fast_check_https_settings import FastCheckHttpsSettings
        from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
        from ..models.page_speed_settings import PageSpeedSettings
        from ..models.ping_check_settings import PingCheckSettings
        from ..models.snmp_check_settings import SNMPCheckSettings
        from ..models.tcp_port_check_settings import TCPPortCheckSettings
        from ..models.text_analysis_settings import TextAnalysisSettings
        from ..models.web_content_check_settings import WebContentCheckSettings
        from ..models.web_risk_settings import WebRiskSettings

        type_: str = self.type_

        add_tags: list[str] | Unset = UNSET
        if not isinstance(self.add_tags, Unset):
            add_tags = self.add_tags

        alert_subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alert_subscriptions, Unset):
            alert_subscriptions = []
            for alert_subscriptions_item_data in self.alert_subscriptions:
                alert_subscriptions_item = alert_subscriptions_item_data.to_dict()
                alert_subscriptions.append(alert_subscriptions_item)

        attached: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attached, Unset):
            attached = self.attached.to_dict()

        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        cron_schedule = self.cron_schedule

        enabled = self.enabled

        full_log = self.full_log

        interval = self.interval

        locations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations.to_dict()

        name = self.name

        on_overlimit: str | Unset = UNSET
        if not isinstance(self.on_overlimit, Unset):
            on_overlimit = self.on_overlimit

        open_stat = self.open_stat

        recheck: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recheck, Unset):
            recheck = self.recheck.to_dict()

        remove_tags: list[str] | Unset = UNSET
        if not isinstance(self.remove_tags, Unset):
            remove_tags = self.remove_tags

        report_subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.report_subscriptions, Unset):
            report_subscriptions = []
            for report_subscriptions_item_data in self.report_subscriptions:
                report_subscriptions_item = report_subscriptions_item_data.to_dict()
                report_subscriptions.append(report_subscriptions_item)

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

        sla_target = self.sla_target

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if add_tags is not UNSET:
            field_dict["addTags"] = add_tags
        if alert_subscriptions is not UNSET:
            field_dict["alertSubscriptions"] = alert_subscriptions
        if attached is not UNSET:
            field_dict["attached"] = attached
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if cron_schedule is not UNSET:
            field_dict["cronSchedule"] = cron_schedule
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if full_log is not UNSET:
            field_dict["fullLog"] = full_log
        if interval is not UNSET:
            field_dict["interval"] = interval
        if locations is not UNSET:
            field_dict["locations"] = locations
        if name is not UNSET:
            field_dict["name"] = name
        if on_overlimit is not UNSET:
            field_dict["onOverlimit"] = on_overlimit
        if open_stat is not UNSET:
            field_dict["openStat"] = open_stat
        if recheck is not UNSET:
            field_dict["recheck"] = recheck
        if remove_tags is not UNSET:
            field_dict["removeTags"] = remove_tags
        if report_subscriptions is not UNSET:
            field_dict["reportSubscriptions"] = report_subscriptions
        if settings is not UNSET:
            field_dict["settings"] = settings
        if sla_target is not UNSET:
            field_dict["slaTarget"] = sla_target
        if tags is not UNSET:
            field_dict["tags"] = tags
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_expiration_settings import CertificateExpirationSettings
        from ..models.database_check_settings import DatabaseCheckSettings
        from ..models.dnsbl_check_settings import DNSBLCheckSettings
        from ..models.domain_expiration_settings import DomainExpirationSettings
        from ..models.fast_check_https_settings import FastCheckHttpsSettings
        from ..models.monitor_alert_subscription import MonitorAlertSubscription
        from ..models.monitor_attached import MonitorAttached
        from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
        from ..models.monitor_inline_contact import MonitorInlineContact
        from ..models.monitor_locations import MonitorLocations
        from ..models.monitor_recheck import MonitorRecheck
        from ..models.monitor_report_subscription import MonitorReportSubscription
        from ..models.page_speed_settings import PageSpeedSettings
        from ..models.ping_check_settings import PingCheckSettings
        from ..models.snmp_check_settings import SNMPCheckSettings
        from ..models.tcp_port_check_settings import TCPPortCheckSettings
        from ..models.text_analysis_settings import TextAnalysisSettings
        from ..models.transaction_check_settings import TransactionCheckSettings
        from ..models.web_content_check_settings import WebContentCheckSettings
        from ..models.web_risk_settings import WebRiskSettings

        d = dict(src_dict)
        type_ = check_monitor_write_request_type(d.pop("type"))

        add_tags = cast(list[str], d.pop("addTags", UNSET))

        _alert_subscriptions = d.pop("alertSubscriptions", UNSET)
        alert_subscriptions: list[MonitorAlertSubscription] | Unset = UNSET
        if _alert_subscriptions is not UNSET:
            alert_subscriptions = []
            for alert_subscriptions_item_data in _alert_subscriptions:
                alert_subscriptions_item = MonitorAlertSubscription.from_dict(alert_subscriptions_item_data)

                alert_subscriptions.append(alert_subscriptions_item)

        _attached = d.pop("attached", UNSET)
        attached: MonitorAttached | Unset
        if isinstance(_attached, Unset):
            attached = UNSET
        else:
            attached = MonitorAttached.from_dict(_attached)

        _contacts = d.pop("contacts", UNSET)
        contacts: list[MonitorInlineContact] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = MonitorInlineContact.from_dict(contacts_item_data)

                contacts.append(contacts_item)

        cron_schedule = d.pop("cronSchedule", UNSET)

        enabled = d.pop("enabled", UNSET)

        full_log = d.pop("fullLog", UNSET)

        interval = d.pop("interval", UNSET)

        _locations = d.pop("locations", UNSET)
        locations: MonitorLocations | Unset
        if isinstance(_locations, Unset):
            locations = UNSET
        else:
            locations = MonitorLocations.from_dict(_locations)

        name = d.pop("name", UNSET)

        _on_overlimit = d.pop("onOverlimit", UNSET)
        on_overlimit: MonitorWriteRequestOnOverlimit | Unset
        if isinstance(_on_overlimit, Unset):
            on_overlimit = UNSET
        else:
            on_overlimit = check_monitor_write_request_on_overlimit(_on_overlimit)

        open_stat = d.pop("openStat", UNSET)

        _recheck = d.pop("recheck", UNSET)
        recheck: MonitorRecheck | Unset
        if isinstance(_recheck, Unset):
            recheck = UNSET
        else:
            recheck = MonitorRecheck.from_dict(_recheck)

        remove_tags = cast(list[str], d.pop("removeTags", UNSET))

        _report_subscriptions = d.pop("reportSubscriptions", UNSET)
        report_subscriptions: list[MonitorReportSubscription] | Unset = UNSET
        if _report_subscriptions is not UNSET:
            report_subscriptions = []
            for report_subscriptions_item_data in _report_subscriptions:
                report_subscriptions_item = MonitorReportSubscription.from_dict(report_subscriptions_item_data)

                report_subscriptions.append(report_subscriptions_item)

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

        sla_target = d.pop("slaTarget", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        url = d.pop("url", UNSET)

        monitor_write_request = cls(
            type_=type_,
            add_tags=add_tags,
            alert_subscriptions=alert_subscriptions,
            attached=attached,
            contacts=contacts,
            cron_schedule=cron_schedule,
            enabled=enabled,
            full_log=full_log,
            interval=interval,
            locations=locations,
            name=name,
            on_overlimit=on_overlimit,
            open_stat=open_stat,
            recheck=recheck,
            remove_tags=remove_tags,
            report_subscriptions=report_subscriptions,
            settings=settings,
            sla_target=sla_target,
            tags=tags,
            url=url,
        )

        return monitor_write_request
