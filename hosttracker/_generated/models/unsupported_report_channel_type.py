from typing import Literal

UnsupportedReportChannelType = Literal["https://api2.host-tracker.com/problems/unsupported-report-channel"]

UNSUPPORTED_REPORT_CHANNEL_TYPE_VALUES: set[UnsupportedReportChannelType] = {
    "https://api2.host-tracker.com/problems/unsupported-report-channel",
}


def check_unsupported_report_channel_type(value: str) -> UnsupportedReportChannelType:
    if value in UNSUPPORTED_REPORT_CHANNEL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNSUPPORTED_REPORT_CHANNEL_TYPE_VALUES!r}")
