from typing import Literal

ContactValidateItemViewOverlimit = Literal["fits", "wouldDisable", "wouldFail"]

CONTACT_VALIDATE_ITEM_VIEW_OVERLIMIT_VALUES: set[ContactValidateItemViewOverlimit] = {
    "fits",
    "wouldDisable",
    "wouldFail",
}


def check_contact_validate_item_view_overlimit(value: str) -> ContactValidateItemViewOverlimit:
    if value in CONTACT_VALIDATE_ITEM_VIEW_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_VALIDATE_ITEM_VIEW_OVERLIMIT_VALUES!r}")
