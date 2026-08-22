from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageSpeedSettings")


@_attrs_define
class PageSpeedSettings:
    """Loads the page in a real browser from the chosen locations and measures every element's download and execution,
    failing the check when a configured budget is exceeded.

    """

    timeout: int | Unset = UNSET
    """ Whole-page budget in milliseconds. """
    xhr: int | Unset = UNSET
    """ Budget for the slowest XHR, in milliseconds. STORED under the shouted key `XHR` - the v2 wire uses `xhr`.
    """
    total_count: int | Unset = UNSET
    """ Fail the check when the total number of requests exceeds this value. """
    on_document: int | Unset = UNSET
    """ Fail the check when the number of document requests exceeds this value. """
    on_script: int | Unset = UNSET
    """ Fail the check when the number of script requests exceeds this value. """
    on_stylesheet: int | Unset = UNSET
    """ Fail the check when the number of stylesheet requests exceeds this value. """
    on_image: int | Unset = UNSET
    """ Fail the check when the number of image requests exceeds this value. """
    on_font: int | Unset = UNSET
    """ Fail the check when the number of font requests exceeds this value. """
    on_ajax: int | Unset = UNSET
    """ Fail the check when the number of ajax requests exceeds this value. """
    on_cpu: int | Unset = UNSET
    """ Fail when CPU utilisation percent exceeds this. The only budget with a non-zero floor - values below 80 are
    refused. """
    on_ram: int | Unset = UNSET
    """ Fail the check when memory use in megabytes exceeds this value. """
    on_console_warning: int | Unset = UNSET
    """ Fail the check when the number of console warnings exceeds this value. """
    on_console_error: int | Unset = UNSET
    """ Fail the check when the number of console errors exceeds this value. """
    device_emulation: str | Unset = "Desktop"
    """ Device profile to emulate. Validated against the live device list the check engine publishes. "Desktop" is
    the implicit default and is never persisted. """

    def to_dict(self) -> dict[str, Any]:
        timeout = self.timeout

        xhr = self.xhr

        total_count = self.total_count

        on_document = self.on_document

        on_script = self.on_script

        on_stylesheet = self.on_stylesheet

        on_image = self.on_image

        on_font = self.on_font

        on_ajax = self.on_ajax

        on_cpu = self.on_cpu

        on_ram = self.on_ram

        on_console_warning = self.on_console_warning

        on_console_error = self.on_console_error

        device_emulation = self.device_emulation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if xhr is not UNSET:
            field_dict["xhr"] = xhr
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if on_document is not UNSET:
            field_dict["onDocument"] = on_document
        if on_script is not UNSET:
            field_dict["onScript"] = on_script
        if on_stylesheet is not UNSET:
            field_dict["onStylesheet"] = on_stylesheet
        if on_image is not UNSET:
            field_dict["onImage"] = on_image
        if on_font is not UNSET:
            field_dict["onFont"] = on_font
        if on_ajax is not UNSET:
            field_dict["onAjax"] = on_ajax
        if on_cpu is not UNSET:
            field_dict["onCpu"] = on_cpu
        if on_ram is not UNSET:
            field_dict["onRam"] = on_ram
        if on_console_warning is not UNSET:
            field_dict["onConsoleWarning"] = on_console_warning
        if on_console_error is not UNSET:
            field_dict["onConsoleError"] = on_console_error
        if device_emulation is not UNSET:
            field_dict["deviceEmulation"] = device_emulation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeout = d.pop("timeout", UNSET)

        xhr = d.pop("xhr", UNSET)

        total_count = d.pop("totalCount", UNSET)

        on_document = d.pop("onDocument", UNSET)

        on_script = d.pop("onScript", UNSET)

        on_stylesheet = d.pop("onStylesheet", UNSET)

        on_image = d.pop("onImage", UNSET)

        on_font = d.pop("onFont", UNSET)

        on_ajax = d.pop("onAjax", UNSET)

        on_cpu = d.pop("onCpu", UNSET)

        on_ram = d.pop("onRam", UNSET)

        on_console_warning = d.pop("onConsoleWarning", UNSET)

        on_console_error = d.pop("onConsoleError", UNSET)

        device_emulation = d.pop("deviceEmulation", UNSET)

        page_speed_settings = cls(
            timeout=timeout,
            xhr=xhr,
            total_count=total_count,
            on_document=on_document,
            on_script=on_script,
            on_stylesheet=on_stylesheet,
            on_image=on_image,
            on_font=on_font,
            on_ajax=on_ajax,
            on_cpu=on_cpu,
            on_ram=on_ram,
            on_console_warning=on_console_warning,
            on_console_error=on_console_error,
            device_emulation=device_emulation,
        )

        return page_speed_settings
