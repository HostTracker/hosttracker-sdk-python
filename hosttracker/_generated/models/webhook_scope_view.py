from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookScopeView")


@_attrs_define
class WebhookScopeView:
    """The webhook's `scope` - exactly ONE of `{all:true}` / `{monitorIds:[…]}` / `{tags:[…]}`. An omitted monitor list
    cannot be allowed to mean "none" (an account-wide webhook would be unexpressible) OR "all", so the third state is
    spelled out.

    """

    monitor_count: int
    """ How many monitors the scope resolved to - always present, including 0. """
    all_: bool | None | Unset = UNSET
    monitor_ids: list[UUID] | None | Unset = UNSET
    """ The monitors this webhook is addressed to - the `api.WebhookMonitor` rows the last write resolved. """
    tags: list[str] | None | Unset = UNSET
    resolved_monitor_ids: list[UUID] | None | Unset = UNSET
    """ What a `tags` scope resolved TO - published rather than hidden, because the fidelity loss is only honest if
    the caller can see the set it actually got. (An `all` scope publishes `all:true` + a count instead - it is a
    form, not an id set, and nothing can widen it.) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_count = self.monitor_count

        all_: bool | None | Unset
        if isinstance(self.all_, Unset):
            all_ = UNSET
        else:
            all_ = self.all_

        monitor_ids: list[str] | None | Unset
        if isinstance(self.monitor_ids, Unset):
            monitor_ids = UNSET
        elif isinstance(self.monitor_ids, list):
            monitor_ids = []
            for monitor_ids_type_0_item_data in self.monitor_ids:
                monitor_ids_type_0_item = str(monitor_ids_type_0_item_data)
                monitor_ids.append(monitor_ids_type_0_item)

        else:
            monitor_ids = self.monitor_ids

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        resolved_monitor_ids: list[str] | None | Unset
        if isinstance(self.resolved_monitor_ids, Unset):
            resolved_monitor_ids = UNSET
        elif isinstance(self.resolved_monitor_ids, list):
            resolved_monitor_ids = []
            for resolved_monitor_ids_type_0_item_data in self.resolved_monitor_ids:
                resolved_monitor_ids_type_0_item = str(resolved_monitor_ids_type_0_item_data)
                resolved_monitor_ids.append(resolved_monitor_ids_type_0_item)

        else:
            resolved_monitor_ids = self.resolved_monitor_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitorCount": monitor_count,
            }
        )
        if all_ is not UNSET:
            field_dict["all"] = all_
        if monitor_ids is not UNSET:
            field_dict["monitorIds"] = monitor_ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if resolved_monitor_ids is not UNSET:
            field_dict["resolvedMonitorIds"] = resolved_monitor_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor_count = d.pop("monitorCount")

        def _parse_all_(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_ = _parse_all_(d.pop("all", UNSET))

        def _parse_monitor_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                monitor_ids_type_0 = []
                _monitor_ids_type_0 = data
                for monitor_ids_type_0_item_data in _monitor_ids_type_0:
                    monitor_ids_type_0_item = UUID(monitor_ids_type_0_item_data)

                    monitor_ids_type_0.append(monitor_ids_type_0_item)

                return monitor_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        monitor_ids = _parse_monitor_ids(d.pop("monitorIds", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_resolved_monitor_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resolved_monitor_ids_type_0 = []
                _resolved_monitor_ids_type_0 = data
                for resolved_monitor_ids_type_0_item_data in _resolved_monitor_ids_type_0:
                    resolved_monitor_ids_type_0_item = UUID(resolved_monitor_ids_type_0_item_data)

                    resolved_monitor_ids_type_0.append(resolved_monitor_ids_type_0_item)

                return resolved_monitor_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        resolved_monitor_ids = _parse_resolved_monitor_ids(d.pop("resolvedMonitorIds", UNSET))

        webhook_scope_view = cls(
            monitor_count=monitor_count,
            all_=all_,
            monitor_ids=monitor_ids,
            tags=tags,
            resolved_monitor_ids=resolved_monitor_ids,
        )

        webhook_scope_view.additional_properties = d
        return webhook_scope_view

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
