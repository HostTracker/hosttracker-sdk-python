from typing import Literal

ReportGenerateRequestFormat = Literal["csv", "html", "pdf", "xml"]

REPORT_GENERATE_REQUEST_FORMAT_VALUES: set[ReportGenerateRequestFormat] = {
    "csv",
    "html",
    "pdf",
    "xml",
}


def check_report_generate_request_format(value: str) -> ReportGenerateRequestFormat:
    if value in REPORT_GENERATE_REQUEST_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_GENERATE_REQUEST_FORMAT_VALUES!r}")
