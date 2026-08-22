from typing import Literal

UnsupportedMediaTypeStatus = Literal[415]

UNSUPPORTED_MEDIA_TYPE_STATUS_VALUES: set[UnsupportedMediaTypeStatus] = {
    415,
}


def check_unsupported_media_type_status(value: int) -> UnsupportedMediaTypeStatus:
    if value in UNSUPPORTED_MEDIA_TYPE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNSUPPORTED_MEDIA_TYPE_STATUS_VALUES!r}")
