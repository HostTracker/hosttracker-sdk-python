from typing import Literal

AgentQueryRequestFieldsItem = Literal[
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

AGENT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[AgentQueryRequestFieldsItem] = {
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


def check_agent_query_request_fields_item(value: str) -> AgentQueryRequestFieldsItem:
    if value in AGENT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
