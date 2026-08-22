from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.report_generate_request_format import ReportGenerateRequestFormat, check_report_generate_request_format
from ..models.report_generate_request_sections_item import (
    ReportGenerateRequestSectionsItem,
    check_report_generate_request_sections_item,
)
from ..models.report_generate_request_type import ReportGenerateRequestType, check_report_generate_request_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_callback import JobCallback


T = TypeVar("T", bound="ReportGenerateRequest")


@_attrs_define
class ReportGenerateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    monitor_ids: list[UUID]
    """ The monitors this applies to. """
    callback: JobCallback | Unset = UNSET
    """ A webhook to call when the job finishes, carrying the terminal job document and its first page of results.
    Send null for none. """
    format_: ReportGenerateRequestFormat | Unset = UNSET
    """ The output format. """
    from_: int | Unset = UNSET
    """ The start of the time window, in Unix seconds. """
    language: str | Unset = UNSET
    """ The language notifications are rendered in. Send null to fall back to the account's. """
    sections: list[ReportGenerateRequestSectionsItem] | Unset = UNSET
    """ Which content blocks the document includes. Absent means the statistics block alone. """
    timezone: str | Unset = UNSET
    """ The zone this request's clock times are read in, as an IANA zone id - "Europe/Berlin", not "W. Europe
    Standard Time". A Windows spelling is refused with the exact IANA id to send in the problem's `expected`. It is
    also the spelling returned - with one documented exception: several IANA zones share one stored zone, so a value
    read back can be the group's representative rather than the id you sent ("Europe/Rome" reads back as
    "Europe/Berlin"). The clock and the daylight-saving rules are the ones you asked for; only the label can be re-
    spelled. """
    to: int | Unset = UNSET
    """ The end of the time window, in Unix seconds. """
    type_: ReportGenerateRequestType | Unset = UNSET
    """ Which report to render. """

    def to_dict(self) -> dict[str, Any]:
        monitor_ids = []
        for monitor_ids_item_data in self.monitor_ids:
            monitor_ids_item = str(monitor_ids_item_data)
            monitor_ids.append(monitor_ids_item)

        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        from_ = self.from_

        language = self.language

        sections: list[str] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item: str = sections_item_data
                sections.append(sections_item)

        timezone = self.timezone

        to = self.to

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitorIds": monitor_ids,
            }
        )
        if callback is not UNSET:
            field_dict["callback"] = callback
        if format_ is not UNSET:
            field_dict["format"] = format_
        if from_ is not UNSET:
            field_dict["from"] = from_
        if language is not UNSET:
            field_dict["language"] = language
        if sections is not UNSET:
            field_dict["sections"] = sections
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if to is not UNSET:
            field_dict["to"] = to
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_callback import JobCallback

        d = dict(src_dict)
        monitor_ids = []
        _monitor_ids = d.pop("monitorIds")
        for monitor_ids_item_data in _monitor_ids:
            monitor_ids_item = UUID(monitor_ids_item_data)

            monitor_ids.append(monitor_ids_item)

        _callback = d.pop("callback", UNSET)
        callback: JobCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = JobCallback.from_dict(_callback)

        _format_ = d.pop("format", UNSET)
        format_: ReportGenerateRequestFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_report_generate_request_format(_format_)

        from_ = d.pop("from", UNSET)

        language = d.pop("language", UNSET)

        _sections = d.pop("sections", UNSET)
        sections: list[ReportGenerateRequestSectionsItem] | Unset = UNSET
        if _sections is not UNSET:
            sections = []
            for sections_item_data in _sections:
                sections_item = check_report_generate_request_sections_item(sections_item_data)

                sections.append(sections_item)

        timezone = d.pop("timezone", UNSET)

        to = d.pop("to", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ReportGenerateRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_report_generate_request_type(_type_)

        report_generate_request = cls(
            monitor_ids=monitor_ids,
            callback=callback,
            format_=format_,
            from_=from_,
            language=language,
            sections=sections,
            timezone=timezone,
            to=to,
            type_=type_,
        )

        return report_generate_request
