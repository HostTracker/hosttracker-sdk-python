from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_not_allowed_code import IpNotAllowedCode, check_ip_not_allowed_code
from ..models.ip_not_allowed_status import IpNotAllowedStatus, check_ip_not_allowed_status
from ..models.ip_not_allowed_type import IpNotAllowedType, check_ip_not_allowed_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_not_allowed_error import IpNotAllowedError


T = TypeVar("T", bound="IpNotAllowed")


@_attrs_define
class IpNotAllowed:
    """The caller's IP address is not on this token's allow-list."""

    type_: IpNotAllowedType
    """ This code's documentation address. """
    title: str
    """ The caller's IP address is not on this token's allow-list. """
    status: IpNotAllowedStatus
    """ The status this code always carries. """
    code: IpNotAllowedCode
    """ The stable machine code. Branch on this. """
    detail: str | Unset = UNSET
    """ Human detail about this occurrence. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on. """
    errors: list[IpNotAllowedError] | Unset = UNSET
    """ One entry per offending value, carrying `clientIp`. """
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
        from ..models.ip_not_allowed_error import IpNotAllowedError

        d = dict(src_dict)
        type_ = check_ip_not_allowed_type(d.pop("type"))

        title = d.pop("title")

        status = check_ip_not_allowed_status(d.pop("status"))

        code = check_ip_not_allowed_code(d.pop("code"))

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[IpNotAllowedError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = IpNotAllowedError.from_dict(errors_item_data)

                errors.append(errors_item)

        ip_not_allowed = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        ip_not_allowed.additional_properties = d
        return ip_not_allowed

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
