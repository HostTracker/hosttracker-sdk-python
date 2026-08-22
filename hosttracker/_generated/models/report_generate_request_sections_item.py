from typing import Literal

ReportGenerateRequestSectionsItem = Literal["incidents", "log", "outages", "state", "stats"]

REPORT_GENERATE_REQUEST_SECTIONS_ITEM_VALUES: set[ReportGenerateRequestSectionsItem] = {
    "incidents",
    "log",
    "outages",
    "state",
    "stats",
}


def check_report_generate_request_sections_item(value: str) -> ReportGenerateRequestSectionsItem:
    if value in REPORT_GENERATE_REQUEST_SECTIONS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_GENERATE_REQUEST_SECTIONS_ITEM_VALUES!r}")
