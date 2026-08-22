from typing import Literal

WebhookTestResultViewOutcome = Literal["delivered", "failed"]

WEBHOOK_TEST_RESULT_VIEW_OUTCOME_VALUES: set[WebhookTestResultViewOutcome] = {
    "delivered",
    "failed",
}


def check_webhook_test_result_view_outcome(value: str) -> WebhookTestResultViewOutcome:
    if value in WEBHOOK_TEST_RESULT_VIEW_OUTCOME_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_TEST_RESULT_VIEW_OUTCOME_VALUES!r}")
