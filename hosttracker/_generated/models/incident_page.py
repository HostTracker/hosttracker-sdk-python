from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_view import IncidentView
    from ..models.page_count import PageCount


T = TypeVar("T", bound="IncidentPage")


@_attrs_define
class IncidentPage:
    """THE collection envelope of the v2 surface - `{ data, nextCursor, hasMore }`. Every collection response uses it,
    including the small closed vocabularies that never page, where it is used for uniformity rather than because paging
    is expected. **Uniformity is the feature**: one envelope means one client parser.

    """

    data: list[IncidentView]
    """ The page's rows. Never null - an empty page is `[]`. """
    next_cursor: None | str
    """ Opaque cursor for the NEXT page, or null when there is none. """
    has_more: bool
    """ True when another page exists. Always equals `NextCursor is not null`. """
    sync_cursor: None | str | Unset = UNSET
    """ Delta cursor for the next SYNC cycle. Omitted where a domain does not support delta reads. """
    count: None | PageCount | Unset = UNSET
    """ Envelope-scoped `expand=count` - `{ total, matched }`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.page_count import PageCount

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        sync_cursor: None | str | Unset
        if isinstance(self.sync_cursor, Unset):
            sync_cursor = UNSET
        else:
            sync_cursor = self.sync_cursor

        count: dict[str, Any] | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        elif isinstance(self.count, PageCount):
            count = self.count.to_dict()
        else:
            count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "nextCursor": next_cursor,
                "hasMore": has_more,
            }
        )
        if sync_cursor is not UNSET:
            field_dict["syncCursor"] = sync_cursor
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_view import IncidentView
        from ..models.page_count import PageCount

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = IncidentView.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        has_more = d.pop("hasMore")

        def _parse_sync_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_cursor = _parse_sync_cursor(d.pop("syncCursor", UNSET))

        def _parse_count(data: object) -> None | PageCount | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                count_type_0 = PageCount.from_dict(data)

                return count_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PageCount | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        incident_page = cls(
            data=data,
            next_cursor=next_cursor,
            has_more=has_more,
            sync_cursor=sync_cursor,
            count=count,
        )

        incident_page.additional_properties = d
        return incident_page

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
