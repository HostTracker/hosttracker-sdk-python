from typing import Literal

UnsupportedMediaTypeCode = Literal["unsupported_media_type"]

UNSUPPORTED_MEDIA_TYPE_CODE_VALUES: set[UnsupportedMediaTypeCode] = {
    "unsupported_media_type",
}


def check_unsupported_media_type_code(value: str) -> UnsupportedMediaTypeCode:
    if value in UNSUPPORTED_MEDIA_TYPE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNSUPPORTED_MEDIA_TYPE_CODE_VALUES!r}")
