from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ic_result_view_state import IcResultViewState, check_ic_result_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ic_event_view import IcEventView


T = TypeVar("T", bound="IcResultView")


@_attrs_define
class IcResultView:
    id: UUID
    db_id: int
    created: int
    """ Unix seconds. """
    state: IcResultViewState | Unset = UNSET
    """ `running` | `done`. """
    url: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    done_at: int | None | Unset = UNSET
    """ When the LAST location reported. """
    retry_after: int | None | Unset = UNSET
    """ Seconds to wait before polling again. Absent once the check is terminal. """
    events: list[IcEventView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        db_id = self.db_id

        created = self.created

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        done_at: int | None | Unset
        if isinstance(self.done_at, Unset):
            done_at = UNSET
        else:
            done_at = self.done_at

        retry_after: int | None | Unset
        if isinstance(self.retry_after, Unset):
            retry_after = UNSET
        else:
            retry_after = self.retry_after

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dbId": db_id,
                "created": created,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if url is not UNSET:
            field_dict["url"] = url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if done_at is not UNSET:
            field_dict["doneAt"] = done_at
        if retry_after is not UNSET:
            field_dict["retryAfter"] = retry_after
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ic_event_view import IcEventView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        db_id = d.pop("dbId")

        created = d.pop("created")

        _state = d.pop("state", UNSET)
        state: IcResultViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_ic_result_view_state(_state)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_done_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        done_at = _parse_done_at(d.pop("doneAt", UNSET))

        def _parse_retry_after(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_after = _parse_retry_after(d.pop("retryAfter", UNSET))

        _events = d.pop("events", UNSET)
        events: list[IcEventView] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = IcEventView.from_dict(events_item_data)

                events.append(events_item)

        ic_result_view = cls(
            id=id,
            db_id=db_id,
            created=created,
            state=state,
            url=url,
            type_=type_,
            done_at=done_at,
            retry_after=retry_after,
            events=events,
        )

        ic_result_view.additional_properties = d
        return ic_result_view

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
