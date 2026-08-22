from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebContentCheckSettings")


@_attrs_define
class WebContentCheckSettings:
    """Loads the page in a real headless browser, waits for it to settle, and matches keywords against the RENDERED DOM's
    visible text - the Http keyword check, but able to see JavaScript-rendered content.

    """

    keyword: str
    """ The text to look for in the RENDERED page. Semicolon-separated for several keywords. """
    case_sensitive: bool | Unset = False
    """ Match case-sensitively. """
    keyword_present: bool | Unset = True
    """ Pass when the keyword IS present; false inverts the verdict. """
    keyword_any: bool | Unset = False
    """ With several keywords, pass on any one rather than requiring all. """
    only_visible: bool | Unset = True
    """ Search only text the browser renders as visible. """
    timeout: int | Unset = 40000
    """ Page-load budget in milliseconds. 40000 is the default and is deliberately not persisted. """

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword

        case_sensitive = self.case_sensitive

        keyword_present = self.keyword_present

        keyword_any = self.keyword_any

        only_visible = self.only_visible

        timeout = self.timeout

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keyword": keyword,
            }
        )
        if case_sensitive is not UNSET:
            field_dict["caseSensitive"] = case_sensitive
        if keyword_present is not UNSET:
            field_dict["keywordPresent"] = keyword_present
        if keyword_any is not UNSET:
            field_dict["keywordAny"] = keyword_any
        if only_visible is not UNSET:
            field_dict["onlyVisible"] = only_visible
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keyword = d.pop("keyword")

        case_sensitive = d.pop("caseSensitive", UNSET)

        keyword_present = d.pop("keywordPresent", UNSET)

        keyword_any = d.pop("keywordAny", UNSET)

        only_visible = d.pop("onlyVisible", UNSET)

        timeout = d.pop("timeout", UNSET)

        web_content_check_settings = cls(
            keyword=keyword,
            case_sensitive=case_sensitive,
            keyword_present=keyword_present,
            keyword_any=keyword_any,
            only_visible=only_visible,
            timeout=timeout,
        )

        return web_content_check_settings
