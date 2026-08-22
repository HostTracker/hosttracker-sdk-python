from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ic_history_view_state import IcHistoryViewState, check_ic_history_view_state
from ..types import UNSET, Unset

T = TypeVar("T", bound="IcHistoryView")


@_attrs_define
class IcHistoryView:
    id: UUID
    db_id: int
    up: bool
    """ The overall verdict recorded for the check: true = up. """
    created: int
    """ Unix seconds. """
    type_: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    state: IcHistoryViewState | Unset = UNSET
    done_at: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        db_id = self.db_id

        up = self.up

        created = self.created

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        done_at: int | None | Unset
        if isinstance(self.done_at, Unset):
            done_at = UNSET
        else:
            done_at = self.done_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dbId": db_id,
                "up": up,
                "created": created,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if state is not UNSET:
            field_dict["state"] = state
        if done_at is not UNSET:
            field_dict["doneAt"] = done_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        db_id = d.pop("dbId")

        up = d.pop("up")

        created = d.pop("created")

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        _state = d.pop("state", UNSET)
        state: IcHistoryViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_ic_history_view_state(_state)

        def _parse_done_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        done_at = _parse_done_at(d.pop("doneAt", UNSET))

        ic_history_view = cls(
            id=id,
            db_id=db_id,
            up=up,
            created=created,
            type_=type_,
            url=url,
            state=state,
            done_at=done_at,
        )

        ic_history_view.additional_properties = d
        return ic_history_view

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
