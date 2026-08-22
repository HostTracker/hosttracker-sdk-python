from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.status_page_template_write_request_default_impact import (
    StatusPageTemplateWriteRequestDefaultImpact,
    check_status_page_template_write_request_default_impact,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageTemplateWriteRequest")


@_attrs_define
class StatusPageTemplateWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    message: str
    """ The message body the preset carries. """
    title: str
    """ The title a declaration made from this preset starts with. """
    default_impact: StatusPageTemplateWriteRequestDefaultImpact | Unset = UNSET
    """ The impact a declaration made from this preset starts with. Defaults to `minor`. """

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        title = self.title

        default_impact: str | Unset = UNSET
        if not isinstance(self.default_impact, Unset):
            default_impact = self.default_impact

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
                "title": title,
            }
        )
        if default_impact is not UNSET:
            field_dict["defaultImpact"] = default_impact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        title = d.pop("title")

        _default_impact = d.pop("defaultImpact", UNSET)
        default_impact: StatusPageTemplateWriteRequestDefaultImpact | Unset
        if isinstance(_default_impact, Unset):
            default_impact = UNSET
        else:
            default_impact = check_status_page_template_write_request_default_impact(_default_impact)

        status_page_template_write_request = cls(
            message=message,
            title=title,
            default_impact=default_impact,
        )

        return status_page_template_write_request
