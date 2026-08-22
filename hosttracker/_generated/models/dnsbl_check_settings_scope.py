from typing import Literal

DNSBLCheckSettingsScope = Literal["allWebIps", "firstWebIp", "webAndMx"]

DNSBL_CHECK_SETTINGS_SCOPE_VALUES: set[DNSBLCheckSettingsScope] = {
    "allWebIps",
    "firstWebIp",
    "webAndMx",
}


def check_dnsbl_check_settings_scope(value: str) -> DNSBLCheckSettingsScope:
    if value in DNSBL_CHECK_SETTINGS_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DNSBL_CHECK_SETTINGS_SCOPE_VALUES!r}")
