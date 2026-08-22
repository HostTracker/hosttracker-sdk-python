from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_type_row import MonitorTypeRow
    from ..models.monitor_type_schema_view_attached_schema_type_0 import MonitorTypeSchemaViewAttachedSchemaType0
    from ..models.monitor_type_schema_view_schema import MonitorTypeSchemaViewSchema


T = TypeVar("T", bound="MonitorTypeSchemaView")


@_attrs_define
class MonitorTypeSchemaView:
    type_: MonitorTypeRow
    schema: MonitorTypeSchemaViewSchema
    """ JSON Schema draft 2020-12 for this type's `settings` object. """
    attached_schema: MonitorTypeSchemaViewAttachedSchemaType0 | None | Unset = UNSET
    """ The shape this type takes as a sub-check on a parent monitor. Present only for `dnsbl`, `domainExp`,
    `sslExp` and `webRisk`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_type_schema_view_attached_schema_type_0 import MonitorTypeSchemaViewAttachedSchemaType0

        type_ = self.type_.to_dict()

        schema = self.schema.to_dict()

        attached_schema: dict[str, Any] | None | Unset
        if isinstance(self.attached_schema, Unset):
            attached_schema = UNSET
        elif isinstance(self.attached_schema, MonitorTypeSchemaViewAttachedSchemaType0):
            attached_schema = self.attached_schema.to_dict()
        else:
            attached_schema = self.attached_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "schema": schema,
            }
        )
        if attached_schema is not UNSET:
            field_dict["attachedSchema"] = attached_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_type_row import MonitorTypeRow
        from ..models.monitor_type_schema_view_attached_schema_type_0 import MonitorTypeSchemaViewAttachedSchemaType0
        from ..models.monitor_type_schema_view_schema import MonitorTypeSchemaViewSchema

        d = dict(src_dict)
        type_ = MonitorTypeRow.from_dict(d.pop("type"))

        schema = MonitorTypeSchemaViewSchema.from_dict(d.pop("schema"))

        def _parse_attached_schema(data: object) -> MonitorTypeSchemaViewAttachedSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attached_schema_type_0 = MonitorTypeSchemaViewAttachedSchemaType0.from_dict(data)

                return attached_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MonitorTypeSchemaViewAttachedSchemaType0 | None | Unset, data)

        attached_schema = _parse_attached_schema(d.pop("attachedSchema", UNSET))

        monitor_type_schema_view = cls(
            type_=type_,
            schema=schema,
            attached_schema=attached_schema,
        )

        monitor_type_schema_view.additional_properties = d
        return monitor_type_schema_view

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
