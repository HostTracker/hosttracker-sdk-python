from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_view_state import MonitorViewState, check_monitor_view_state
from ..models.monitor_view_type import MonitorViewType, check_monitor_view_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_expiration_settings import CertificateExpirationSettings
    from ..models.database_check_settings import DatabaseCheckSettings
    from ..models.dnsbl_check_settings import DNSBLCheckSettings
    from ..models.domain_expiration_settings import DomainExpirationSettings
    from ..models.fast_check_https_settings import FastCheckHttpsSettings
    from ..models.maintenance_view import MaintenanceView
    from ..models.monitor_attached_view import MonitorAttachedView
    from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
    from ..models.monitor_disabled_span_view import MonitorDisabledSpanView
    from ..models.monitor_incident_view import MonitorIncidentView
    from ..models.monitor_locations_view import MonitorLocationsView
    from ..models.monitor_maintenance_span_view import MonitorMaintenanceSpanView
    from ..models.monitor_recheck_view import MonitorRecheckView
    from ..models.monitor_span_view import MonitorSpanView
    from ..models.monitor_subscription_view import MonitorSubscriptionView
    from ..models.monitor_view_attached_type_0 import MonitorViewAttachedType0
    from ..models.page_speed_settings import PageSpeedSettings
    from ..models.ping_check_settings import PingCheckSettings
    from ..models.result_view import ResultView
    from ..models.snmp_check_settings import SNMPCheckSettings
    from ..models.tcp_port_check_settings import TCPPortCheckSettings
    from ..models.text_analysis_settings import TextAnalysisSettings
    from ..models.transaction_check_settings import TransactionCheckSettings
    from ..models.web_content_check_settings import WebContentCheckSettings
    from ..models.web_risk_settings import WebRiskSettings


T = TypeVar("T", bound="MonitorView")


