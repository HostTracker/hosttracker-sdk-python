from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.contact_patch_request_type import ContactPatchRequestType, check_contact_patch_request_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_active_period import ContactActivePeriod
    from ..models.contact_alert_subscription import ContactAlertSubscription
    from ..models.contact_default_subscriptions import ContactDefaultSubscriptions
    from ..models.contact_http_header import ContactHttpHeader
    from ..models.contact_push_subscription import ContactPushSubscription
    from ..models.contact_report_subscription import ContactReportSubscription
    from ..models.contact_template import ContactTemplate


T = TypeVar("T", bound="ContactPatchRequest")


@_attrs_define
class ContactPatchRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    active_period: ContactActivePeriod | Unset = UNSET
    """ The daily window during which this contact accepts delivery. Send null to remove the restriction, which is
    also the default: every day, all day. """
    address: str | Unset = UNSET
    """ Where a notification is delivered, validated per `type`: an email address for `email`, a phone number for
    `sms` and `voiceCall`, an http(s) url for `http`. Required for those four and refused for `webPush`, which is
    reached through its push subscription and stores no address. Changing it on an existing contact clears its
    confirmation and sends a fresh code. """
    alert_delay: int | Unset = UNSET
    """ How long a failure must persist before this contact hears about it, in MINUTES. """
    alert_subscriptions: list[ContactAlertSubscription] | Unset = UNSET
    """ Alert subscriptions to wire up in the same request. """
    billing_notifications: bool | Unset = UNSET
    """ Send this contact the account's billing notices. """
    default_subscriptions: ContactDefaultSubscriptions | Unset = UNSET
    """ Wire this contact to every monitor the account has, without listing them. """
    gateway: str | Unset = UNSET
    """ Which delivery gateway carries the message, for types that offer a choice. """
    grouped_alerts: bool | Unset = UNSET
    """ Collapse simultaneous alerts for this contact into one message rather than one per monitor. """
    http_headers: list[ContactHttpHeader] | Unset = UNSET
    """ Extra headers to send. `http` contacts only. """
    language: str | Unset = UNSET
    """ The language notifications are rendered in. Send null to fall back to the account's. """
    mime_type: str | Unset = UNSET
    """ The content type a webhook-style delivery is posted with. `http` contacts only; defaults to
    `application/json`. """
    name: str | Unset = UNSET
    """ A display name. Never an identifier. """
    push_subscription: ContactPushSubscription | Unset = UNSET
    """ The browser push subscription a `webPush` contact is created from - the three values the Push API hands a
    page: the subscription's endpoint and its two keys. Required for `webPush` and refused for every other type. The
    server pushes a verification message to the endpoint before the contact is written, so an unreachable
    subscription is refused rather than stored. Create only: pointing a contact at another browser is a new contact,
    not an edit. It is never returned by a read - the stored subscription is named by the contact's `botId`. """
    report_subscriptions: list[ContactReportSubscription] | Unset = UNSET
    """ Report subscriptions to wire up in the same request. """
    send_news: bool | Unset = UNSET
    """ Send this contact product news. """
    templates: list[ContactTemplate] | Unset = UNSET
    """ Per-event message templates. Applied only to `http` contacts today. """
    type_: ContactPatchRequestType | Unset = UNSET
    """ Which kind of contact this is. It fixes how the contact is addressed and cannot be changed after creation.
    These are the ones that can be created through the API; the messenger channels are bound by registering with the
    bot instead. `webPush` is created from the `pushSubscription` a browser issues rather than from an `address`.
    """

    def to_dict(self) -> dict[str, Any]:
        active_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_period, Unset):
            active_period = self.active_period.to_dict()

        address = self.address

        alert_delay = self.alert_delay

        alert_subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alert_subscriptions, Unset):
            alert_subscriptions = []
            for alert_subscriptions_item_data in self.alert_subscriptions:
                alert_subscriptions_item = alert_subscriptions_item_data.to_dict()
                alert_subscriptions.append(alert_subscriptions_item)

        billing_notifications = self.billing_notifications

        default_subscriptions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_subscriptions, Unset):
            default_subscriptions = self.default_subscriptions.to_dict()

        gateway = self.gateway

        grouped_alerts = self.grouped_alerts

        http_headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.http_headers, Unset):
            http_headers = []
            for http_headers_item_data in self.http_headers:
                http_headers_item = http_headers_item_data.to_dict()
                http_headers.append(http_headers_item)

        language = self.language

        mime_type = self.mime_type

        name = self.name

        push_subscription: dict[str, Any] | Unset = UNSET
        if not isinstance(self.push_subscription, Unset):
            push_subscription = self.push_subscription.to_dict()

        report_subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.report_subscriptions, Unset):
            report_subscriptions = []
            for report_subscriptions_item_data in self.report_subscriptions:
                report_subscriptions_item = report_subscriptions_item_data.to_dict()
                report_subscriptions.append(report_subscriptions_item)

        send_news = self.send_news

        templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active_period is not UNSET:
            field_dict["activePeriod"] = active_period
        if address is not UNSET:
            field_dict["address"] = address
        if alert_delay is not UNSET:
            field_dict["alertDelay"] = alert_delay
        if alert_subscriptions is not UNSET:
            field_dict["alertSubscriptions"] = alert_subscriptions
        if billing_notifications is not UNSET:
            field_dict["billingNotifications"] = billing_notifications
        if default_subscriptions is not UNSET:
            field_dict["defaultSubscriptions"] = default_subscriptions
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if grouped_alerts is not UNSET:
            field_dict["groupedAlerts"] = grouped_alerts
        if http_headers is not UNSET:
            field_dict["httpHeaders"] = http_headers
        if language is not UNSET:
            field_dict["language"] = language
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if push_subscription is not UNSET:
            field_dict["pushSubscription"] = push_subscription
        if report_subscriptions is not UNSET:
            field_dict["reportSubscriptions"] = report_subscriptions
        if send_news is not UNSET:
            field_dict["sendNews"] = send_news
        if templates is not UNSET:
            field_dict["templates"] = templates
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_active_period import ContactActivePeriod
        from ..models.contact_alert_subscription import ContactAlertSubscription
        from ..models.contact_default_subscriptions import ContactDefaultSubscriptions
        from ..models.contact_http_header import ContactHttpHeader
        from ..models.contact_push_subscription import ContactPushSubscription
        from ..models.contact_report_subscription import ContactReportSubscription
        from ..models.contact_template import ContactTemplate

        d = dict(src_dict)
        _active_period = d.pop("activePeriod", UNSET)
        active_period: ContactActivePeriod | Unset
        if isinstance(_active_period, Unset):
            active_period = UNSET
        else:
            active_period = ContactActivePeriod.from_dict(_active_period)

        address = d.pop("address", UNSET)

        alert_delay = d.pop("alertDelay", UNSET)

        _alert_subscriptions = d.pop("alertSubscriptions", UNSET)
        alert_subscriptions: list[ContactAlertSubscription] | Unset = UNSET
        if _alert_subscriptions is not UNSET:
            alert_subscriptions = []
            for alert_subscriptions_item_data in _alert_subscriptions:
                alert_subscriptions_item = ContactAlertSubscription.from_dict(alert_subscriptions_item_data)

                alert_subscriptions.append(alert_subscriptions_item)

        billing_notifications = d.pop("billingNotifications", UNSET)

        _default_subscriptions = d.pop("defaultSubscriptions", UNSET)
        default_subscriptions: ContactDefaultSubscriptions | Unset
        if isinstance(_default_subscriptions, Unset):
            default_subscriptions = UNSET
        else:
            default_subscriptions = ContactDefaultSubscriptions.from_dict(_default_subscriptions)

        gateway = d.pop("gateway", UNSET)

        grouped_alerts = d.pop("groupedAlerts", UNSET)

        _http_headers = d.pop("httpHeaders", UNSET)
        http_headers: list[ContactHttpHeader] | Unset = UNSET
        if _http_headers is not UNSET:
            http_headers = []
            for http_headers_item_data in _http_headers:
                http_headers_item = ContactHttpHeader.from_dict(http_headers_item_data)

                http_headers.append(http_headers_item)

        language = d.pop("language", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        name = d.pop("name", UNSET)

        _push_subscription = d.pop("pushSubscription", UNSET)
        push_subscription: ContactPushSubscription | Unset
        if isinstance(_push_subscription, Unset):
            push_subscription = UNSET
        else:
            push_subscription = ContactPushSubscription.from_dict(_push_subscription)

        _report_subscriptions = d.pop("reportSubscriptions", UNSET)
        report_subscriptions: list[ContactReportSubscription] | Unset = UNSET
        if _report_subscriptions is not UNSET:
            report_subscriptions = []
            for report_subscriptions_item_data in _report_subscriptions:
                report_subscriptions_item = ContactReportSubscription.from_dict(report_subscriptions_item_data)

                report_subscriptions.append(report_subscriptions_item)

        send_news = d.pop("sendNews", UNSET)

        _templates = d.pop("templates", UNSET)
        templates: list[ContactTemplate] | Unset = UNSET
        if _templates is not UNSET:
            templates = []
            for templates_item_data in _templates:
                templates_item = ContactTemplate.from_dict(templates_item_data)

                templates.append(templates_item)

        _type_ = d.pop("type", UNSET)
        type_: ContactPatchRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_contact_patch_request_type(_type_)

        contact_patch_request = cls(
            active_period=active_period,
            address=address,
            alert_delay=alert_delay,
            alert_subscriptions=alert_subscriptions,
            billing_notifications=billing_notifications,
            default_subscriptions=default_subscriptions,
            gateway=gateway,
            grouped_alerts=grouped_alerts,
            http_headers=http_headers,
            language=language,
            mime_type=mime_type,
            name=name,
            push_subscription=push_subscription,
            report_subscriptions=report_subscriptions,
            send_news=send_news,
            templates=templates,
            type_=type_,
        )

        return contact_patch_request
