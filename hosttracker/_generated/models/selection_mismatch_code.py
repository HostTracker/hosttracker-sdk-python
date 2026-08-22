from typing import Literal

SelectionMismatchCode = Literal["selection_mismatch"]

SELECTION_MISMATCH_CODE_VALUES: set[SelectionMismatchCode] = {
    "selection_mismatch",
}


def check_selection_mismatch_code(value: str) -> SelectionMismatchCode:
    if value in SELECTION_MISMATCH_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SELECTION_MISMATCH_CODE_VALUES!r}")
