from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_view import LocationView
    from ..models.result_recheck_failure_view import ResultRecheckFailureView


T = TypeVar("T", bound="ResultRecheckView")


@_attrs_define
class ResultRecheckView:
    """Who saw what during the recheck that confirmed (or refuted) a failure."""

    ok_locations: list[LocationView] | Unset = UNSET
    """ Locations that saw the target as UP - the disagreement that a single-agent blip is made of. """
    fail_locations: list[ResultRecheckFailureView] | Unset = UNSET
    """ Locations that confirmed a failure, grouped by the error each of them saw. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ok_locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ok_locations, Unset):
            ok_locations = []
            for ok_locations_item_data in self.ok_locations:
                ok_locations_item = ok_locations_item_data.to_dict()
                ok_locations.append(ok_locations_item)

        fail_locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fail_locations, Unset):
            fail_locations = []
            for fail_locations_item_data in self.fail_locations:
                fail_locations_item = fail_locations_item_data.to_dict()
                fail_locations.append(fail_locations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ok_locations is not UNSET:
            field_dict["okLocations"] = ok_locations
        if fail_locations is not UNSET:
            field_dict["failLocations"] = fail_locations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_view import LocationView
        from ..models.result_recheck_failure_view import ResultRecheckFailureView

        d = dict(src_dict)
        _ok_locations = d.pop("okLocations", UNSET)
        ok_locations: list[LocationView] | Unset = UNSET
        if _ok_locations is not UNSET:
            ok_locations = []
            for ok_locations_item_data in _ok_locations:
                ok_locations_item = LocationView.from_dict(ok_locations_item_data)

                ok_locations.append(ok_locations_item)

        _fail_locations = d.pop("failLocations", UNSET)
        fail_locations: list[ResultRecheckFailureView] | Unset = UNSET
        if _fail_locations is not UNSET:
            fail_locations = []
            for fail_locations_item_data in _fail_locations:
                fail_locations_item = ResultRecheckFailureView.from_dict(fail_locations_item_data)

                fail_locations.append(fail_locations_item)

        result_recheck_view = cls(
            ok_locations=ok_locations,
            fail_locations=fail_locations,
        )

        result_recheck_view.additional_properties = d
        return result_recheck_view

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
