from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_type_account_limits import MonitorTypeAccountLimits


T = TypeVar("T", bound="MonitorTypeRow")


@_attrs_define
class MonitorTypeRow:
    creatable: bool
    """ Always true. """
    attachable: bool
    """ True for the four dual-natured sub-checks, which can also ride on a parent monitor. """
    min_interval: int
    """ The type's interval floor in SECONDS. """
    requires_pool: bool
    """ True when a create is refused without `locations.pools`. """
    type_: str | Unset = UNSET
    label: str | Unset = UNSET
    fixed_interval: int | None | Unset = UNSET
    """ The cadence this type is PINNED to, in seconds - present only for the types the product schedules itself
    (the blacklist, certificate-expiry, domain-expiry and web-risk checks). For those, an `interval` is neither
    required on create nor honoured: omit it and the monitor is created at this cadence. Omitted for every type
    whose interval the account chooses, where `minInterval` is the floor to pick above. """
    entitlement: None | str | Unset = UNSET
    """ The package entitlement gating the type, or null. Always present - explicitly `null` rather than omitted, so
    a client can test the field without first testing that it exists. """
    presets: list[str] | Unset = UNSET
    """ Server-built settings presets. Http publishes `["bl:ru"]`; every other type is `[]`. """
    attachable_to: list[str] | None | Unset = UNSET
    """ The parent types this sub-check attaches to. Omitted when the type is not attachable. """
    account_limits: MonitorTypeAccountLimits | None | Unset = UNSET
    """ The CALLER'S account-specific limits for this type - present only when the request carried a credential; the
    catalogue itself stays global and anonymous. Settable (not init) because enrichment stamps it onto rows the
    static catalogue builder already produced. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_type_account_limits import MonitorTypeAccountLimits

        creatable = self.creatable

        attachable = self.attachable

        min_interval = self.min_interval

        requires_pool = self.requires_pool

        type_ = self.type_

        label = self.label

        fixed_interval: int | None | Unset
        if isinstance(self.fixed_interval, Unset):
            fixed_interval = UNSET
        else:
            fixed_interval = self.fixed_interval

        entitlement: None | str | Unset
        if isinstance(self.entitlement, Unset):
            entitlement = UNSET
        else:
            entitlement = self.entitlement

        presets: list[str] | Unset = UNSET
        if not isinstance(self.presets, Unset):
            presets = self.presets

        attachable_to: list[str] | None | Unset
        if isinstance(self.attachable_to, Unset):
            attachable_to = UNSET
        elif isinstance(self.attachable_to, list):
            attachable_to = self.attachable_to

        else:
            attachable_to = self.attachable_to

        account_limits: dict[str, Any] | None | Unset
        if isinstance(self.account_limits, Unset):
            account_limits = UNSET
        elif isinstance(self.account_limits, MonitorTypeAccountLimits):
            account_limits = self.account_limits.to_dict()
        else:
            account_limits = self.account_limits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creatable": creatable,
                "attachable": attachable,
                "minInterval": min_interval,
                "requiresPool": requires_pool,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if fixed_interval is not UNSET:
            field_dict["fixedInterval"] = fixed_interval
        if entitlement is not UNSET:
            field_dict["entitlement"] = entitlement
        if presets is not UNSET:
            field_dict["presets"] = presets
        if attachable_to is not UNSET:
            field_dict["attachableTo"] = attachable_to
        if account_limits is not UNSET:
            field_dict["accountLimits"] = account_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_type_account_limits import MonitorTypeAccountLimits

        d = dict(src_dict)
        creatable = d.pop("creatable")

        attachable = d.pop("attachable")

        min_interval = d.pop("minInterval")

        requires_pool = d.pop("requiresPool")

        type_ = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        def _parse_fixed_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fixed_interval = _parse_fixed_interval(d.pop("fixedInterval", UNSET))

        def _parse_entitlement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entitlement = _parse_entitlement(d.pop("entitlement", UNSET))

        presets = cast(list[str], d.pop("presets", UNSET))

        def _parse_attachable_to(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachable_to_type_0 = cast(list[str], data)

                return attachable_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        attachable_to = _parse_attachable_to(d.pop("attachableTo", UNSET))

        def _parse_account_limits(data: object) -> MonitorTypeAccountLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                account_limits_type_0 = MonitorTypeAccountLimits.from_dict(data)

                return account_limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorTypeAccountLimits | None | Unset, data)

        account_limits = _parse_account_limits(d.pop("accountLimits", UNSET))

        monitor_type_row = cls(
            creatable=creatable,
            attachable=attachable,
            min_interval=min_interval,
            requires_pool=requires_pool,
            type_=type_,
            label=label,
            fixed_interval=fixed_interval,
            entitlement=entitlement,
            presets=presets,
            attachable_to=attachable_to,
            account_limits=account_limits,
        )

        monitor_type_row.additional_properties = d
        return monitor_type_row

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
