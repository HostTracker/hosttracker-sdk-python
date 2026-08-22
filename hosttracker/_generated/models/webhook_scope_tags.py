from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookScopeTags")


@_attrs_define
class WebhookScopeTags:
    """Every monitor carrying any of these tags, evaluated per delivery."""

    tags: list[str]
    """ A tag to match. """

    def to_dict(self) -> dict[str, Any]:
        tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags"))

        webhook_scope_tags = cls(
            tags=tags,
        )

        return webhook_scope_tags
