from typing import Literal

CronPreviewViewReason = Literal["neverFires", "notEntitled", "tooFrequent", "unparseable"]

CRON_PREVIEW_VIEW_REASON_VALUES: set[CronPreviewViewReason] = {
    "neverFires",
    "notEntitled",
    "tooFrequent",
    "unparseable",
}


def check_cron_preview_view_reason(value: str) -> CronPreviewViewReason:
    if value in CRON_PREVIEW_VIEW_REASON_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CRON_PREVIEW_VIEW_REASON_VALUES!r}")
