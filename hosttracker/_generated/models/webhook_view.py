from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_header_view import WebhookHeaderView
    from ..models.webhook_scope_view import WebhookScopeView
    from ..models.webhook_secret_view import WebhookSecretView


T = TypeVar("T", bound="WebhookView")


@_attrs_define
class WebhookView:
    id: UUID
    enabled: bool
    consecutive_failures: int
    created: int
    """ The contact row's creation instant. Unix seconds. """
    updated: int
    url: str | Unset = UNSET
    events: list[str] | Unset = UNSET
    scope: WebhookScopeView | Unset = UNSET
    """ The webhook's `scope` - exactly ONE of `{all:true}` / `{monitorIds:[…]}` / `{tags:[…]}`. An omitted monitor
    list cannot be allowed to mean "none" (an account-wide webhook would be unexpressible) OR "all", so the third
    state is spelled out. """
    name: None | str | Unset = UNSET
    disabled_reason: None | str | Unset = UNSET
    """ `deliveryFailure` / `gone` when the SYSTEM disabled it; absent when the user did. """
    last_delivery_at: int | None | Unset = UNSET
    """ Unix seconds. """
    headers: list[WebhookHeaderView] | None | Unset = UNSET
    """ The custom request headers every delivery carries, when any are configured. """
    secret: WebhookSecretView | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        enabled = self.enabled

        consecutive_failures = self.consecutive_failures

        created = self.created

        updated = self.updated

        url = self.url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        disabled_reason: None | str | Unset
        if isinstance(self.disabled_reason, Unset):
            disabled_reason = UNSET
        else:
            disabled_reason = self.disabled_reason

        last_delivery_at: int | None | Unset
        if isinstance(self.last_delivery_at, Unset):
            last_delivery_at = UNSET
        else:
            last_delivery_at = self.last_delivery_at

        headers: list[dict[str, Any]] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, list):
            headers = []
            for headers_type_0_item_data in self.headers:
                headers_type_0_item = headers_type_0_item_data.to_dict()
                headers.append(headers_type_0_item)

        else:
            headers = self.headers

        secret: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "enabled": enabled,
                "consecutiveFailures": consecutive_failures,
                "created": created,
                "updated": updated,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if events is not UNSET:
            field_dict["events"] = events
        if scope is not UNSET:
            field_dict["scope"] = scope
        if name is not UNSET:
            field_dict["name"] = name
        if disabled_reason is not UNSET:
            field_dict["disabledReason"] = disabled_reason
        if last_delivery_at is not UNSET:
            field_dict["lastDeliveryAt"] = last_delivery_at
        if headers is not UNSET:
            field_dict["headers"] = headers
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_header_view import WebhookHeaderView
        from ..models.webhook_scope_view import WebhookScopeView
        from ..models.webhook_secret_view import WebhookSecretView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        enabled = d.pop("enabled")

        consecutive_failures = d.pop("consecutiveFailures")

        created = d.pop("created")

        updated = d.pop("updated")

        url = d.pop("url", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        _scope = d.pop("scope", UNSET)
        scope: WebhookScopeView | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = WebhookScopeView.from_dict(_scope)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_disabled_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabledReason", UNSET))

        def _parse_last_delivery_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("lastDeliveryAt", UNSET))

        def _parse_headers(data: object) -> list[WebhookHeaderView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                headers_type_0 = []
                _headers_type_0 = data
                for headers_type_0_item_data in _headers_type_0:
                    headers_type_0_item = WebhookHeaderView.from_dict(headers_type_0_item_data)

                    headers_type_0.append(headers_type_0_item)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WebhookHeaderView] | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        _secret = d.pop("secret", UNSET)
        secret: WebhookSecretView | Unset
        if isinstance(_secret, Unset):
            secret = UNSET
        else:
            secret = WebhookSecretView.from_dict(_secret)

        webhook_view = cls(
            id=id,
            enabled=enabled,
            consecutive_failures=consecutive_failures,
            created=created,
            updated=updated,
            url=url,
            events=events,
            scope=scope,
            name=name,
            disabled_reason=disabled_reason,
            last_delivery_at=last_delivery_at,
            headers=headers,
            secret=secret,
        )

        webhook_view.additional_properties = d
        return webhook_view

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
