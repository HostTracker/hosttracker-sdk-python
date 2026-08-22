from typing import Literal

GetAccountFieldsItem = Literal[
    "badges",
    "defaultAgentPools",
    "flags",
    "id",
    "language",
    "limits",
    "login",
    "overlimits",
    "package",
    "profile",
    "quota",
    "timezone",
    "usage",
]

GET_ACCOUNT_FIELDS_ITEM_VALUES: set[GetAccountFieldsItem] = {
    "badges",
    "defaultAgentPools",
    "flags",
    "id",
    "language",
    "limits",
    "login",
    "overlimits",
    "package",
    "profile",
    "quota",
    "timezone",
    "usage",
}


def check_get_account_fields_item(value: str) -> GetAccountFieldsItem:
    if value in GET_ACCOUNT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ACCOUNT_FIELDS_ITEM_VALUES!r}")
