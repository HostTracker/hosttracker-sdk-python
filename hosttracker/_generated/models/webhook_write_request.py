from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.webhook_write_request_events_item import (
    WebhookWriteRequestEventsItem,
    check_webhook_write_request_events_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_header import WebhookHeader
    from ..models.webhook_scope_all import WebhookScopeAll
    from ..models.webhook_scope_monitors import WebhookScopeMonitors
    from ..models.webhook_scope_tags import WebhookScopeTags
    from ..models.webhook_secret_rotate import WebhookSecretRotate


T = TypeVar("T", bound="WebhookWriteRequest")


@_attrs_define
class WebhookWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    events: list[WebhookWriteRequestEventsItem]
    """ Which event types this webhook receives. There is no wildcard, and an empty list is refused - a webhook
    subscribed to nothing is a webhook that silently never fires. """
    scope: WebhookScopeAll | WebhookScopeMonitors | WebhookScopeTags
    """ Which monitors this webhook receives events for. Exactly ONE of the three forms - a scope that named two
    would be ambiguous about which one wins, so it is refused rather than resolved. """
    url: str
    """ Where deliveries are POSTed. An absolute http(s) url, not a bare host. """
    enabled: bool | Unset = UNSET
    """ Whether this is currently running. """
    headers: list[WebhookHeader] | Unset = UNSET
    """ Custom request headers sent with every delivery. An empty array clears them; omitting the member leaves them
    alone. They can never overwrite a signing header. """
    name: str | Unset = UNSET
    """ A display name. Never an identifier. """
    secret: str | Unset | WebhookSecretRotate = UNSET
    """ The signing secret. Its value is returned exactly once, at the moment it is set, and never again - store it
    when you see it. """

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_scope_all import WebhookScopeAll
        from ..models.webhook_scope_monitors import WebhookScopeMonitors
        from ..models.webhook_secret_rotate import WebhookSecretRotate

        events = []
        for events_item_data in self.events:
            events_item: str = events_item_data
            events.append(events_item)

        scope: dict[str, Any]
        if isinstance(self.scope, WebhookScopeAll):
            scope = self.scope.to_dict()
        elif isinstance(self.scope, WebhookScopeMonitors):
            scope = self.scope.to_dict()
        else:
            scope = self.scope.to_dict()

        url = self.url

        enabled = self.enabled

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        name = self.name

        secret: dict[str, Any] | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        elif isinstance(self.secret, WebhookSecretRotate):
            secret = self.secret.to_dict()
        else:
            secret = self.secret

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "scope": scope,
                "url": url,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if headers is not UNSET:
            field_dict["headers"] = headers
        if name is not UNSET:
            field_dict["name"] = name
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_header import WebhookHeader
        from ..models.webhook_scope_all import WebhookScopeAll
        from ..models.webhook_scope_monitors import WebhookScopeMonitors
        from ..models.webhook_scope_tags import WebhookScopeTags
        from ..models.webhook_secret_rotate import WebhookSecretRotate

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = check_webhook_write_request_events_item(events_item_data)

            events.append(events_item)

        def _parse_scope(data: object) -> WebhookScopeAll | WebhookScopeMonitors | WebhookScopeTags:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scope_type_0 = WebhookScopeAll.from_dict(data)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scope_type_1 = WebhookScopeMonitors.from_dict(data)

                return scope_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            scope_type_2 = WebhookScopeTags.from_dict(data)

            return scope_type_2

        scope = _parse_scope(d.pop("scope"))

        url = d.pop("url")

        enabled = d.pop("enabled", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: list[WebhookHeader] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = WebhookHeader.from_dict(headers_item_data)

                headers.append(headers_item)

        name = d.pop("name", UNSET)

        def _parse_secret(data: object) -> str | Unset | WebhookSecretRotate:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_type_1 = WebhookSecretRotate.from_dict(data)

                return secret_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | Unset | WebhookSecretRotate, data)

        secret = _parse_secret(d.pop("secret", UNSET))

        webhook_write_request = cls(
            events=events,
            scope=scope,
            url=url,
            enabled=enabled,
            headers=headers,
            name=name,
            secret=secret,
        )

        return webhook_write_request
