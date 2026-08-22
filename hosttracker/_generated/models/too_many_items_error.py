from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TooManyItemsError")


@_attrs_define
class TooManyItemsError:
    pointer: str | Unset = UNSET
    """ Where the offending value is. """
    limit: int | Unset = UNSET
    """ The ceiling that was hit. """
    actual: bool | float | str | Unset = UNSET
    """ What it found instead. """
    parameter: str | Unset = UNSET
    """ The query parameter involved. """
    count: int | Unset = UNSET
    """ How many items the request carried. """
    max_: float | Unset = UNSET
    """ The largest accepted value. """
    max_items: int | Unset = UNSET
    """ The most items this operation accepts in one request - the same fact as `limit`, under the spelling this
    endpoint uses. """
    monitors: int | Unset = UNSET
    """ How many monitors the request named. """
    buckets: int | Unset = UNSET
    """ How many buckets the requested granularity would produce over the requested range. """
    cells: int | Unset = UNSET
    """ The monitors x buckets product a getResultSummary request would materialise - the value the `max` limit is
    measured against. """
    reason: str | Unset = UNSET
    """ A stable token naming which variety of this failure occurred. """
    detail: str | Unset = UNSET
    """ Further detail about this entry. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        limit = self.limit

        actual: bool | float | str | Unset
        if isinstance(self.actual, Unset):
            actual = UNSET
        else:
            actual = self.actual

        parameter = self.parameter

        count = self.count

        max_ = self.max_

        max_items = self.max_items

        monitors = self.monitors

        buckets = self.buckets

        cells = self.cells

        reason = self.reason

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if limit is not UNSET:
            field_dict["limit"] = limit
        if actual is not UNSET:
            field_dict["actual"] = actual
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if count is not UNSET:
            field_dict["count"] = count
        if max_ is not UNSET:
            field_dict["max"] = max_
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if monitors is not UNSET:
            field_dict["monitors"] = monitors
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if cells is not UNSET:
            field_dict["cells"] = cells
        if reason is not UNSET:
            field_dict["reason"] = reason
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        limit = d.pop("limit", UNSET)

        def _parse_actual(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        actual = _parse_actual(d.pop("actual", UNSET))

        parameter = d.pop("parameter", UNSET)

        count = d.pop("count", UNSET)

        max_ = d.pop("max", UNSET)

        max_items = d.pop("maxItems", UNSET)

        monitors = d.pop("monitors", UNSET)

        buckets = d.pop("buckets", UNSET)

        cells = d.pop("cells", UNSET)

        reason = d.pop("reason", UNSET)

        detail = d.pop("detail", UNSET)

        too_many_items_error = cls(
            pointer=pointer,
            limit=limit,
            actual=actual,
            parameter=parameter,
            count=count,
            max_=max_,
            max_items=max_items,
            monitors=monitors,
            buckets=buckets,
            cells=cells,
            reason=reason,
            detail=detail,
        )

        too_many_items_error.additional_properties = d
        return too_many_items_error

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
