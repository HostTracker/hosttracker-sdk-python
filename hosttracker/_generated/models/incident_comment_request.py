from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="IncidentCommentRequest")


@_attrs_define
class IncidentCommentRequest:
    comment: str
    """ The annotation. **Required** - and required MEANS required: an omitted member is `422 validation_failed`
    pointing at `/comment`, never an empty write. **To CLEAR an existing comment, send `""` explicitly** - that is
    the whole gesture, and it is deliberately the only way to reach it. """

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        incident_comment_request = cls(
            comment=comment,
        )

        return incident_comment_request
