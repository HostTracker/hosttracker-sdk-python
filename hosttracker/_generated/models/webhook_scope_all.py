from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookScopeAll")


@_attrs_define
class WebhookScopeAll:
    """Every monitor on the account, including ones created later."""

    all_: bool
    """ Must be `true`. Send `monitorIds` or `tags` to narrow instead. """

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "all": all_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_ = d.pop("all")

        webhook_scope_all = cls(
            all_=all_,
        )

        return webhook_scope_all
