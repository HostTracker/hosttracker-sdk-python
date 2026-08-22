from typing import Literal

ContactWriteRequestType = Literal["email", "http", "sms", "voiceCall", "webPush"]

CONTACT_WRITE_REQUEST_TYPE_VALUES: set[ContactWriteRequestType] = {
    "email",
    "http",
    "sms",
    "voiceCall",
    "webPush",
}


def check_contact_write_request_type(value: str) -> ContactWriteRequestType:
    if value in CONTACT_WRITE_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_WRITE_REQUEST_TYPE_VALUES!r}")
