from typing import Literal

SelectionMismatchStatus = Literal[409]

SELECTION_MISMATCH_STATUS_VALUES: set[SelectionMismatchStatus] = {
    409,
}


def check_selection_mismatch_status(value: int) -> SelectionMismatchStatus:
    if value in SELECTION_MISMATCH_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SELECTION_MISMATCH_STATUS_VALUES!r}")
