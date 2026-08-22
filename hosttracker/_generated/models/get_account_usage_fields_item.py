from typing import Literal

GetAccountUsageFieldsItem = Literal["contact", "maintenance", "monitor", "report"]

GET_ACCOUNT_USAGE_FIELDS_ITEM_VALUES: set[GetAccountUsageFieldsItem] = {
    "contact",
    "maintenance",
    "monitor",
    "report",
}


def check_get_account_usage_fields_item(value: str) -> GetAccountUsageFieldsItem:
    if value in GET_ACCOUNT_USAGE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ACCOUNT_USAGE_FIELDS_ITEM_VALUES!r}")
