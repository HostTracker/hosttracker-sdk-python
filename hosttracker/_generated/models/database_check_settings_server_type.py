from typing import Literal

DatabaseCheckSettingsServerType = Literal["firebird", "mssql", "mysql", "oracle", "postgresql"]

DATABASE_CHECK_SETTINGS_SERVER_TYPE_VALUES: set[DatabaseCheckSettingsServerType] = {
    "firebird",
    "mssql",
    "mysql",
    "oracle",
    "postgresql",
}


def check_database_check_settings_server_type(value: str) -> DatabaseCheckSettingsServerType:
    if value in DATABASE_CHECK_SETTINGS_SERVER_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATABASE_CHECK_SETTINGS_SERVER_TYPE_VALUES!r}")
