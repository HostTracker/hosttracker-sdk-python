from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_range_view import ReportRangeView


T = TypeVar("T", bound="GeneratedReportView")


@_attrs_define
class GeneratedReportView:
    expires_at: int
    """ Unix seconds. """
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    format_: str | Unset = UNSET
    range_: ReportRangeView | Unset = UNSET
    """ A report's window, Unix seconds on the wire. """
    monitor_ids: list[UUID] | Unset = UNSET
    sections: list[str] | Unset = UNSET
    size_bytes: int | None | Unset = UNSET
    """ Present only while the rendered document is still held. """
    state: str | Unset = UNSET
    """ `ready` - the content endpoint will serve it (from cache, or by re-rendering). There is no `expired` value:
    an expired id is a **404**, because a resource that cannot be fetched is not a resource whose state you read.
    """
    content_url: str | Unset = UNSET
    """ The download url - same base URL, same auth. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        id = self.id

        type_ = self.type_

        format_ = self.format_

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        monitor_ids: list[str] | Unset = UNSET
        if not isinstance(self.monitor_ids, Unset):
            monitor_ids = []
            for monitor_ids_item_data in self.monitor_ids:
                monitor_ids_item = str(monitor_ids_item_data)
                monitor_ids.append(monitor_ids_item)

        sections: list[str] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections

        size_bytes: int | None | Unset
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        state = self.state

        content_url = self.content_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiresAt": expires_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if format_ is not UNSET:
            field_dict["format"] = format_
        if range_ is not UNSET:
            field_dict["range"] = range_
        if monitor_ids is not UNSET:
            field_dict["monitorIds"] = monitor_ids
        if sections is not UNSET:
            field_dict["sections"] = sections
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if state is not UNSET:
            field_dict["state"] = state
        if content_url is not UNSET:
            field_dict["contentUrl"] = content_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_range_view import ReportRangeView

        d = dict(src_dict)
        expires_at = d.pop("expiresAt")

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        format_ = d.pop("format", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: ReportRangeView | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = ReportRangeView.from_dict(_range_)

        _monitor_ids = d.pop("monitorIds", UNSET)
        monitor_ids: list[UUID] | Unset = UNSET
        if _monitor_ids is not UNSET:
            monitor_ids = []
            for monitor_ids_item_data in _monitor_ids:
                monitor_ids_item = UUID(monitor_ids_item_data)

                monitor_ids.append(monitor_ids_item)

        sections = cast(list[str], d.pop("sections", UNSET))

        def _parse_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes", UNSET))

        state = d.pop("state", UNSET)

        content_url = d.pop("contentUrl", UNSET)

        generated_report_view = cls(
            expires_at=expires_at,
            id=id,
            type_=type_,
            format_=format_,
            range_=range_,
            monitor_ids=monitor_ids,
            sections=sections,
            size_bytes=size_bytes,
            state=state,
            content_url=content_url,
        )

        generated_report_view.additional_properties = d
        return generated_report_view

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
