from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmationView")


@_attrs_define
class ConfirmationView:
    sent: bool
    tries_allowed: int
    channel: str | Unset = UNSET
    expires_at: int | None | Unset = UNSET
    """ Unix seconds. """
    reason: None | str | Unset = UNSET
    """ Why nothing was sent - a STABLE, documented machine token (snake_case) a client is meant to branch on, never
    internal prose. `overlimited` is a real state, not an error and not a silence. The failure tokens are:
    `insufficient_balance` (the account's SMS/voice balance could not cover the send - same vocabulary as the
    (currently unraised) `insufficient_balance` problem code, reused here for the same concept, one level down),
    `no_billing_profile` (the account has no billing profile so a paid channel could not be charged),
    `render_failed` (the message content could not be built), `billing_unavailable` (the billing subsystem was
    unreachable - infra, not a balance verdict), `delivery_suppressed` (this address had too many recent permanent
    delivery failures and is in a cooldown), `send_failed` (the transport rejected or could not attempt the send -
    the catch-all for every other transport-level outcome), `rate_limited`. """
    detail: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sent = self.sent

        tries_allowed = self.tries_allowed

        channel = self.channel

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sent": sent,
                "triesAllowed": tries_allowed,
            }
        )
        if channel is not UNSET:
            field_dict["channel"] = channel
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sent = d.pop("sent")

        tries_allowed = d.pop("triesAllowed")

        channel = d.pop("channel", UNSET)

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        confirmation_view = cls(
            sent=sent,
            tries_allowed=tries_allowed,
            channel=channel,
            expires_at=expires_at,
            reason=reason,
            detail=detail,
        )

        confirmation_view.additional_properties = d
        return confirmation_view

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
