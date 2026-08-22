from typing import Literal

StatusPageTemplateWriteRequestDefaultImpact = Literal["major", "minor"]

STATUS_PAGE_TEMPLATE_WRITE_REQUEST_DEFAULT_IMPACT_VALUES: set[StatusPageTemplateWriteRequestDefaultImpact] = {
    "major",
    "minor",
}


def check_status_page_template_write_request_default_impact(value: str) -> StatusPageTemplateWriteRequestDefaultImpact:
    if value in STATUS_PAGE_TEMPLATE_WRITE_REQUEST_DEFAULT_IMPACT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEMPLATE_WRITE_REQUEST_DEFAULT_IMPACT_VALUES!r}"
    )
