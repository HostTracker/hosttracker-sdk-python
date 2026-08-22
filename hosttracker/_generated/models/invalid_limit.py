from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invalid_limit_code import InvalidLimitCode, check_invalid_limit_code
from ..models.invalid_limit_status import InvalidLimitStatus, check_invalid_limit_status
from ..models.invalid_limit_type import InvalidLimitType, check_invalid_limit_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invalid_limit_error import InvalidLimitError


T = TypeVar("T", bound="InvalidLimit")


@_attrs_define
class InvalidLimit:
    """The requested page size is outside the allowed range."""

    type_: InvalidLimitType
    """ This code's documentation address. """
    title: str
    """ The requested page size is outside the allowed range. """
    status: InvalidLimitStatus
    """ The status this code always carries. """
    code: InvalidLimitCode
    """ The stable machine code. Branch on this. """
    detail: str | Unset = UNSET
    """ Human detail about this occurrence. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on. """
    errors: list[InvalidLimitError] | Unset = UNSET
    """ One entry per offending value, carrying `parameter`, `value`, `min` and `max`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        title = self.title

        status: int = self.status

        code: str = self.code

        detail = self.detail

        instance = self.instance

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "status": status,
                "code": code,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invalid_limit_error import InvalidLimitError

        d = dict(src_dict)
        type_ = check_invalid_limit_type(d.pop("type"))

        title = d.pop("title")

        status = check_invalid_limit_status(d.pop("status"))

        code = check_invalid_limit_code(d.pop("code"))

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[InvalidLimitError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = InvalidLimitError.from_dict(errors_item_data)

                errors.append(errors_item)

        invalid_limit = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        invalid_limit.additional_properties = d
        return invalid_limit

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
