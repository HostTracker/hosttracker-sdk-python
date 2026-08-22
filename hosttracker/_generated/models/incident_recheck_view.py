from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_recheck_confirmation_view import IncidentRecheckConfirmationView
    from ..models.location_view import LocationView


T = TypeVar("T", bound="IncidentRecheckView")


@_attrs_define
class IncidentRecheckView:
    """**The recheck constellation of an incident** - the answer to "who saw this, and did anyone disagree?", which is what
    turns a red row into something an operator can act on. It is the episode-level view of the same data the opening
    transition's `timeline[].recheck` carries, arranged around the DETECTING location rather than around the check: the
    detector, the locations that confirmed grouped by the error each of them saw, and the locations that did not.

    """

    detected_by: LocationView | None | Unset = UNSET
    """ The monitoring location whose check opened the episode. """
    confirmations: list[IncidentRecheckConfirmationView] | Unset = UNSET
    """ The locations that confirmed the failure, grouped by the error each of them saw. """
    unconfirmed: list[LocationView] | Unset = UNSET
    """ The locations that rechecked and still saw the target up. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_view import LocationView

        detected_by: dict[str, Any] | None | Unset
        if isinstance(self.detected_by, Unset):
            detected_by = UNSET
        elif isinstance(self.detected_by, LocationView):
            detected_by = self.detected_by.to_dict()
        else:
            detected_by = self.detected_by

        confirmations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.confirmations, Unset):
            confirmations = []
            for confirmations_item_data in self.confirmations:
                confirmations_item = confirmations_item_data.to_dict()
                confirmations.append(confirmations_item)

        unconfirmed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unconfirmed, Unset):
            unconfirmed = []
            for unconfirmed_item_data in self.unconfirmed:
                unconfirmed_item = unconfirmed_item_data.to_dict()
                unconfirmed.append(unconfirmed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detected_by is not UNSET:
            field_dict["detectedBy"] = detected_by
        if confirmations is not UNSET:
            field_dict["confirmations"] = confirmations
        if unconfirmed is not UNSET:
            field_dict["unconfirmed"] = unconfirmed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_recheck_confirmation_view import IncidentRecheckConfirmationView
        from ..models.location_view import LocationView

        d = dict(src_dict)

        def _parse_detected_by(data: object) -> LocationView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detected_by_type_0 = LocationView.from_dict(data)

                return detected_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocationView | None | Unset, data)

        detected_by = _parse_detected_by(d.pop("detectedBy", UNSET))

        _confirmations = d.pop("confirmations", UNSET)
        confirmations: list[IncidentRecheckConfirmationView] | Unset = UNSET
        if _confirmations is not UNSET:
            confirmations = []
            for confirmations_item_data in _confirmations:
                confirmations_item = IncidentRecheckConfirmationView.from_dict(confirmations_item_data)

                confirmations.append(confirmations_item)

        _unconfirmed = d.pop("unconfirmed", UNSET)
        unconfirmed: list[LocationView] | Unset = UNSET
        if _unconfirmed is not UNSET:
            unconfirmed = []
            for unconfirmed_item_data in _unconfirmed:
                unconfirmed_item = LocationView.from_dict(unconfirmed_item_data)

                unconfirmed.append(unconfirmed_item)

        incident_recheck_view = cls(
            detected_by=detected_by,
            confirmations=confirmations,
            unconfirmed=unconfirmed,
        )

        incident_recheck_view.additional_properties = d
        return incident_recheck_view

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
