from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookSecretRotate")


@_attrs_define
class WebhookSecretRotate:
    """Ask the server to mint a new one. Update only - on a create there is nothing to rotate."""

    rotate: bool
    """ Must be `true`. """

    def to_dict(self) -> dict[str, Any]:
        rotate = self.rotate

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rotate": rotate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rotate = d.pop("rotate")

        webhook_secret_rotate = cls(
            rotate=rotate,
        )

        return webhook_secret_rotate
