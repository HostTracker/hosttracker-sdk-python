from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.webhook_patch_request_events_item import (
    WebhookPatchRequestEventsItem,
    check_webhook_patch_request_events_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_header import WebhookHeader
    from ..models.webhook_scope_all import WebhookScopeAll
    from ..models.webhook_scope_monitors import WebhookScopeMonitors
    from ..models.webhook_scope_tags import WebhookScopeTags
    from ..models.webhook_secret_rotate import WebhookSecretRotate


T = TypeVar("T", bound="WebhookPatchRequest")


@_attrs_define
class WebhookPatchRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    enabled: bool | Unset = UNSET
    """ Whether this is currently running. """
    events: list[WebhookPatchRequestEventsItem] | Unset = UNSET
    """ Which event types this webhook receives. There is no wildcard, and an empty list is refused - a webhook
    subscribed to nothing is a webhook that silently never fires. """
    headers: list[WebhookHeader] | Unset = UNSET
    """ Custom request headers sent with every delivery. An empty array clears them; omitting the member leaves them
    alone. They can never overwrite a signing header. """
    name: str | Unset = UNSET
    """ A display name. Never an identifier. """
    scope: Unset | WebhookScopeAll | WebhookScopeMonitors | WebhookScopeTags = UNSET
    """ Which monitors this webhook receives events for. Exactly ONE of the three forms - a scope that named two
    would be ambiguous about which one wins, so it is refused rather than resolved. """
    secret: str | Unset | WebhookSecretRotate = UNSET
    """ The signing secret. Its value is returned exactly once, at the moment it is set, and never again - store it
    when you see it. """
    url: str | Unset = UNSET
    """ Where deliveries are POSTed. An absolute http(s) url, not a bare host. """

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_scope_all import WebhookScopeAll
        from ..models.webhook_scope_monitors import WebhookScopeMonitors
        from ..models.webhook_secret_rotate import WebhookSecretRotate

        enabled = self.enabled

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item: str = events_item_data
                events.append(events_item)

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        name = self.name

        scope: dict[str, Any] | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        elif isinstance(self.scope, WebhookScopeAll):
            scope = self.scope.to_dict()
        elif isinstance(self.scope, WebhookScopeMonitors):
            scope = self.scope.to_dict()
        else:
            scope = self.scope.to_dict()

        secret: dict[str, Any] | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        elif isinstance(self.secret, WebhookSecretRotate):
            secret = self.secret.to_dict()
        else:
            secret = self.secret

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if events is not UNSET:
            field_dict["events"] = events
        if headers is not UNSET:
            field_dict["headers"] = headers
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if secret is not UNSET:
            field_dict["secret"] = secret
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_header import WebhookHeader
        from ..models.webhook_scope_all import WebhookScopeAll
        from ..models.webhook_scope_monitors import WebhookScopeMonitors
        from ..models.webhook_scope_tags import WebhookScopeTags
        from ..models.webhook_secret_rotate import WebhookSecretRotate

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _events = d.pop("events", UNSET)
        events: list[WebhookPatchRequestEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = check_webhook_patch_request_events_item(events_item_data)

                events.append(events_item)

        _headers = d.pop("headers", UNSET)
        headers: list[WebhookHeader] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = WebhookHeader.from_dict(headers_item_data)

                headers.append(headers_item)

        name = d.pop("name", UNSET)

        def _parse_scope(data: object) -> Unset | WebhookScopeAll | WebhookScopeMonitors | WebhookScopeTags:
            if isinstance(data, Unset):
                return data
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

        scope = _parse_scope(d.pop("scope", UNSET))

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

        url = d.pop("url", UNSET)

        webhook_patch_request = cls(
            enabled=enabled,
            events=events,
            headers=headers,
            name=name,
            scope=scope,
            secret=secret,
            url=url,
        )

        return webhook_patch_request
