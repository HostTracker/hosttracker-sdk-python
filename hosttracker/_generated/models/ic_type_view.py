from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ic_type_view_options_type_0 import IcTypeViewOptionsType0


T = TypeVar("T", bound="IcTypeView")


@_attrs_define
class IcTypeView:
    experimental: bool
    """ True while the type is not generally announced. """
    agent_routed: bool
    """ True when the check runs on the agent fleet - the only types for which `pools`/`locations` mean anything.
    Sending a location filter with a non-agent type is refused, so this is the flag that tells a client which is
    which. """
    retry_after: int
    estimated_duration_sec: int
    type_: str | Unset = UNSET
    """ The v2 type token - the SAME vocabulary `/monitor/type` publishes. """
    label: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    example: None | str | Unset = UNSET
    """ A valid `url` for this type - the shape the target is expected in. """
    options: IcTypeViewOptionsType0 | None | Unset = UNSET
    """ Per-type option vocabulary - `deviceEmulation[]` for `waterfall`, `dnsQuery[]` for `dns`. Omitted for a type
    that takes no options. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ic_type_view_options_type_0 import IcTypeViewOptionsType0

        experimental = self.experimental

        agent_routed = self.agent_routed

        retry_after = self.retry_after

        estimated_duration_sec = self.estimated_duration_sec

        type_ = self.type_

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        example: None | str | Unset
        if isinstance(self.example, Unset):
            example = UNSET
        else:
            example = self.example

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, IcTypeViewOptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "experimental": experimental,
                "agentRouted": agent_routed,
                "retryAfter": retry_after,
                "estimatedDurationSec": estimated_duration_sec,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if example is not UNSET:
            field_dict["example"] = example
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ic_type_view_options_type_0 import IcTypeViewOptionsType0

        d = dict(src_dict)
        experimental = d.pop("experimental")

        agent_routed = d.pop("agentRouted")

        retry_after = d.pop("retryAfter")

        estimated_duration_sec = d.pop("estimatedDurationSec")

        type_ = d.pop("type", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_example(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        example = _parse_example(d.pop("example", UNSET))

        def _parse_options(data: object) -> IcTypeViewOptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = IcTypeViewOptionsType0.from_dict(data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IcTypeViewOptionsType0 | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        ic_type_view = cls(
            experimental=experimental,
            agent_routed=agent_routed,
            retry_after=retry_after,
            estimated_duration_sec=estimated_duration_sec,
            type_=type_,
            label=label,
            description=description,
            example=example,
            options=options,
        )

        ic_type_view.additional_properties = d
        return ic_type_view

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
