from typing import Literal

AccountMemberViewState = Literal["active", "disabled", "pending"]

ACCOUNT_MEMBER_VIEW_STATE_VALUES: set[AccountMemberViewState] = {
    "active",
    "disabled",
    "pending",
}


def check_account_member_view_state(value: str) -> AccountMemberViewState:
    if value in ACCOUNT_MEMBER_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_MEMBER_VIEW_STATE_VALUES!r}")
