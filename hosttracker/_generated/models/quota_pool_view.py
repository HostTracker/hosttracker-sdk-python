from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quota_window_view import QuotaWindowView


T = TypeVar("T", bound="QuotaPoolView")


@_attrs_define
class QuotaPoolView:
    """One metered pool. The two pools are metered independently: `ic` is the instant-check pool, `account` is everything
    else.

    """

    limit: int | None | Unset = UNSET
    """ The tightest-binding window's limit, or null when the pool has no configured quota. """
    used: int | None | Unset = UNSET
    remaining: int | None | Unset = UNSET
    reset_at: int | None | Unset = UNSET
    """ Unix seconds. """
    quotas: list[QuotaWindowView] | Unset = UNSET
    """ Every configured window of this pool - a pool routinely has more than one. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        quotas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotas, Unset):
            quotas = []
            for quotas_item_data in self.quotas:
                quotas_item = quotas_item_data.to_dict()
                quotas.append(quotas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if used is not UNSET:
            field_dict["used"] = used
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if reset_at is not UNSET:
            field_dict["resetAt"] = reset_at
        if quotas is not UNSET:
            field_dict["quotas"] = quotas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quota_window_view import QuotaWindowView

        d = dict(src_dict)

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

        _quotas = d.pop("quotas", UNSET)
        quotas: list[QuotaWindowView] | Unset = UNSET
        if _quotas is not UNSET:
            quotas = []
            for quotas_item_data in _quotas:
                quotas_item = QuotaWindowView.from_dict(quotas_item_data)

                quotas.append(quotas_item)

        quota_pool_view = cls(
            limit=limit,
            used=used,
            remaining=remaining,
            reset_at=reset_at,
            quotas=quotas,
        )

        quota_pool_view.additional_properties = d
        return quota_pool_view

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
