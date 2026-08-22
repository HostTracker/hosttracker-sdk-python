from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactTestRequest")


@_attrs_define
class ContactTestRequest:
    """Which alert type the test delivery should render."""

    alert_type: str | Unset = UNSET
    """ The alert type to render. Defaults to an up notification. """

    def to_dict(self) -> dict[str, Any]:
        alert_type = self.alert_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if alert_type is not UNSET:
            field_dict["alertType"] = alert_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_type = d.pop("alertType", UNSET)

        contact_test_request = cls(
            alert_type=alert_type,
        )

        return contact_test_request
