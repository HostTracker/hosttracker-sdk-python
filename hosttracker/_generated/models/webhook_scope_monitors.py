from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookScopeMonitors")


@_attrs_define
class WebhookScopeMonitors:
    """An explicit list of monitors."""

    monitor_ids: list[UUID]
    """ A monitor to receive events for. """

    def to_dict(self) -> dict[str, Any]:
        monitor_ids = []
        for monitor_ids_item_data in self.monitor_ids:
            monitor_ids_item = str(monitor_ids_item_data)
            monitor_ids.append(monitor_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitorIds": monitor_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor_ids = []
        _monitor_ids = d.pop("monitorIds")
        for monitor_ids_item_data in _monitor_ids:
            monitor_ids_item = UUID(monitor_ids_item_data)

            monitor_ids.append(monitor_ids_item)

        webhook_scope_monitors = cls(
            monitor_ids=monitor_ids,
        )

        return webhook_scope_monitors
