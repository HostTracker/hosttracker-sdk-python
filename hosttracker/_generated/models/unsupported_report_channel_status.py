from typing import Literal

UnsupportedReportChannelStatus = Literal[422]

UNSUPPORTED_REPORT_CHANNEL_STATUS_VALUES: set[UnsupportedReportChannelStatus] = {
    422,
}


def check_unsupported_report_channel_status(value: int) -> UnsupportedReportChannelStatus:
    if value in UNSUPPORTED_REPORT_CHANNEL_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNSUPPORTED_REPORT_CHANNEL_STATUS_VALUES!r}")
