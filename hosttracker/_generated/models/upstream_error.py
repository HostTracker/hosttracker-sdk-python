from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upstream_error_code import UpstreamErrorCode, check_upstream_error_code
from ..models.upstream_error_status import UpstreamErrorStatus, check_upstream_error_status
from ..models.upstream_error_type import UpstreamErrorType, check_upstream_error_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upstream_error_detail import UpstreamErrorDetail


T = TypeVar("T", bound="UpstreamError")


@_attrs_define
class UpstreamError:
    """A service this request depends on failed."""

    type_: UpstreamErrorType
    """ This code's documentation address. """
    title: str
    """ A service this request depends on failed. """
    status: UpstreamErrorStatus
    """ The status this code always carries. """
    code: UpstreamErrorCode
    """ The stable machine code. Branch on this. """
    detail: str | Unset = UNSET
    """ Human detail about this occurrence. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on. """
    errors: list[UpstreamErrorDetail] | Unset = UNSET
    """ One entry per offending value, carrying `service`, `retryAfter`, `origin`, `outcome`, `notificationId`,
    `externalId` and `error`. """
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
        from ..models.upstream_error_detail import UpstreamErrorDetail

        d = dict(src_dict)
        type_ = check_upstream_error_type(d.pop("type"))

        title = d.pop("title")

        status = check_upstream_error_status(d.pop("status"))

        code = check_upstream_error_code(d.pop("code"))

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[UpstreamErrorDetail] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = UpstreamErrorDetail.from_dict(errors_item_data)

                errors.append(errors_item)

        upstream_error = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        upstream_error.additional_properties = d
        return upstream_error

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
