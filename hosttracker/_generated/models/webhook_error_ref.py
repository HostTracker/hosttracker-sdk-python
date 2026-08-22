from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookErrorRef")


@_attrs_define
class WebhookErrorRef:
    """A failed check's error, typed the same way the results feed types it."""

    code: int | Unset = UNSET
    """ The protocol or status code behind the failure, when it has one (an HTTP status, for example). """
    message: str | Unset = UNSET
    """ The technical message the checking agent reported. """
    codename: str | Unset = UNSET
    """ A short, stable, English-only name for the failure (ConnectTimeout, HttpError) - the value to switch on. """

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        codename = self.codename

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if codename is not UNSET:
            field_dict["codename"] = codename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        codename = d.pop("codename", UNSET)

        webhook_error_ref = cls(
            code=code,
            message=message,
            codename=codename,
        )

        return webhook_error_ref
