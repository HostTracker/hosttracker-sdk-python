from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_type_template_parameter import ContactTypeTemplateParameter


T = TypeVar("T", bound="ContactTypeRow")


@_attrs_define
class ContactTypeRow:
    """One contact type in the catalogue."""

    type_: str | Unset = UNSET
    """ The type token, as a contact's type member spells it. """
    label: str | Unset = UNSET
    """ The display name for this type. """
    creatable: bool | Unset = UNSET
    """ Whether a contact of this type may be created through the API. """
    requires_registration: bool | Unset = UNSET
    """ Whether the recipient must register with a messenger before delivery works. """
    gateways: list[str] | Unset = UNSET
    """ The gateways available for this type. """
    supports_reports: bool | Unset = UNSET
    """ Whether scheduled reports can be delivered to this type. """
    confirmable: bool | Unset = UNSET
    """ Whether a contact of this type must confirm a code before it receives anything. """
    alert_delays: list[int] | Unset = UNSET
    """ The alert delays this type accepts. """
    web_push_key: str | Unset = UNSET
    """ The application server (VAPID) PUBLIC key a browser passes to
    `pushManager.subscribe({applicationServerKey})` to mint the subscription a webPush contact is created from.
    Present on the `webPush` row only, and absent when this installation has no key configured - which is the answer
    to whether a browser can be registered at all. """
    template_parameters: list[ContactTypeTemplateParameter] | Unset = UNSET
    """ The `[[token]]` vocabulary a custom message template may use. Present on the `http` row only - it is the
    vocabulary of a contact's `templates[].content`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        label = self.label

        creatable = self.creatable

        requires_registration = self.requires_registration

        gateways: list[str] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = self.gateways

        supports_reports = self.supports_reports

        confirmable = self.confirmable

        alert_delays: list[int] | Unset = UNSET
        if not isinstance(self.alert_delays, Unset):
            alert_delays = self.alert_delays

        web_push_key = self.web_push_key

        template_parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.template_parameters, Unset):
            template_parameters = []
            for template_parameters_item_data in self.template_parameters:
                template_parameters_item = template_parameters_item_data.to_dict()
                template_parameters.append(template_parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if creatable is not UNSET:
            field_dict["creatable"] = creatable
        if requires_registration is not UNSET:
            field_dict["requiresRegistration"] = requires_registration
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if supports_reports is not UNSET:
            field_dict["supportsReports"] = supports_reports
        if confirmable is not UNSET:
            field_dict["confirmable"] = confirmable
        if alert_delays is not UNSET:
            field_dict["alertDelays"] = alert_delays
        if web_push_key is not UNSET:
            field_dict["webPushKey"] = web_push_key
        if template_parameters is not UNSET:
            field_dict["templateParameters"] = template_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_type_template_parameter import ContactTypeTemplateParameter

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        label = d.pop("label", UNSET)

        creatable = d.pop("creatable", UNSET)

        requires_registration = d.pop("requiresRegistration", UNSET)

        gateways = cast(list[str], d.pop("gateways", UNSET))

        supports_reports = d.pop("supportsReports", UNSET)

        confirmable = d.pop("confirmable", UNSET)

        alert_delays = cast(list[int], d.pop("alertDelays", UNSET))

        web_push_key = d.pop("webPushKey", UNSET)

        _template_parameters = d.pop("templateParameters", UNSET)
        template_parameters: list[ContactTypeTemplateParameter] | Unset = UNSET
        if _template_parameters is not UNSET:
            template_parameters = []
            for template_parameters_item_data in _template_parameters:
                template_parameters_item = ContactTypeTemplateParameter.from_dict(template_parameters_item_data)

                template_parameters.append(template_parameters_item)

        contact_type_row = cls(
            type_=type_,
            label=label,
            creatable=creatable,
            requires_registration=requires_registration,
            gateways=gateways,
            supports_reports=supports_reports,
            confirmable=confirmable,
            alert_delays=alert_delays,
            web_push_key=web_push_key,
            template_parameters=template_parameters,
        )

        contact_type_row.additional_properties = d
        return contact_type_row

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
