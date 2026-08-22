from typing import Literal

AccountMemberQueryRequestFieldsItem = Literal["contact", "id", "rights", "state", "userId"]

ACCOUNT_MEMBER_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[AccountMemberQueryRequestFieldsItem] = {
    "contact",
    "id",
    "rights",
    "state",
    "userId",
}


def check_account_member_query_request_fields_item(value: str) -> AccountMemberQueryRequestFieldsItem:
    if value in ACCOUNT_MEMBER_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACCOUNT_MEMBER_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
