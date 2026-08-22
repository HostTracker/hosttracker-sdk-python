from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricPointView")


@_attrs_define
class MetricPointView:
    """One aggregated metric over a bucket - `{t, value, p95, samples}`."""

    t: int
    """ The bucket's midpoint, Unix seconds. Unix seconds. """
    samples: int
    """ How many checks contributed - what tells a thin bucket from a flat one. """
    value: float | None | Unset = UNSET
    """ The mean over the bucket, or null when nothing was sampled. """
    p95: float | None | Unset = UNSET
    """ The 95th percentile over the same samples the mean is computed from, or null when nothing was sampled. It is
    the figure a latency chart needs beside the average: a mean hides the slow tail that users actually feel, and a
    single slow check moves the mean far less than it moves this. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        t = self.t

        samples = self.samples

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        p95: float | None | Unset
        if isinstance(self.p95, Unset):
            p95 = UNSET
        else:
            p95 = self.p95

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "t": t,
                "samples": samples,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if p95 is not UNSET:
            field_dict["p95"] = p95

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        t = d.pop("t")

        samples = d.pop("samples")

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_p95(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        p95 = _parse_p95(d.pop("p95", UNSET))

        metric_point_view = cls(
            t=t,
            samples=samples,
            value=value,
            p95=p95,
        )

        metric_point_view.additional_properties = d
        return metric_point_view

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
