from typing import Literal

SelectionMismatchType = Literal["https://api2.host-tracker.com/problems/selection-mismatch"]

SELECTION_MISMATCH_TYPE_VALUES: set[SelectionMismatchType] = {
    "https://api2.host-tracker.com/problems/selection-mismatch",
}


def check_selection_mismatch_type(value: str) -> SelectionMismatchType:
    if value in SELECTION_MISMATCH_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SELECTION_MISMATCH_TYPE_VALUES!r}")
