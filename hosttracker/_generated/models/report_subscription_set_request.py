from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.report_subscription_set_request_frequencies_item import (
    ReportSubscriptionSetRequestFrequenciesItem,
    check_report_subscription_set_request_frequencies_item,
)

T = TypeVar("T", bound="ReportSubscriptionSetRequest")


@_attrs_define
class ReportSubscriptionSetRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    frequencies: list[ReportSubscriptionSetRequestFrequenciesItem]
    """ The EXACT set of report frequencies for this pair. At least one; use DELETE to remove. """

    def to_dict(self) -> dict[str, Any]:
        frequencies = []
        for frequencies_item_data in self.frequencies:
            frequencies_item: str = frequencies_item_data
            frequencies.append(frequencies_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "frequencies": frequencies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequencies = []
        _frequencies = d.pop("frequencies")
        for frequencies_item_data in _frequencies:
            frequencies_item = check_report_subscription_set_request_frequencies_item(frequencies_item_data)

            frequencies.append(frequencies_item)

        report_subscription_set_request = cls(
            frequencies=frequencies,
        )

        return report_subscription_set_request
