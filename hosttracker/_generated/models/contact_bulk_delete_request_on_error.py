from typing import Literal

ContactBulkDeleteRequestOnError = Literal["continue", "stop"]

CONTACT_BULK_DELETE_REQUEST_ON_ERROR_VALUES: set[ContactBulkDeleteRequestOnError] = {
    "continue",
    "stop",
}


def check_contact_bulk_delete_request_on_error(value: str) -> ContactBulkDeleteRequestOnError:
    if value in CONTACT_BULK_DELETE_REQUEST_ON_ERROR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_BULK_DELETE_REQUEST_ON_ERROR_VALUES!r}")
