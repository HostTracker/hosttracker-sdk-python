from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_validate_item_view_overlimit import (
    ContactValidateItemViewOverlimit,
    check_contact_validate_item_view_overlimit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.problem_error import ProblemError


T = TypeVar("T", bound="ContactValidateItemView")


@_attrs_define
class ContactValidateItemView:
    """One item's verdict. The `index` is the item's position in ITS OWN leg array, which is what the caller sent and can
    act on.

    """

    index: int
    valid: bool
    overlimit: ContactValidateItemViewOverlimit | Unset = UNSET
    """ `fits` | `wouldDisable` | `wouldFail` - the item's package fit under the request's own `onOverlimit` mode.
    """
    existing_id: None | Unset | UUID = UNSET
    """ The contact this item names: an update/delete target, or the row a create would BIND to. """
    would_bind: bool | None | Unset = UNSET
    would_confirm: bool | None | Unset = UNSET
    """ Whether the created contact would be born confirmed (inherited from a sibling, or a type with no out-of-band
    channel). Create items only. """
    code: None | str | Unset = UNSET
    """ The problem code this item WOULD be refused with (`validation_failed`, `package_limit`, `not_found`, …) -
    the member a client branches on. """
    errors: list[ProblemError] | None | Unset = UNSET
    """ The refusal's own `errors[]`, pointers and all - the SAME entries the write would have answered with, so a
    client renders one error shape whichever door it came through. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        valid = self.valid

        overlimit: str | Unset = UNSET
        if not isinstance(self.overlimit, Unset):
            overlimit = self.overlimit

        existing_id: None | str | Unset
        if isinstance(self.existing_id, Unset):
            existing_id = UNSET
        elif isinstance(self.existing_id, UUID):
            existing_id = str(self.existing_id)
        else:
            existing_id = self.existing_id

        would_bind: bool | None | Unset
        if isinstance(self.would_bind, Unset):
            would_bind = UNSET
        else:
            would_bind = self.would_bind

        would_confirm: bool | None | Unset
        if isinstance(self.would_confirm, Unset):
            would_confirm = UNSET
        else:
            would_confirm = self.would_confirm

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "valid": valid,
            }
        )
        if overlimit is not UNSET:
            field_dict["overlimit"] = overlimit
        if existing_id is not UNSET:
            field_dict["existingId"] = existing_id
        if would_bind is not UNSET:
            field_dict["wouldBind"] = would_bind
        if would_confirm is not UNSET:
            field_dict["wouldConfirm"] = would_confirm
        if code is not UNSET:
            field_dict["code"] = code
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.problem_error import ProblemError

        d = dict(src_dict)
        index = d.pop("index")

        valid = d.pop("valid")

        _overlimit = d.pop("overlimit", UNSET)
        overlimit: ContactValidateItemViewOverlimit | Unset
        if isinstance(_overlimit, Unset):
            overlimit = UNSET
        else:
            overlimit = check_contact_validate_item_view_overlimit(_overlimit)

        def _parse_existing_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                existing_id_type_0 = UUID(data)

                return existing_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        existing_id = _parse_existing_id(d.pop("existingId", UNSET))

        def _parse_would_bind(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        would_bind = _parse_would_bind(d.pop("wouldBind", UNSET))

        def _parse_would_confirm(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        would_confirm = _parse_would_confirm(d.pop("wouldConfirm", UNSET))

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

        contact_validate_item_view = cls(
            index=index,
            valid=valid,
            overlimit=overlimit,
            existing_id=existing_id,
            would_bind=would_bind,
            would_confirm=would_confirm,
            code=code,
            errors=errors,
        )

        contact_validate_item_view.additional_properties = d
        return contact_validate_item_view

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
