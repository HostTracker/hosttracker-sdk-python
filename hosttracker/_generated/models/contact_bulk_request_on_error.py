from typing import Literal

ContactBulkRequestOnError = Literal["continue", "stop"]

CONTACT_BULK_REQUEST_ON_ERROR_VALUES: set[ContactBulkRequestOnError] = {
    "continue",
    "stop",
}


def check_contact_bulk_request_on_error(value: str) -> ContactBulkRequestOnError:
    if value in CONTACT_BULK_REQUEST_ON_ERROR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_BULK_REQUEST_ON_ERROR_VALUES!r}")
