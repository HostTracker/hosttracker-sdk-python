from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebRiskSettings")


@_attrs_define
class WebRiskSettings:
    """Checks urls against Google's Web Risk lists of phishing, deceptive and malware-hosting resources. It always runs
    from a fixed internal check network rather than the public agent fleet, so there is no location to choose -
    `locations.pools` is refused if sent; omit `locations` entirely when creating this type.

    """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        web_risk_settings = cls()

        return web_risk_settings
