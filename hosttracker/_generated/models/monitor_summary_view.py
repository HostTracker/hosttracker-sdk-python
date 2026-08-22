from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_group_count import MonitorGroupCount
    from ..models.monitor_state_counts import MonitorStateCounts


T = TypeVar("T", bound="MonitorSummaryView")


@_attrs_define
class MonitorSummaryView:
    """`expand=summary` - the account-wide dashboard block."""

    downtime_sec: int
    """ Total DOWN seconds across the account, clipped to the request's `from`/`to` - the one interval-scoped member
    of an otherwise instantaneous block. """
    counts: MonitorStateCounts | Unset = UNSET
    """ The four states, always all four present - a zero is information, an absent key is a question. """
    by_type: list[MonitorGroupCount] | Unset = UNSET
    by_tag: list[MonitorGroupCount] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    top_domains: list[MonitorGroupCount] | Unset = UNSET
    """ The account's ten largest domains by monitor count, most monitors first. The count is fixed at ten and is
    not a parameter - the block is a dashboard header, not a query surface. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        downtime_sec = self.downtime_sec

        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        by_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = []
            for by_type_item_data in self.by_type:
                by_type_item = by_type_item_data.to_dict()
                by_type.append(by_type_item)

        by_tag: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_tag, Unset):
            by_tag = []
            for by_tag_item_data in self.by_tag:
                by_tag_item = by_tag_item_data.to_dict()
                by_tag.append(by_tag_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        top_domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_domains, Unset):
            top_domains = []
            for top_domains_item_data in self.top_domains:
                top_domains_item = top_domains_item_data.to_dict()
                top_domains.append(top_domains_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "downtimeSec": downtime_sec,
            }
        )
        if counts is not UNSET:
            field_dict["counts"] = counts
        if by_type is not UNSET:
            field_dict["byType"] = by_type
        if by_tag is not UNSET:
            field_dict["byTag"] = by_tag
        if tags is not UNSET:
            field_dict["tags"] = tags
        if top_domains is not UNSET:
            field_dict["topDomains"] = top_domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_group_count import MonitorGroupCount
        from ..models.monitor_state_counts import MonitorStateCounts

        d = dict(src_dict)
        downtime_sec = d.pop("downtimeSec")

        _counts = d.pop("counts", UNSET)
        counts: MonitorStateCounts | Unset
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = MonitorStateCounts.from_dict(_counts)

        _by_type = d.pop("byType", UNSET)
        by_type: list[MonitorGroupCount] | Unset = UNSET
        if _by_type is not UNSET:
            by_type = []
            for by_type_item_data in _by_type:
                by_type_item = MonitorGroupCount.from_dict(by_type_item_data)

                by_type.append(by_type_item)

        _by_tag = d.pop("byTag", UNSET)
        by_tag: list[MonitorGroupCount] | Unset = UNSET
        if _by_tag is not UNSET:
            by_tag = []
            for by_tag_item_data in _by_tag:
                by_tag_item = MonitorGroupCount.from_dict(by_tag_item_data)

                by_tag.append(by_tag_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        _top_domains = d.pop("topDomains", UNSET)
        top_domains: list[MonitorGroupCount] | Unset = UNSET
        if _top_domains is not UNSET:
            top_domains = []
            for top_domains_item_data in _top_domains:
                top_domains_item = MonitorGroupCount.from_dict(top_domains_item_data)

                top_domains.append(top_domains_item)

        monitor_summary_view = cls(
            downtime_sec=downtime_sec,
            counts=counts,
            by_type=by_type,
            by_tag=by_tag,
            tags=tags,
            top_domains=top_domains,
        )

        monitor_summary_view.additional_properties = d
        return monitor_summary_view

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
