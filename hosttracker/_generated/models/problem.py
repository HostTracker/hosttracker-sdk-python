from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.problem_error import ProblemError


T = TypeVar("T", bound="Problem")


@_attrs_define
class Problem:
    """An RFC 9457 problem document. `code` is the member to branch on - not `title` or `detail`, which are for humans and
    may be reworded, and not `type`, which is a documentation address. `type` spells the same identity in kebab-case
    (`.../problems/not-found`) where `code` is snake_case (`not_found`); both dereference to the same page, and only one
    of them is a stable branch key. The machine-actionable remediation is in `errors[]`, whose members differ per code
    and are documented on each code's own schema.

    """

    type_: str
    """ The problem type's documentation address. Dereference it to read what this code means. """
    title: str
    """ A short human summary of the problem type. Carries no data. """
    status: int
    """ The HTTP status, repeated in the body. """
    code: str
    """ The stable machine code. This is the member to branch on. """
    detail: str | Unset = UNSET
    """ Human detail about this particular occurrence, when there is any. """
    instance: str | Unset = UNSET
    """ The path the failure occurred on, when it is meaningful. """
    errors: list[ProblemError] | Unset = UNSET
    """ One entry per offending value, each naming where the problem is and carrying the members that fix it. Absent
    when the problem is not value-scoped. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        code = self.code

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
        from ..models.problem_error import ProblemError

        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        code = d.pop("code")

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ProblemError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ProblemError.from_dict(errors_item_data)

                errors.append(errors_item)

        problem = cls(
            type_=type_,
            title=title,
            status=status,
            code=code,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        problem.additional_properties = d
        return problem

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
