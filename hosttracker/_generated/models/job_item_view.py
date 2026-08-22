from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_item_view_status import JobItemViewStatus, check_job_item_view_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_item_view_error_type_0 import JobItemViewErrorType0
    from ..models.job_item_view_result_type_0 import JobItemViewResultType0


T = TypeVar("T", bound="JobItemView")


@_attrs_define
class JobItemView:
    index: int
    """ Position in the caller's `items[]`. """
    item_ref: None | str | Unset = UNSET
    status: JobItemViewStatus | Unset = UNSET
    """ What the job did with this one item. `pending` means it has not been reached yet; the rest are final for
    that item. """
    entity_id: None | Unset | UUID = UNSET
    result: JobItemViewResultType0 | None | Unset = UNSET
    """ The FULL representation of the affected entity - what removes the re-read leg. **Rehydrated, not stored**:
    it is the entity as it stands NOW, rendered at the POLLING caller's credential tier. Only a receipt for an
    entity that no longer exists (a deletion) comes from storage. """
    error: JobItemViewErrorType0 | None | Unset = UNSET
    """ A FULL problem document for a failed item. """
    processed_at: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job_item_view_error_type_0 import JobItemViewErrorType0
        from ..models.job_item_view_result_type_0 import JobItemViewResultType0

        index = self.index

        item_ref: None | str | Unset
        if isinstance(self.item_ref, Unset):
            item_ref = UNSET
        else:
            item_ref = self.item_ref

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, JobItemViewResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, JobItemViewErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        processed_at: int | None | Unset
        if isinstance(self.processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = self.processed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
            }
        )
        if item_ref is not UNSET:
            field_dict["itemRef"] = item_ref
        if status is not UNSET:
            field_dict["status"] = status
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_item_view_error_type_0 import JobItemViewErrorType0
        from ..models.job_item_view_result_type_0 import JobItemViewResultType0

        d = dict(src_dict)
        index = d.pop("index")

        def _parse_item_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_ref = _parse_item_ref(d.pop("itemRef", UNSET))

        _status = d.pop("status", UNSET)
        status: JobItemViewStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_job_item_view_status(_status)

        def _parse_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)

                return entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        entity_id = _parse_entity_id(d.pop("entityId", UNSET))

        def _parse_result(data: object) -> JobItemViewResultType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = JobItemViewResultType0.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobItemViewResultType0 | None | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_error(data: object) -> JobItemViewErrorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = JobItemViewErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobItemViewErrorType0 | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_processed_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        processed_at = _parse_processed_at(d.pop("processedAt", UNSET))

        job_item_view = cls(
            index=index,
            item_ref=item_ref,
            status=status,
            entity_id=entity_id,
            result=result,
            error=error,
            processed_at=processed_at,
        )

        job_item_view.additional_properties = d
        return job_item_view

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
