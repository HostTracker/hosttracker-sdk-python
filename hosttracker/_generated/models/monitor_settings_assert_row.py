from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.monitor_settings_assert_row_op import MonitorSettingsAssertRowOp, check_monitor_settings_assert_row_op
from ..models.monitor_settings_assert_row_val_t import (
    MonitorSettingsAssertRowValT,
    check_monitor_settings_assert_row_val_t,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSettingsAssertRow")


@_attrs_define
class MonitorSettingsAssertRow:
    """One assertion. The row's operator decides which operand members are legal."""

    sub: str
    """ The SUBJECT - what is being asserted about, as a canonical AssertRuleLang expression (`status`,
    `body.json.path("$.ok")`, `header("etag")`). """
    op: MonitorSettingsAssertRowOp
    """ The predicate. Case-sensitive; an unknown operator is refused rather than ignored. """
    name: str | Unset = UNSET
    """ A label for this row, used in the failure message. Cosmetic. """
    not_: bool | Unset = False
    """ Negates the predicate. """
    val: Any | Unset = UNSET
    """ The operand, as a TYPED literal - the JSON type is part of the value, so `true` and `"true"` are different
    operands. An explicit null IS the null literal; omitting the member means no operand at all. For the comparison
    and text operators; mutually exclusive with `valSub`, and refused by the nullary ones. Accepts
    string/number/boolean/null. """
    val_t: MonitorSettingsAssertRowValT | Unset = UNSET
    """ Marks `val` as a DOCUMENT to compare structurally rather than as a scalar literal. Only alongside `val`, and
    only for `eq` and `contains`. """
    vals: list[Any] | Unset = UNSET
    """ The operand LIST, for `containsAny`, `containsAll` and `in`. `in` additionally accepts range strings -
    `"5..10"`, `"..399"`, `"400.."`, and the exclusive forms `"5<..10"`/`"5..<10"`/`"5<..<10"`. Never empty, and
    never a boolean. """
    val_sub: str | Unset = UNSET
    """ A SECOND subject expression to compare against, instead of a literal - which is how a row asserts one part
    of the response against another. Mutually exclusive with `val`. """
    nocase: bool | Unset = False
    """ Compare text case-insensitively. """

    def to_dict(self) -> dict[str, Any]:
        sub = self.sub

        op: str = self.op

        name = self.name

        not_ = self.not_

        val = self.val

        val_t: str | Unset = UNSET
        if not isinstance(self.val_t, Unset):
            val_t = self.val_t

        vals: list[Any] | Unset = UNSET
        if not isinstance(self.vals, Unset):
            vals = self.vals

        val_sub = self.val_sub

        nocase = self.nocase

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sub": sub,
                "op": op,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if not_ is not UNSET:
            field_dict["not"] = not_
        if val is not UNSET:
            field_dict["val"] = val
        if val_t is not UNSET:
            field_dict["valT"] = val_t
        if vals is not UNSET:
            field_dict["vals"] = vals
        if val_sub is not UNSET:
            field_dict["valSub"] = val_sub
        if nocase is not UNSET:
            field_dict["nocase"] = nocase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub = d.pop("sub")

        op = check_monitor_settings_assert_row_op(d.pop("op"))

        name = d.pop("name", UNSET)

        not_ = d.pop("not", UNSET)

        val = d.pop("val", UNSET)

        _val_t = d.pop("valT", UNSET)
        val_t: MonitorSettingsAssertRowValT | Unset
        if isinstance(_val_t, Unset):
            val_t = UNSET
        else:
            val_t = check_monitor_settings_assert_row_val_t(_val_t)

        vals = cast(list[Any], d.pop("vals", UNSET))

        val_sub = d.pop("valSub", UNSET)

        nocase = d.pop("nocase", UNSET)

        monitor_settings_assert_row = cls(
            sub=sub,
            op=op,
            name=name,
            not_=not_,
            val=val,
            val_t=val_t,
            vals=vals,
            val_sub=val_sub,
            nocase=nocase,
        )

        return monitor_settings_assert_row
