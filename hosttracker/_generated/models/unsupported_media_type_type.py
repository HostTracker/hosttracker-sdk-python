from typing import Literal

UnsupportedMediaTypeType = Literal["https://api2.host-tracker.com/problems/unsupported-media-type"]

UNSUPPORTED_MEDIA_TYPE_TYPE_VALUES: set[UnsupportedMediaTypeType] = {
    "https://api2.host-tracker.com/problems/unsupported-media-type",
}


def check_unsupported_media_type_type(value: str) -> UnsupportedMediaTypeType:
    if value in UNSUPPORTED_MEDIA_TYPE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNSUPPORTED_MEDIA_TYPE_TYPE_VALUES!r}")
