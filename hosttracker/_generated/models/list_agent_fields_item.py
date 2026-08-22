from typing import Literal

ListAgentFieldsItem = Literal[
    "capabilities",
    "city",
    "country",
    "id",
    "ip",
    "ipv6",
    "lat",
    "lon",
    "name",
    "pools",
    "provider",
    "region",
    "upFrom",
    "version",
    "visible",
]

LIST_AGENT_FIELDS_ITEM_VALUES: set[ListAgentFieldsItem] = {
    "capabilities",
    "city",
    "country",
    "id",
    "ip",
    "ipv6",
    "lat",
    "lon",
    "name",
    "pools",
    "provider",
    "region",
    "upFrom",
    "version",
    "visible",
}


def check_list_agent_fields_item(value: str) -> ListAgentFieldsItem:
    if value in LIST_AGENT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGENT_FIELDS_ITEM_VALUES!r}")
