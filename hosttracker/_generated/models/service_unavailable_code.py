from typing import Literal

ServiceUnavailableCode = Literal["service_unavailable"]

SERVICE_UNAVAILABLE_CODE_VALUES: set[ServiceUnavailableCode] = {
    "service_unavailable",
}


def check_service_unavailable_code(value: str) -> ServiceUnavailableCode:
    if value in SERVICE_UNAVAILABLE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_UNAVAILABLE_CODE_VALUES!r}")
