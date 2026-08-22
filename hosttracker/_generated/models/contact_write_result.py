from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_view_type import ContactViewType, check_contact_view_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confirmation_view import ConfirmationView
    from ..models.contact_active_period_view import ContactActivePeriodView
    from ..models.contact_group_membership_view import ContactGroupMembershipView
    from ..models.contact_header_view import ContactHeaderView
    from ..models.contact_subscription_summary_view import ContactSubscriptionSummaryView
    from ..models.contact_template_view import ContactTemplateView


T = TypeVar("T", bound="ContactWriteResult")


@_attrs_define
class ContactWriteResult:
    """The contact, in exactly the shape `GET /contact/{id}` renders it, plus what the write itself did - the confirmation
    attempt, and the subscriptions it wired.

    """

    id: UUID
    confirmed: bool
    overlimited: bool
    grouped_alerts: bool
    created: int
    """ Creation instant, Unix seconds. Unix seconds. """
    updated: int
    """ Creation-faithful, not edit-faithful: this is the contact's creation instant, and nothing else moves it. **⚠
    A configuration edit does NOT move it, and this field cannot be used to detect one.**`UserContact` carries no
    modification timestamp, so a rename, a re-delay, a re-language, or `confirmed` flipping true leaves this value
    untouched - a poll loop built on it, or on the `updatedSince` parameter, will silently never observe that edit.
    Subscribe to the `contact.updated` webhook (and `contact.confirmed` for the confirmation transition) to hear
    about a change this field and this poll cannot see. """
    confirmation: ConfirmationView | None
    """ The confirmation attempt this write made, or null when it issued no code. Always present: every write could
    have issued one, so the silence is spelled rather than left as an absent key. """
    type_: ContactViewType | Unset = UNSET
    name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    alert_delay: int | None | Unset = UNSET
    """ Minutes on the frozen ladder, or null for a stored index the ladder does not carry. """
    send_cost: float | None | Unset = UNSET
    """ What one notification to this contact costs the account, in the same units its message balance is kept in.
    Absent for a type that carries no per-message charge - only the paid channels (text messages and voice calls)
    have one, and their price depends on the destination, so it is a property of THIS contact rather than of its
    type. A long text message is split into several parts and each part is charged, so a single alert can cost a
    multiple of this number. """
    gateway: None | str | Unset = UNSET
    """ The routing gateway the server assigned (SMS/VoiceCall) or the caller pinned. """
    language: None | str | Unset = UNSET
    billing_notifications: bool | None | Unset = UNSET
    """ Email only - billing messages go to this address. """
    send_news: bool | None | Unset = UNSET
    """ Email only - product news and press releases. """
    mime_type: None | str | Unset = UNSET
    """ `http` only - the MIME type the alert body is rendered as. """
    http_headers: list[ContactHeaderView] | None | Unset = UNSET
    templates: list[ContactTemplateView] | None | Unset = UNSET
    """ `expand=template` - the custom `[[token]]` bodies an `http` contact posts. """
    active_period: ContactActivePeriodView | None | Unset = UNSET
    """ The contact's active-hours window, exactly as it is stored. """
    bot_id: None | Unset | UUID = UNSET
    """ The bot registration this contact is bound to - bot channels only. """
    subscription: ContactSubscriptionSummaryView | None | Unset = UNSET
    """ `expand=subscription` - counts plus a bounded identifying sample. """
    groups: list[ContactGroupMembershipView] | None | Unset = UNSET
    """ `expand=group` - the contact groups this contact is a member of, each with the events the group holds for
    it. An empty array means it is in none. """
    subscriptions: ContactSubscriptionSummaryView | None | Unset = UNSET
    """ The subscription state this write produced. Present only when the request named a subscription member - for
    any other write the key would be noise. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.confirmation_view import ConfirmationView
        from ..models.contact_active_period_view import ContactActivePeriodView
        from ..models.contact_subscription_summary_view import ContactSubscriptionSummaryView

        id = str(self.id)

        confirmed = self.confirmed

        overlimited = self.overlimited

        grouped_alerts = self.grouped_alerts

        created = self.created

        updated = self.updated

        confirmation: dict[str, Any] | None
        if isinstance(self.confirmation, ConfirmationView):
            confirmation = self.confirmation.to_dict()
        else:
            confirmation = self.confirmation

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        alert_delay: int | None | Unset
        if isinstance(self.alert_delay, Unset):
            alert_delay = UNSET
        else:
            alert_delay = self.alert_delay

        send_cost: float | None | Unset
        if isinstance(self.send_cost, Unset):
            send_cost = UNSET
        else:
            send_cost = self.send_cost

        gateway: None | str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        billing_notifications: bool | None | Unset
        if isinstance(self.billing_notifications, Unset):
            billing_notifications = UNSET
        else:
            billing_notifications = self.billing_notifications

        send_news: bool | None | Unset
        if isinstance(self.send_news, Unset):
            send_news = UNSET
        else:
            send_news = self.send_news

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        http_headers: list[dict[str, Any]] | None | Unset
        if isinstance(self.http_headers, Unset):
            http_headers = UNSET
        elif isinstance(self.http_headers, list):
            http_headers = []
            for http_headers_type_0_item_data in self.http_headers:
                http_headers_type_0_item = http_headers_type_0_item_data.to_dict()
                http_headers.append(http_headers_type_0_item)

        else:
            http_headers = self.http_headers

        templates: list[dict[str, Any]] | None | Unset
        if isinstance(self.templates, Unset):
            templates = UNSET
        elif isinstance(self.templates, list):
            templates = []
            for templates_type_0_item_data in self.templates:
                templates_type_0_item = templates_type_0_item_data.to_dict()
                templates.append(templates_type_0_item)

        else:
            templates = self.templates

        active_period: dict[str, Any] | None | Unset
        if isinstance(self.active_period, Unset):
            active_period = UNSET
        elif isinstance(self.active_period, ContactActivePeriodView):
            active_period = self.active_period.to_dict()
        else:
            active_period = self.active_period

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        subscription: dict[str, Any] | None | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        elif isinstance(self.subscription, ContactSubscriptionSummaryView):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription

        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        subscriptions: dict[str, Any] | None | Unset
        if isinstance(self.subscriptions, Unset):
            subscriptions = UNSET
        elif isinstance(self.subscriptions, ContactSubscriptionSummaryView):
            subscriptions = self.subscriptions.to_dict()
        else:
            subscriptions = self.subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "confirmed": confirmed,
                "overlimited": overlimited,
                "groupedAlerts": grouped_alerts,
                "created": created,
                "updated": updated,
                "confirmation": confirmation,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if alert_delay is not UNSET:
            field_dict["alertDelay"] = alert_delay
        if send_cost is not UNSET:
            field_dict["sendCost"] = send_cost
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if language is not UNSET:
            field_dict["language"] = language
        if billing_notifications is not UNSET:
            field_dict["billingNotifications"] = billing_notifications
        if send_news is not UNSET:
            field_dict["sendNews"] = send_news
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if http_headers is not UNSET:
            field_dict["httpHeaders"] = http_headers
        if templates is not UNSET:
            field_dict["templates"] = templates
        if active_period is not UNSET:
            field_dict["activePeriod"] = active_period
        if bot_id is not UNSET:
            field_dict["botId"] = bot_id
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if groups is not UNSET:
            field_dict["groups"] = groups
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirmation_view import ConfirmationView
        from ..models.contact_active_period_view import ContactActivePeriodView
        from ..models.contact_group_membership_view import ContactGroupMembershipView
        from ..models.contact_header_view import ContactHeaderView
        from ..models.contact_subscription_summary_view import ContactSubscriptionSummaryView
        from ..models.contact_template_view import ContactTemplateView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        confirmed = d.pop("confirmed")

        overlimited = d.pop("overlimited")

        grouped_alerts = d.pop("groupedAlerts")

        created = d.pop("created")

        updated = d.pop("updated")

        def _parse_confirmation(data: object) -> ConfirmationView | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                confirmation_type_0 = ConfirmationView.from_dict(data)

                return confirmation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfirmationView | None, data)

        confirmation = _parse_confirmation(d.pop("confirmation"))

        _type_ = d.pop("type", UNSET)
        type_: ContactViewType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_contact_view_type(_type_)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_alert_delay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        alert_delay = _parse_alert_delay(d.pop("alertDelay", UNSET))

        def _parse_send_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        send_cost = _parse_send_cost(d.pop("sendCost", UNSET))

        def _parse_gateway(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_billing_notifications(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        billing_notifications = _parse_billing_notifications(d.pop("billingNotifications", UNSET))

        def _parse_send_news(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_news = _parse_send_news(d.pop("sendNews", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mimeType", UNSET))

        def _parse_http_headers(data: object) -> list[ContactHeaderView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                http_headers_type_0 = []
                _http_headers_type_0 = data
                for http_headers_type_0_item_data in _http_headers_type_0:
                    http_headers_type_0_item = ContactHeaderView.from_dict(http_headers_type_0_item_data)

                    http_headers_type_0.append(http_headers_type_0_item)

                return http_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContactHeaderView] | None | Unset, data)

        http_headers = _parse_http_headers(d.pop("httpHeaders", UNSET))

        def _parse_templates(data: object) -> list[ContactTemplateView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                templates_type_0 = []
                _templates_type_0 = data
                for templates_type_0_item_data in _templates_type_0:
                    templates_type_0_item = ContactTemplateView.from_dict(templates_type_0_item_data)

                    templates_type_0.append(templates_type_0_item)

                return templates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContactTemplateView] | None | Unset, data)

        templates = _parse_templates(d.pop("templates", UNSET))

        def _parse_active_period(data: object) -> ContactActivePeriodView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                active_period_type_0 = ContactActivePeriodView.from_dict(data)

                return active_period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactActivePeriodView | None | Unset, data)

        active_period = _parse_active_period(d.pop("activePeriod", UNSET))

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("botId", UNSET))

        def _parse_subscription(data: object) -> ContactSubscriptionSummaryView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscription_type_0 = ContactSubscriptionSummaryView.from_dict(data)

                return subscription_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactSubscriptionSummaryView | None | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_groups(data: object) -> list[ContactGroupMembershipView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = ContactGroupMembershipView.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContactGroupMembershipView] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_subscriptions(data: object) -> ContactSubscriptionSummaryView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscriptions_type_0 = ContactSubscriptionSummaryView.from_dict(data)

                return subscriptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactSubscriptionSummaryView | None | Unset, data)

        subscriptions = _parse_subscriptions(d.pop("subscriptions", UNSET))

        contact_write_result = cls(
            id=id,
            confirmed=confirmed,
            overlimited=overlimited,
            grouped_alerts=grouped_alerts,
            created=created,
            updated=updated,
            confirmation=confirmation,
            type_=type_,
            name=name,
            address=address,
            alert_delay=alert_delay,
            send_cost=send_cost,
            gateway=gateway,
            language=language,
            billing_notifications=billing_notifications,
            send_news=send_news,
            mime_type=mime_type,
            http_headers=http_headers,
            templates=templates,
            active_period=active_period,
            bot_id=bot_id,
            subscription=subscription,
            groups=groups,
            subscriptions=subscriptions,
        )

        contact_write_result.additional_properties = d
        return contact_write_result

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
