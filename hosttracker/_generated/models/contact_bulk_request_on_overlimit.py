from typing import Literal

ContactBulkRequestOnOverlimit = Literal["disable", "fail", "stop"]

CONTACT_BULK_REQUEST_ON_OVERLIMIT_VALUES: set[ContactBulkRequestOnOverlimit] = {
    "disable",
    "fail",
    "stop",
}


def check_contact_bulk_request_on_overlimit(value: str) -> ContactBulkRequestOnOverlimit:
    if value in CONTACT_BULK_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_BULK_REQUEST_ON_OVERLIMIT_VALUES!r}")
