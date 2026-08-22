from typing import Literal

ListAccountMemberFieldsItem = Literal["contact", "id", "rights", "state", "userId"]

LIST_ACCOUNT_MEMBER_FIELDS_ITEM_VALUES: set[ListAccountMemberFieldsItem] = {
    "contact",
    "id",
    "rights",
    "state",
    "userId",
}


def check_list_account_member_fields_item(value: str) -> ListAccountMemberFieldsItem:
    if value in LIST_ACCOUNT_MEMBER_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ACCOUNT_MEMBER_FIELDS_ITEM_VALUES!r}")
