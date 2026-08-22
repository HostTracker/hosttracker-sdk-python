from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_quota_view_pools import AccountQuotaViewPools
    from ..models.quota_scope_view import QuotaScopeView


T = TypeVar("T", bound="AccountQuotaView")


@_attrs_define
class AccountQuotaView:
    api_enabled: bool
    """ **Whether the account is entitled to use the API at all** - the same flag `GET /account` publishes as
    `flags.apiEnabled`, repeated here because this is the document a client reads when it is asking "may I, and how
    much" and the two halves of that question should not need two calls. **It never blocks this read.** An
    unentitled account gets its 200 and whatever quota rows it has - which is usually none, and "no rows" is exactly
    the state that used to be indistinguishable from a bug. """
    limit: int | None | Unset = UNSET
    """ The tightest-binding window across both pools, or null when nothing is metered. """
    used: int | None | Unset = UNSET
    remaining: int | None | Unset = UNSET
    reset_at: int | None | Unset = UNSET
    """ Unix seconds. """
    pools: AccountQuotaViewPools | Unset = UNSET
    token_cap: int | None | Unset = UNSET
    """ The calling token's optional self-cap: the effective bound is `min(userQuota, tokenCap)`. Omitted for a
    cookie session or a token that carries none. """
    scopes: list[QuotaScopeView] | Unset = UNSET
    """ The scope vocabulary a token may be minted with - the same declarative registry the mint validates against,
    so "which token do I need" is answerable from this one read. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_enabled = self.api_enabled

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        used: int | None | Unset
        if isinstance(self.used, Unset):
            used = UNSET
        else:
            used = self.used

        remaining: int | None | Unset
        if isinstance(self.remaining, Unset):
            remaining = UNSET
        else:
            remaining = self.remaining

        reset_at: int | None | Unset
        if isinstance(self.reset_at, Unset):
            reset_at = UNSET
        else:
            reset_at = self.reset_at

        pools: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pools, Unset):
            pools = self.pools.to_dict()

        token_cap: int | None | Unset
        if isinstance(self.token_cap, Unset):
            token_cap = UNSET
        else:
            token_cap = self.token_cap

        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiEnabled": api_enabled,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if used is not UNSET:
            field_dict["used"] = used
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if reset_at is not UNSET:
            field_dict["resetAt"] = reset_at
        if pools is not UNSET:
            field_dict["pools"] = pools
        if token_cap is not UNSET:
            field_dict["tokenCap"] = token_cap
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_quota_view_pools import AccountQuotaViewPools
        from ..models.quota_scope_view import QuotaScopeView

        d = dict(src_dict)
        api_enabled = d.pop("apiEnabled")

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_used(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used = _parse_used(d.pop("used", UNSET))

        def _parse_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remaining = _parse_remaining(d.pop("remaining", UNSET))

        def _parse_reset_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reset_at = _parse_reset_at(d.pop("resetAt", UNSET))

        _pools = d.pop("pools", UNSET)
        pools: AccountQuotaViewPools | Unset
        if isinstance(_pools, Unset):
            pools = UNSET
        else:
            pools = AccountQuotaViewPools.from_dict(_pools)

        def _parse_token_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        token_cap = _parse_token_cap(d.pop("tokenCap", UNSET))

        _scopes = d.pop("scopes", UNSET)
        scopes: list[QuotaScopeView] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = QuotaScopeView.from_dict(scopes_item_data)

                scopes.append(scopes_item)

        account_quota_view = cls(
            api_enabled=api_enabled,
            limit=limit,
            used=used,
            remaining=remaining,
            reset_at=reset_at,
            pools=pools,
            token_cap=token_cap,
            scopes=scopes,
        )

        account_quota_view.additional_properties = d
        return account_quota_view

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
