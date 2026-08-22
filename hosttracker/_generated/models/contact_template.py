from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.contact_template_event import ContactTemplateEvent, check_contact_template_event
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactTemplate")


@_attrs_define
class ContactTemplate:
    """One per-event message template."""

    event: ContactTemplateEvent
    """ Which alert this template renders. """
    content: str | Unset = UNSET
    """ The template body. Absent means empty. """

    def to_dict(self) -> dict[str, Any]:
        event: str = self.event

        content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = check_contact_template_event(d.pop("event"))

        content = d.pop("content", UNSET)

        contact_template = cls(
            event=event,
            content=content,
        )

        return contact_template
