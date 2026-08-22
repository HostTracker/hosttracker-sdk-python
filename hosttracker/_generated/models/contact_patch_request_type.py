from typing import Literal

ContactPatchRequestType = Literal["email", "http", "sms", "voiceCall", "webPush"]

CONTACT_PATCH_REQUEST_TYPE_VALUES: set[ContactPatchRequestType] = {
    "email",
    "http",
    "sms",
    "voiceCall",
    "webPush",
}


def check_contact_patch_request_type(value: str) -> ContactPatchRequestType:
    if value in CONTACT_PATCH_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_PATCH_REQUEST_TYPE_VALUES!r}")
