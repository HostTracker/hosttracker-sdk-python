from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_badges_view import AccountBadgesView
    from ..models.account_flags_view import AccountFlagsView
    from ..models.account_limits_view import AccountLimitsView
    from ..models.account_package_view import AccountPackageView
    from ..models.account_profile_view import AccountProfileView
    from ..models.account_quota_view import AccountQuotaView
    from ..models.account_usage_view import AccountUsageView
    from ..models.account_view_default_agent_pools import AccountViewDefaultAgentPools


T = TypeVar("T", bound="AccountView")


@_attrs_define
class AccountView:
    id: UUID
    login: None | str | Unset = UNSET
    timezone: str | Unset = UNSET
    """ IANA zone id (rule: v2 uses IANA directly and publishes no timezone-translation endpoint). Storage keeps a
    WINDOWS id, converted here; an id that does not convert is passed through unchanged rather than replaced with a
    wrong zone. """
    language: None | str | Unset = UNSET
    """ The account's UI language, ISO 639-1 where the app's code maps to one. """
    profile: AccountProfileView | Unset = UNSET
    default_agent_pools: AccountViewDefaultAgentPools | Unset = UNSET
    """ **The monitoring locations a new monitor of each service type starts with**, keyed by the service type's
    wire token (`net`, `waterfall`, `internal`) and valued with that type's default pool ids - a pool id, an agent
    id, or an agent id prefixed `-` to exclude it from an otherwise selected pool. Empty when the account has never
    chosen one, in which case a create falls back to the platform default. It is the same map `GET /agent/pool`
    publishes on its envelope as `defaults`, in the same spelling - one fact, one vocabulary - and it is here
    because it is WRITABLE through `PATCH /account` and a client should be able to read what it is about to change
    from the resource that owns it. ⚠ **The keys are the lowerCamel service-type tokens this surface publishes
    everywhere else** (`net`), not the storage enum names the first-party `GET /user` returns (`Net`). Two spellings
    of one vocabulary is the defect this surface is built to avoid, and the v2 half of it was already spelled this
    way. """
    flags: AccountFlagsView | Unset = UNSET
    package: AccountPackageView | Unset = UNSET
    usage: AccountUsageView | Unset = UNSET
    overlimits: list[str] | Unset = UNSET
    """ WHICH account-level overlimit bits are set - `task`, `contact`, `report`, `maintenance`. Empty when the
    account is inside its package. """
    limits: AccountLimitsView | Unset = UNSET
    badges: AccountBadgesView | Unset = UNSET
    quota: AccountQuotaView | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account_quota_view import AccountQuotaView

        id = str(self.id)

        login: None | str | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        timezone = self.timezone

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        default_agent_pools: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_agent_pools, Unset):
            default_agent_pools = self.default_agent_pools.to_dict()

        flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags.to_dict()

        package: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        overlimits: list[str] | Unset = UNSET
        if not isinstance(self.overlimits, Unset):
            overlimits = self.overlimits

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        badges: dict[str, Any] | Unset = UNSET
        if not isinstance(self.badges, Unset):
            badges = self.badges.to_dict()

        quota: dict[str, Any] | None | Unset
        if isinstance(self.quota, Unset):
            quota = UNSET
        elif isinstance(self.quota, AccountQuotaView):
            quota = self.quota.to_dict()
        else:
            quota = self.quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if login is not UNSET:
            field_dict["login"] = login
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if language is not UNSET:
            field_dict["language"] = language
        if profile is not UNSET:
            field_dict["profile"] = profile
        if default_agent_pools is not UNSET:
            field_dict["defaultAgentPools"] = default_agent_pools
        if flags is not UNSET:
            field_dict["flags"] = flags
        if package is not UNSET:
            field_dict["package"] = package
        if usage is not UNSET:
            field_dict["usage"] = usage
        if overlimits is not UNSET:
            field_dict["overlimits"] = overlimits
        if limits is not UNSET:
            field_dict["limits"] = limits
        if badges is not UNSET:
            field_dict["badges"] = badges
        if quota is not UNSET:
            field_dict["quota"] = quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_badges_view import AccountBadgesView
        from ..models.account_flags_view import AccountFlagsView
        from ..models.account_limits_view import AccountLimitsView
        from ..models.account_package_view import AccountPackageView
        from ..models.account_profile_view import AccountProfileView
        from ..models.account_quota_view import AccountQuotaView
        from ..models.account_usage_view import AccountUsageView
        from ..models.account_view_default_agent_pools import AccountViewDefaultAgentPools

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login = _parse_login(d.pop("login", UNSET))

        timezone = d.pop("timezone", UNSET)

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        _profile = d.pop("profile", UNSET)
        profile: AccountProfileView | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = AccountProfileView.from_dict(_profile)

        _default_agent_pools = d.pop("defaultAgentPools", UNSET)
        default_agent_pools: AccountViewDefaultAgentPools | Unset
        if isinstance(_default_agent_pools, Unset):
            default_agent_pools = UNSET
        else:
            default_agent_pools = AccountViewDefaultAgentPools.from_dict(_default_agent_pools)

        _flags = d.pop("flags", UNSET)
        flags: AccountFlagsView | Unset
        if isinstance(_flags, Unset):
            flags = UNSET
        else:
            flags = AccountFlagsView.from_dict(_flags)

        _package = d.pop("package", UNSET)
        package: AccountPackageView | Unset
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = AccountPackageView.from_dict(_package)

        _usage = d.pop("usage", UNSET)
        usage: AccountUsageView | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = AccountUsageView.from_dict(_usage)

        overlimits = cast(list[str], d.pop("overlimits", UNSET))

        _limits = d.pop("limits", UNSET)
        limits: AccountLimitsView | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = AccountLimitsView.from_dict(_limits)

        _badges = d.pop("badges", UNSET)
        badges: AccountBadgesView | Unset
        if isinstance(_badges, Unset):
            badges = UNSET
        else:
            badges = AccountBadgesView.from_dict(_badges)

        def _parse_quota(data: object) -> AccountQuotaView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quota_type_0 = AccountQuotaView.from_dict(data)

                return quota_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountQuotaView | None | Unset, data)

        quota = _parse_quota(d.pop("quota", UNSET))

        account_view = cls(
            id=id,
            login=login,
            timezone=timezone,
            language=language,
            profile=profile,
            default_agent_pools=default_agent_pools,
            flags=flags,
            package=package,
            usage=usage,
            overlimits=overlimits,
            limits=limits,
            badges=badges,
            quota=quota,
        )

        account_view.additional_properties = d
        return account_view

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