@_attrs_define
class MonitorView:
    id: UUID
    since: int
    """ When the current state began. Unix seconds. """
    enabled: bool
    """ The monitor's CONFIGURED enablement - the raw flag the owner set, not the effective one. A monitor that is
    enabled but suspended by a package limit reads `enabled: true` with `state: "paused"`: one concept per name, and
    the remediation is visible. """
    updated: int
    """ The value `updatedSince` compares against - `MAX(createTime, lastStateChange, disableDate)`. **⚠ This moves
    on creation and on STATE transitions. A configuration edit does not move it.** Exactly three things move it: the
    monitor's CREATION, an up/down transition, and an AUTOMATIC disable by the package-limit machinery. Nothing else
    does - not a rename, an interval change, a settings or a tag edit, and not a MANUAL pause or resume either: the
    third input is `disableDate`, which only the overlimit path ever writes, so switching a monitor off through the
    API leaves this value exactly where it was. The reason is the same for all of them - nothing in the database
    records when a change happened: `TaskSettings` has no modification timestamp (its only dates are `createTime`,
    `cronNextStart` and `statViewed`), and the `DirtyTaskIds` change marker carries an id and nothing else. The
    other half of the gap, for anyone building a delta sync on this: a DELETED monitor leaves no tombstone. It
    simply stops appearing, and a page that omits a row cannot be told apart from a filter that never matched it -
    so a client mirroring the account must reconcile against a full list periodically, or subscribe to
    `monitor.deleted`. So a sync loop built on `updatedSince` is **correct for state and incomplete for
    configuration**, and that is the published contract, stated here rather than hidden. """
    open_stat: bool
    """ Whether this monitor's statistics are publicly readable - the share switch behind the public stats page and
    the uptime badge. **Always emitted, list and item alike, and that is the point of this member**: it was accepted
    by `POST`/`PATCH /monitor` and published by no read, so a client could set the flag and never see it - a write-
    without-read hole, which makes any editor built on v2 unable to render the control it just wrote. It is a
    boolean column on a row this read already fetches, so emitting it costs nothing (the same argument that put
    `updated` and `created` in the always-present set). """
    full_log: bool
    """ Whether every check is recorded, rather than only the state CHANGES. """
    type_: MonitorViewType | Unset = UNSET
    """ The monitor type, from an OPEN vocabulary: 14 tokens today, and new ones may appear without a new API
    version. """
    name: None | str | Unset = UNSET
    url: str | Unset = UNSET
    """ The display identity. For a standalone DNSBL monitor the stored `!##f|a|m` suffix is STRIPPED. For a Counter
    monitor this is the display identity only: the DIALED endpoint is `settings.probeUrl` and the two are never
    substituted for one another. """
    effective_url: None | str | Unset = UNSET
    state: MonitorViewState | Unset = UNSET
    """ The monitor's current state: `up` | `down` | `paused` | `maintenance`. """
    tags: list[str] | Unset = UNSET
    created: int | None | Unset = UNSET
    """ When the monitor was created. Always present, on the list and on the item read alike - see the class remarks
    for why it is not part of `expand=settings` any more. Unix seconds. """
    cron_schedule: None | str | Unset = UNSET
    """ The monitor's cron expression, when it is cron-scheduled - the third member the write surface took and no
    read published. **Present exactly when the monitor HAS one**, and omitted otherwise rather than emitted as null:
    cron and `interval` are alternative schedules, and a cron-scheduled monitor legitimately carries `interval: 0`,
    so the member's PRESENCE is what says which schedule is in force. Cron is accepted for every type except the
    fixed-cadence ones (blacklist, certificate and domain expiry, web risk), whose cadence the service pins and
    which therefore never carry one. """
    expiration_date: int | None | Unset = UNSET
    """ When the thing this monitor watches EXPIRES - the certificate's `notAfter` for a `sslExp` monitor, the
    registration's expiry date for a `domainExp` one. Omitted for every other type, and for a monitor of those two
    types that has not produced a readable result yet. **It is the monitor's own subject, not a sub-check
    observation**, which is why it sits on the row: for these two types the expiry date IS what the monitor
    measures. An http monitor with a certificate or domain check ATTACHED reads the same information from the
    `sslExp`/`domainExp` blocks of `expand=attached`, where it is per-kind and unambiguous - this member would have
    to pick one of the two and would be a second spelling of a value the block already publishes. Unix seconds. """
    cert_not_before: int | None | Unset = UNSET
    """ When the watched certificate became valid - the issuance instant, so a client can render the elapsed
    fraction of a certificate's validity window rather than only the days left. `sslExp` monitors only, omitted when
    the stored observation does not carry one (it is additive: an observation made by an older agent build has no
    such field). Unix seconds. """
    interval: int | None | Unset = UNSET
    """ Check interval in SECONDS. """
    sla_target: float | None | Unset = UNSET
    locations: MonitorLocationsView | None | Unset = UNSET
    """ Where a monitor is checked from. Folds in `GET /Sites/{id}/agents/excluded`. """
    recheck: MonitorRecheckView | None | Unset = UNSET
    """ The recheck strategy - persisted inside the settings blob, a monitor-level concept on the wire. """
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
    attached: MonitorViewAttachedType0 | None | Unset = UNSET
    attached_results: MonitorAttachedView | None | Unset = UNSET
    subscription: list[MonitorSubscriptionView] | None | Unset = UNSET
    """ `expand=subscription` - the alert subscriptions on this monitor. An array despite the singular token, so
    field name and token match exactly. """
    last_incident: MonitorIncidentView | None | Unset = UNSET
    """ `expand=lastIncident` - the monitor's last up/down transition. """
    last_result: None | ResultView | Unset = UNSET
    uptime: float | None | Unset = UNSET
    """ `expand=uptime` - uptime PERCENT over the request's `from`/`to`. One stored-procedure run for the whole
    page, over the caller's window rather than a set of fixed windows. `null` when the window holds no data for this
    monitor. """
    spans: list[MonitorSpanView] | None | Unset = UNSET
    """ `expand=spans` - the up/down spans intersecting the request's window. """
    disabled_spans: list[MonitorDisabledSpanView] | None | Unset = UNSET
    """ `expand=spans` - the intervals inside the window during which the monitor was PAUSED, clipped to it. """
    maintenance_spans: list[MonitorMaintenanceSpanView] | None | Unset = UNSET
    """ `expand=spans` - the maintenance OCCURRENCES intersecting the window, clipped to it, each naming the window
    it comes from. """
    maintenance: list[MaintenanceView] | None | Unset = UNSET
    """ `expand=maintenance` - the maintenance windows COVERING this monitor, each as its window definition in
    exactly the shape `GET /maintenance` lists. Never materialized occurrences - a recurring window appears once.
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_expiration_settings import CertificateExpirationSettings
        from ..models.database_check_settings import DatabaseCheckSettings
        from ..models.dnsbl_check_settings import DNSBLCheckSettings
        from ..models.domain_expiration_settings import DomainExpirationSettings
        from ..models.fast_check_https_settings import FastCheckHttpsSettings
        from ..models.monitor_attached_view import MonitorAttachedView
        from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
        from ..models.monitor_incident_view import MonitorIncidentView
        from ..models.monitor_locations_view import MonitorLocationsView
        from ..models.monitor_recheck_view import MonitorRecheckView
        from ..models.monitor_view_attached_type_0 import MonitorViewAttachedType0
        from ..models.page_speed_settings import PageSpeedSettings
        from ..models.ping_check_settings import PingCheckSettings
        from ..models.result_view import ResultView
        from ..models.snmp_check_settings import SNMPCheckSettings
        from ..models.tcp_port_check_settings import TCPPortCheckSettings
        from ..models.text_analysis_settings import TextAnalysisSettings
        from ..models.web_content_check_settings import WebContentCheckSettings
        from ..models.web_risk_settings import WebRiskSettings

        id = str(self.id)

        since = self.since

        enabled = self.enabled

        updated = self.updated

        open_stat = self.open_stat

        full_log = self.full_log

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        url = self.url

        effective_url: None | str | Unset
        if isinstance(self.effective_url, Unset):
            effective_url = UNSET
        else:
            effective_url = self.effective_url

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        created: int | None | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        else:
            created = self.created

        cron_schedule: None | str | Unset
        if isinstance(self.cron_schedule, Unset):
            cron_schedule = UNSET
        else:
            cron_schedule = self.cron_schedule

        expiration_date: int | None | Unset
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = self.expiration_date

        cert_not_before: int | None | Unset
        if isinstance(self.cert_not_before, Unset):
            cert_not_before = UNSET
        else:
            cert_not_before = self.cert_not_before

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
        elif isinstance(self.attached, MonitorViewAttachedType0):
            attached = self.attached.to_dict()
        else:
            attached = self.attached

        attached_results: dict[str, Any] | None | Unset
        if isinstance(self.attached_results, Unset):
            attached_results = UNSET
        elif isinstance(self.attached_results, MonitorAttachedView):
            attached_results = self.attached_results.to_dict()
        else:
            attached_results = self.attached_results

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

        last_result: dict[str, Any] | None | Unset
        if isinstance(self.last_result, Unset):
            last_result = UNSET
        elif isinstance(self.last_result, ResultView):
            last_result = self.last_result.to_dict()
        else:
            last_result = self.last_result

        uptime: float | None | Unset
        if isinstance(self.uptime, Unset):
            uptime = UNSET
        else:
            uptime = self.uptime

        spans: list[dict[str, Any]] | None | Unset
        if isinstance(self.spans, Unset):
            spans = UNSET
        elif isinstance(self.spans, list):
            spans = []
            for spans_type_0_item_data in self.spans:
                spans_type_0_item = spans_type_0_item_data.to_dict()
                spans.append(spans_type_0_item)

        else:
            spans = self.spans

        disabled_spans: list[dict[str, Any]] | None | Unset
        if isinstance(self.disabled_spans, Unset):
            disabled_spans = UNSET
        elif isinstance(self.disabled_spans, list):
            disabled_spans = []
            for disabled_spans_type_0_item_data in self.disabled_spans:
                disabled_spans_type_0_item = disabled_spans_type_0_item_data.to_dict()
                disabled_spans.append(disabled_spans_type_0_item)

        else:
            disabled_spans = self.disabled_spans

        maintenance_spans: list[dict[str, Any]] | None | Unset
        if isinstance(self.maintenance_spans, Unset):
            maintenance_spans = UNSET
        elif isinstance(self.maintenance_spans, list):
            maintenance_spans = []
            for maintenance_spans_type_0_item_data in self.maintenance_spans:
                maintenance_spans_type_0_item = maintenance_spans_type_0_item_data.to_dict()
                maintenance_spans.append(maintenance_spans_type_0_item)

        else:
            maintenance_spans = self.maintenance_spans

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
                "since": since,
                "enabled": enabled,
                "updated": updated,
                "openStat": open_stat,
                "fullLog": full_log,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if effective_url is not UNSET:
            field_dict["effectiveUrl"] = effective_url
        if state is not UNSET:
            field_dict["state"] = state
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created is not UNSET:
            field_dict["created"] = created
        if cron_schedule is not UNSET:
            field_dict["cronSchedule"] = cron_schedule
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if cert_not_before is not UNSET:
            field_dict["certNotBefore"] = cert_not_before
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
        if attached_results is not UNSET:
            field_dict["attachedResults"] = attached_results
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if last_incident is not UNSET:
            field_dict["lastIncident"] = last_incident
        if last_result is not UNSET:
            field_dict["lastResult"] = last_result
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if spans is not UNSET:
            field_dict["spans"] = spans
        if disabled_spans is not UNSET:
            field_dict["disabledSpans"] = disabled_spans
        if maintenance_spans is not UNSET:
            field_dict["maintenanceSpans"] = maintenance_spans
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
        from ..models.monitor_attached_view import MonitorAttachedView
        from ..models.monitor_cpuramhdd_settings import MonitorCPURAMHDDSettings
        from ..models.monitor_disabled_span_view import MonitorDisabledSpanView
        from ..models.monitor_incident_view import MonitorIncidentView
        from ..models.monitor_locations_view import MonitorLocationsView
        from ..models.monitor_maintenance_span_view import MonitorMaintenanceSpanView
        from ..models.monitor_recheck_view import MonitorRecheckView
        from ..models.monitor_span_view import MonitorSpanView
        from ..models.monitor_subscription_view import MonitorSubscriptionView
        from ..models.monitor_view_attached_type_0 import MonitorViewAttachedType0
        from ..models.page_speed_settings import PageSpeedSettings
        from ..models.ping_check_settings import PingCheckSettings
        from ..models.result_view import ResultView
        from ..models.snmp_check_settings import SNMPCheckSettings
        from ..models.tcp_port_check_settings import TCPPortCheckSettings
        from ..models.text_analysis_settings import TextAnalysisSettings
        from ..models.transaction_check_settings import TransactionCheckSettings
        from ..models.web_content_check_settings import WebContentCheckSettings
        from ..models.web_risk_settings import WebRiskSettings

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        since = d.pop("since")

        enabled = d.pop("enabled")

        updated = d.pop("updated")

        open_stat = d.pop("openStat")

        full_log = d.pop("fullLog")

        _type_ = d.pop("type", UNSET)
        type_: MonitorViewType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_monitor_view_type(_type_)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        url = d.pop("url", UNSET)

        def _parse_effective_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_url = _parse_effective_url(d.pop("effectiveUrl", UNSET))

        _state = d.pop("state", UNSET)
        state: MonitorViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_monitor_view_state(_state)

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_created(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        def _parse_cron_schedule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cron_schedule = _parse_cron_schedule(d.pop("cronSchedule", UNSET))

        def _parse_expiration_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        def _parse_cert_not_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cert_not_before = _parse_cert_not_before(d.pop("certNotBefore", UNSET))

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

        def _parse_attached(data: object) -> MonitorViewAttachedType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attached_type_0 = MonitorViewAttachedType0.from_dict(data)

                return attached_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorViewAttachedType0 | None | Unset, data)

        attached = _parse_attached(d.pop("attached", UNSET))

        def _parse_attached_results(data: object) -> MonitorAttachedView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attached_results_type_0 = MonitorAttachedView.from_dict(data)

                return attached_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorAttachedView | None | Unset, data)

        attached_results = _parse_attached_results(d.pop("attachedResults", UNSET))

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

        def _parse_last_result(data: object) -> None | ResultView | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_result_type_0 = ResultView.from_dict(data)

                return last_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultView | Unset, data)

        last_result = _parse_last_result(d.pop("lastResult", UNSET))

        def _parse_uptime(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        uptime = _parse_uptime(d.pop("uptime", UNSET))

        def _parse_spans(data: object) -> list[MonitorSpanView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                spans_type_0 = []
                _spans_type_0 = data
                for spans_type_0_item_data in _spans_type_0:
                    spans_type_0_item = MonitorSpanView.from_dict(spans_type_0_item_data)

                    spans_type_0.append(spans_type_0_item)

                return spans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonitorSpanView] | None | Unset, data)

        spans = _parse_spans(d.pop("spans", UNSET))

        def _parse_disabled_spans(data: object) -> list[MonitorDisabledSpanView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                disabled_spans_type_0 = []
                _disabled_spans_type_0 = data
                for disabled_spans_type_0_item_data in _disabled_spans_type_0:
                    disabled_spans_type_0_item = MonitorDisabledSpanView.from_dict(disabled_spans_type_0_item_data)

                    disabled_spans_type_0.append(disabled_spans_type_0_item)

                return disabled_spans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonitorDisabledSpanView] | None | Unset, data)

        disabled_spans = _parse_disabled_spans(d.pop("disabledSpans", UNSET))

        def _parse_maintenance_spans(data: object) -> list[MonitorMaintenanceSpanView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                maintenance_spans_type_0 = []
                _maintenance_spans_type_0 = data
                for maintenance_spans_type_0_item_data in _maintenance_spans_type_0:
                    maintenance_spans_type_0_item = MonitorMaintenanceSpanView.from_dict(
                        maintenance_spans_type_0_item_data
                    )

                    maintenance_spans_type_0.append(maintenance_spans_type_0_item)

                return maintenance_spans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonitorMaintenanceSpanView] | None | Unset, data)

        maintenance_spans = _parse_maintenance_spans(d.pop("maintenanceSpans", UNSET))

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

        monitor_view = cls(
            id=id,
            since=since,
            enabled=enabled,
            updated=updated,
            open_stat=open_stat,
            full_log=full_log,
            type_=type_,
            name=name,
            url=url,
            effective_url=effective_url,
            state=state,
            tags=tags,
            created=created,
            cron_schedule=cron_schedule,
            expiration_date=expiration_date,
            cert_not_before=cert_not_before,
            interval=interval,
            sla_target=sla_target,
            locations=locations,
            recheck=recheck,
            settings=settings,
            attached=attached,
            attached_results=attached_results,
            subscription=subscription,
            last_incident=last_incident,
            last_result=last_result,
            uptime=uptime,
            spans=spans,
            disabled_spans=disabled_spans,
            maintenance_spans=maintenance_spans,
            maintenance=maintenance,
        )

        monitor_view.additional_properties = d
        return monitor_view

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
