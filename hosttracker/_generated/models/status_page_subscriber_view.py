from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_subscriber_view_kind import (
    StatusPageSubscriberViewKind,
    check_status_page_subscriber_view_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageSubscriberView")


@_attrs_define
class StatusPageSubscriberView:
    """One subscriber, owner view."""

    id: UUID
    created: int
    """ Unix seconds. """
    kind: StatusPageSubscriberViewKind | Unset = UNSET
    email: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    component_id: None | Unset | UUID = UNSET
    confirmed_at: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created = self.created

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        component_id: None | str | Unset
        if isinstance(self.component_id, Unset):
            component_id = UNSET
        elif isinstance(self.component_id, UUID):
            component_id = str(self.component_id)
        else:
            component_id = self.component_id

        confirmed_at: int | None | Unset
        if isinstance(self.confirmed_at, Unset):
            confirmed_at = UNSET
        else:
            confirmed_at = self.confirmed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if email is not UNSET:
            field_dict["email"] = email
        if url is not UNSET:
            field_dict["url"] = url
        if component_id is not UNSET:
            field_dict["componentId"] = component_id
        if confirmed_at is not UNSET:
            field_dict["confirmedAt"] = confirmed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = d.pop("created")

        _kind = d.pop("kind", UNSET)
        kind: StatusPageSubscriberViewKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_status_page_subscriber_view_kind(_kind)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_component_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                component_id_type_0 = UUID(data)

                return component_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        component_id = _parse_component_id(d.pop("componentId", UNSET))

        def _parse_confirmed_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmedAt", UNSET))

        status_page_subscriber_view = cls(
            id=id,
            created=created,
            kind=kind,
            email=email,
            url=url,
            component_id=component_id,
            confirmed_at=confirmed_at,
        )

        status_page_subscriber_view.additional_properties = d
        return status_page_subscriber_view

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
