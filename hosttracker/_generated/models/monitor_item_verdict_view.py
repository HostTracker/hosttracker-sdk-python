from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_item_verdict_view_overlimit import (
    MonitorItemVerdictViewOverlimit,
    check_monitor_item_verdict_view_overlimit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.problem_error import ProblemError


T = TypeVar("T", bound="MonitorItemVerdictView")


@_attrs_define
class MonitorItemVerdictView:
    """One item's verdict. `index` correlates with the caller's own `items[]`, exactly as a job's `results[]` does."""

    index: int
    valid: bool
    """ Whether a create of this item would be accepted (a `wouldDisable` item IS accepted). """
    item_ref: None | str | Unset = UNSET
    """ The item's url, when it has one - the same correlation aid the job items carry. """
    code: None | str | Unset = UNSET
    """ The problem code the create would answer with (`validation_failed`, `duplicate_monitor`, `package_limit`,
    …). Absent when the item is valid. """
    errors: list[ProblemError] | None | Unset = UNSET
    """ That problem's error entries - `pointer` plus the code's declared remediation fields, the same shape they
    have inside a problem document. Absent when the item is valid. """
    overlimit: MonitorItemVerdictViewOverlimit | Unset = UNSET
    """ `fits` | `wouldDisable` | `wouldFail`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        valid = self.valid

        item_ref: None | str | Unset
        if isinstance(self.item_ref, Unset):
            item_ref = UNSET
        else:
            item_ref = self.item_ref

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        overlimit: str | Unset = UNSET
        if not isinstance(self.overlimit, Unset):
            overlimit = self.overlimit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "valid": valid,
            }
        )
        if item_ref is not UNSET:
            field_dict["itemRef"] = item_ref
        if code is not UNSET:
            field_dict["code"] = code
        if errors is not UNSET:
            field_dict["errors"] = errors
        if overlimit is not UNSET:
            field_dict["overlimit"] = overlimit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.problem_error import ProblemError

        d = dict(src_dict)
        index = d.pop("index")

        valid = d.pop("valid")

        def _parse_item_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_ref = _parse_item_ref(d.pop("itemRef", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_errors(data: object) -> list[ProblemError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = ProblemError.from_dict(errors_type_0_item_data)

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProblemError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        _overlimit = d.pop("overlimit", UNSET)
        overlimit: MonitorItemVerdictViewOverlimit | Unset
        if isinstance(_overlimit, Unset):
            overlimit = UNSET
        else:
            overlimit = check_monitor_item_verdict_view_overlimit(_overlimit)

        monitor_item_verdict_view = cls(
            index=index,
            valid=valid,
            item_ref=item_ref,
            code=code,
            errors=errors,
            overlimit=overlimit,
        )

        monitor_item_verdict_view.additional_properties = d
        return monitor_item_verdict_view

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
