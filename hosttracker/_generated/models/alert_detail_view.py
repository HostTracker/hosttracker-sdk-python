from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_detail_view_kind import AlertDetailViewKind, check_alert_detail_view_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_attempt_view import AlertAttemptView
    from ..models.contacts_contact_ref_view import ContactsContactRefView
    from ..models.results_monitor_ref_view import ResultsMonitorRefView


T = TypeVar("T", bound="AlertDetailView")


@_attrs_define
class AlertDetailView:
    sent_at: int
    """ Unix seconds. """
    id: str | Unset = UNSET
    kind: AlertDetailViewKind | Unset = UNSET
    channel: str | Unset = UNSET
    gateway: None | str | Unset = UNSET
    contact: ContactsContactRefView | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    monitor: None | ResultsMonitorRefView | Unset = UNSET
    check_number: int | None | Unset = UNSET
    subject: None | str | Unset = UNSET
    preview: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    attempts: list[AlertAttemptView] | Unset = UNSET
    """ Every log row recorded at this instant for this contact - the per-attempt detail. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        sent_at = self.sent_at

        id = self.id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        channel = self.channel

        gateway: None | str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        monitor: dict[str, Any] | None | Unset
        if isinstance(self.monitor, Unset):
            monitor = UNSET
        elif isinstance(self.monitor, ResultsMonitorRefView):
            monitor = self.monitor.to_dict()
        else:
            monitor = self.monitor

        check_number: int | None | Unset
        if isinstance(self.check_number, Unset):
            check_number = UNSET
        else:
            check_number = self.check_number

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        preview: None | str | Unset
        if isinstance(self.preview, Unset):
            preview = UNSET
        else:
            preview = self.preview

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        attempts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attempts, Unset):
            attempts = []
            for attempts_item_data in self.attempts:
                attempts_item = attempts_item_data.to_dict()
                attempts.append(attempts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sentAt": sent_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if channel is not UNSET:
            field_dict["channel"] = channel
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if contact is not UNSET:
            field_dict["contact"] = contact
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if check_number is not UNSET:
            field_dict["checkNumber"] = check_number
        if subject is not UNSET:
            field_dict["subject"] = subject
        if preview is not UNSET:
            field_dict["preview"] = preview
        if body is not UNSET:
            field_dict["body"] = body
        if attempts is not UNSET:
            field_dict["attempts"] = attempts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_attempt_view import AlertAttemptView
        from ..models.contacts_contact_ref_view import ContactsContactRefView
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        d = dict(src_dict)
        sent_at = d.pop("sentAt")

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: AlertDetailViewKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_alert_detail_view_kind(_kind)

        channel = d.pop("channel", UNSET)

        def _parse_gateway(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        _contact = d.pop("contact", UNSET)
        contact: ContactsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactsContactRefView.from_dict(_contact)

        def _parse_monitor(data: object) -> None | ResultsMonitorRefView | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                monitor_type_0 = ResultsMonitorRefView.from_dict(data)

                return monitor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultsMonitorRefView | Unset, data)

        monitor = _parse_monitor(d.pop("monitor", UNSET))

        def _parse_check_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        check_number = _parse_check_number(d.pop("checkNumber", UNSET))

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview = _parse_preview(d.pop("preview", UNSET))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        _attempts = d.pop("attempts", UNSET)
        attempts: list[AlertAttemptView] | Unset = UNSET
        if _attempts is not UNSET:
            attempts = []
            for attempts_item_data in _attempts:
                attempts_item = AlertAttemptView.from_dict(attempts_item_data)

                attempts.append(attempts_item)

        alert_detail_view = cls(
            sent_at=sent_at,
            id=id,
            kind=kind,
            channel=channel,
            gateway=gateway,
            contact=contact,
            monitor=monitor,
            check_number=check_number,
            subject=subject,
            preview=preview,
            body=body,
            attempts=attempts,
        )

        alert_detail_view.additional_properties = d
        return alert_detail_view

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
