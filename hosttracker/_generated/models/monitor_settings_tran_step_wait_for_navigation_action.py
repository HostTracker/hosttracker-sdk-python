from typing import Literal

MonitorSettingsTranStepWaitForNavigationAction = Literal["waitForNavigation"]

MONITOR_SETTINGS_TRAN_STEP_WAIT_FOR_NAVIGATION_ACTION_VALUES: set[MonitorSettingsTranStepWaitForNavigationAction] = {
    "waitForNavigation",
}


def check_monitor_settings_tran_step_wait_for_navigation_action(
    value: str,
) -> MonitorSettingsTranStepWaitForNavigationAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_WAIT_FOR_NAVIGATION_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_WAIT_FOR_NAVIGATION_ACTION_VALUES!r}"
    )
