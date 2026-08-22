from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_write_only_code import CredentialWriteOnlyCode, check_credential_write_only_code
from ..models.credential_write_only_status import CredentialWriteOnlyStatus, check_credential_write_only_status
from ..models.credential_write_only_type import CredentialWriteOnlyType, check_credential_write_only_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_write_only_error import CredentialWriteOnlyError


T = TypeVar("T", bound="CredentialWriteOnly")


@_attrs_define
class CredentialWriteOnly:
    """The read sentinel cannot be sent as a credential value."""

    type_: CredentialWriteOnlyType
    """ This code's documentation address. """
    title: str
    """ The read sentinel cannot be sent as a credential value. """
    status: CredentialWriteOnlyStatus
    """ The status this code always carries. """
    code: CredentialWriteOnlyCode
    """ The stable machine code. Branch on this. """
    detail: str | Unset = UNSET
    """ Human detail about this occurrence. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on. """
    errors: list[CredentialWriteOnlyError] | Unset = UNSET
    """ One entry per offending value, carrying `pointer`. """
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
        from ..models.credential_write_only_error import CredentialWriteOnlyError

        d = dict(src_dict)
        type_ = check_credential_write_only_type(d.pop("type"))

        title = d.pop("title")

        status = check_credential_write_only_status(d.pop("status"))

        code = check_credential_write_only_code(d.pop("code"))

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[CredentialWriteOnlyError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = CredentialWriteOnlyError.from_dict(errors_item_data)

                errors.append(errors_item)

        credential_write_only = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        credential_write_only.additional_properties = d
        return credential_write_only

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
