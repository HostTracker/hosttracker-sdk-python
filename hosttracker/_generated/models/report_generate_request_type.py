from typing import Literal

ReportGenerateRequestType = Literal["uptime"]

REPORT_GENERATE_REQUEST_TYPE_VALUES: set[ReportGenerateRequestType] = {
    "uptime",
}


def check_report_generate_request_type(value: str) -> ReportGenerateRequestType:
    if value in REPORT_GENERATE_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_GENERATE_REQUEST_TYPE_VALUES!r}")
