from typing import Literal

GetAccountQuotaFieldsItem = Literal[
    "apiEnabled", "limit", "pools", "remaining", "resetAt", "scopes", "tokenCap", "used"
]

GET_ACCOUNT_QUOTA_FIELDS_ITEM_VALUES: set[GetAccountQuotaFieldsItem] = {
    "apiEnabled",
    "limit",
    "pools",
    "remaining",
    "resetAt",
    "scopes",
    "tokenCap",
    "used",
}


def check_get_account_quota_fields_item(value: str) -> GetAccountQuotaFieldsItem:
    if value in GET_ACCOUNT_QUOTA_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ACCOUNT_QUOTA_FIELDS_ITEM_VALUES!r}")
