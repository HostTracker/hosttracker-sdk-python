from typing import Literal

ServiceUnavailableType = Literal["https://api2.host-tracker.com/problems/service-unavailable"]

SERVICE_UNAVAILABLE_TYPE_VALUES: set[ServiceUnavailableType] = {
    "https://api2.host-tracker.com/problems/service-unavailable",
}


def check_service_unavailable_type(value: str) -> ServiceUnavailableType:
    if value in SERVICE_UNAVAILABLE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_UNAVAILABLE_TYPE_VALUES!r}")
