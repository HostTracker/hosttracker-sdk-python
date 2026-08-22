from typing import Literal

SNMPCheckSettingsVerb = Literal["Get", "GetNext"]

SNMP_CHECK_SETTINGS_VERB_VALUES: set[SNMPCheckSettingsVerb] = {
    "Get",
    "GetNext",
}


def check_snmp_check_settings_verb(value: str) -> SNMPCheckSettingsVerb:
    if value in SNMP_CHECK_SETTINGS_VERB_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SNMP_CHECK_SETTINGS_VERB_VALUES!r}")
