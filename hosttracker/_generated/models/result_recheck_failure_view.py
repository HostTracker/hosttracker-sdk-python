from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_view import LocationView
    from ..models.result_error_view import ResultErrorView


T = TypeVar("T", bound="ResultRecheckFailureView")


@_attrs_define
class ResultRecheckFailureView:
    """One error and the locations that saw it."""

    error: ResultErrorView | Unset = UNSET
    """ The error taxonomy of a failed check - typed members, never a prose blob. """
    locations: list[LocationView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_view import LocationView
        from ..models.result_error_view import ResultErrorView

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: ResultErrorView | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ResultErrorView.from_dict(_error)

        _locations = d.pop("locations", UNSET)
        locations: list[LocationView] | Unset = UNSET
        if _locations is not UNSET:
            locations = []
            for locations_item_data in _locations:
                locations_item = LocationView.from_dict(locations_item_data)

                locations.append(locations_item)

        result_recheck_failure_view = cls(
            error=error,
            locations=locations,
        )

        result_recheck_failure_view.additional_properties = d
        return result_recheck_failure_view

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
