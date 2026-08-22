from typing import Literal

StatusPageTemplateViewDefaultImpact = Literal["major", "minor"]

STATUS_PAGE_TEMPLATE_VIEW_DEFAULT_IMPACT_VALUES: set[StatusPageTemplateViewDefaultImpact] = {
    "major",
    "minor",
}


def check_status_page_template_view_default_impact(value: str) -> StatusPageTemplateViewDefaultImpact:
    if value in STATUS_PAGE_TEMPLATE_VIEW_DEFAULT_IMPACT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_TEMPLATE_VIEW_DEFAULT_IMPACT_VALUES!r}")
