from typing import Literal

ServiceUnavailableStatus = Literal[503]

SERVICE_UNAVAILABLE_STATUS_VALUES: set[ServiceUnavailableStatus] = {
    503,
}


def check_service_unavailable_status(value: int) -> ServiceUnavailableStatus:
    if value in SERVICE_UNAVAILABLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_UNAVAILABLE_STATUS_VALUES!r}")
