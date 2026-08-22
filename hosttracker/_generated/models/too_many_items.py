from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.too_many_items_code import TooManyItemsCode, check_too_many_items_code
from ..models.too_many_items_status import TooManyItemsStatus, check_too_many_items_status
from ..models.too_many_items_type import TooManyItemsType, check_too_many_items_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.too_many_items_error import TooManyItemsError


T = TypeVar("T", bound="TooManyItems")


@_attrs_define
class TooManyItems:
    """The request carries more items than this operation accepts."""

    type_: TooManyItemsType
    """ This code's documentation address. """
    title: str
    """ The request carries more items than this operation accepts. """
    status: TooManyItemsStatus
    """ The status this code always carries. """
    code: TooManyItemsCode
    """ The stable machine code. Branch on this. """
    detail: str | Unset = UNSET
    """ Human detail about this occurrence. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on. """
    errors: list[TooManyItemsError] | Unset = UNSET
    """ One entry per offending value, carrying `limit`, `actual`, `pointer`, `parameter`, `count`, `max`,
    `maxItems`, `monitors`, `buckets`, `cells`, `reason` and `detail`. """
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
        from ..models.too_many_items_error import TooManyItemsError

        d = dict(src_dict)
        type_ = check_too_many_items_type(d.pop("type"))

        title = d.pop("title")

        status = check_too_many_items_status(d.pop("status"))

        code = check_too_many_items_code(d.pop("code"))

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[TooManyItemsError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = TooManyItemsError.from_dict(errors_item_data)

                errors.append(errors_item)

        too_many_items = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        too_many_items.additional_properties = d
        return too_many_items

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
