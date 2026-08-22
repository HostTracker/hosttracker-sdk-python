from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_page_settings import StatusPageSettings


T = TypeVar("T", bound="StatusPagePatchRequest")


@_attrs_define
class StatusPagePatchRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    settings: StatusPageSettings | Unset = UNSET
    """ How the public page looks and behaves. Only the members you send change; an explicit null clears a clearable
    one. """
    title: str | Unset = UNSET
    """ The heading the public page carries. """

    def to_dict(self) -> dict[str, Any]:
        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_page_settings import StatusPageSettings

        d = dict(src_dict)
        _settings = d.pop("settings", UNSET)
        settings: StatusPageSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = StatusPageSettings.from_dict(_settings)

        title = d.pop("title", UNSET)

        status_page_patch_request = cls(
            settings=settings,
            title=title,
        )

        return status_page_patch_request
