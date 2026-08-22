from typing import Literal

UnsupportedReportChannelCode = Literal["unsupported_report_channel"]

UNSUPPORTED_REPORT_CHANNEL_CODE_VALUES: set[UnsupportedReportChannelCode] = {
    "unsupported_report_channel",
}


def check_unsupported_report_channel_code(value: str) -> UnsupportedReportChannelCode:
    if value in UNSUPPORTED_REPORT_CHANNEL_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNSUPPORTED_REPORT_CHANNEL_CODE_VALUES!r}")
