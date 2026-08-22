from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_unavailable_code import ServiceUnavailableCode, check_service_unavailable_code
from ..models.service_unavailable_status import ServiceUnavailableStatus, check_service_unavailable_status
from ..models.service_unavailable_type import ServiceUnavailableType, check_service_unavailable_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_unavailable_error import ServiceUnavailableError


T = TypeVar("T", bound="ServiceUnavailable")


@_attrs_define
class ServiceUnavailable:
    """The service is temporarily unavailable."""

    type_: ServiceUnavailableType
    """ This code's documentation address. """
    title: str
    """ The service is temporarily unavailable. """
    status: ServiceUnavailableStatus
    """ The status this code always carries. """
    code: ServiceUnavailableCode
    """ The stable machine code. Branch on this. """
    detail: str | Unset = UNSET
    """ Human detail about this occurrence. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on. """
    errors: list[ServiceUnavailableError] | Unset = UNSET
    """ One entry per offending value, carrying `service`, `retryAfter`, `reason`, `retryAfterSeconds` and `detail`.
    """
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
        from ..models.service_unavailable_error import ServiceUnavailableError

        d = dict(src_dict)
        type_ = check_service_unavailable_type(d.pop("type"))

        title = d.pop("title")

        status = check_service_unavailable_status(d.pop("status"))

        code = check_service_unavailable_code(d.pop("code"))

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ServiceUnavailableError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ServiceUnavailableError.from_dict(errors_item_data)

                errors.append(errors_item)

        service_unavailable = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        service_unavailable.additional_properties = d
        return service_unavailable

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
