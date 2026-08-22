from typing import Literal

SNMPCheckSettingsSecurityLevel = Literal["authNoPriv", "authPriv", "noAuthNoPriv"]

SNMP_CHECK_SETTINGS_SECURITY_LEVEL_VALUES: set[SNMPCheckSettingsSecurityLevel] = {
    "authNoPriv",
    "authPriv",
    "noAuthNoPriv",
}


def check_snmp_check_settings_security_level(value: str) -> SNMPCheckSettingsSecurityLevel:
    if value in SNMP_CHECK_SETTINGS_SECURITY_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SNMP_CHECK_SETTINGS_SECURITY_LEVEL_VALUES!r}")
