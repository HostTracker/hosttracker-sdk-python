from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_check_settings_comparison_mode import (
    DatabaseCheckSettingsComparisonMode,
    check_database_check_settings_comparison_mode,
)
from ..models.database_check_settings_mode import DatabaseCheckSettingsMode, check_database_check_settings_mode
from ..models.database_check_settings_server_type import (
    DatabaseCheckSettingsServerType,
    check_database_check_settings_server_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseCheckSettings")


@_attrs_define
class DatabaseCheckSettings:
    """Connects to a customer database, optionally runs a query, and compares the scalar it returns against a threshold -
    measuring connection, authentication and query performance. It always runs from a fixed internal check network
    rather than the public agent fleet, so there is no location to choose - `locations.pools` is refused if sent; omit
    `locations` entirely when creating this type.

    """

    server: str
    """ Host name or address. Must not contain any of `; , " : ' ( ) =` or a space - a colon in particular is
    refused with "don't put the port here"; give the port in `port`. """
    server_type: DatabaseCheckSettingsServerType | Unset = "mssql"
    """ Database engine. Decides the default port and the ADO.NET provider. """
    port: int | Unset = UNSET
    """ Port. Absent ⇒ the engine's default. """
    database: str | Unset = UNSET
    """ Database name. For Oracle it doubles as the instance name and must match ^[a-zA-Z][a-zA-Z0-9_]*$. """
    service: str | Unset = UNSET
    """ Oracle service name; same identifier rule as `database`. """
    login: str | Unset = UNSET
    """ User name. """
    password: str | Unset = UNSET
    """ Password. Credential. Read visibility is tiered: the monitor's owner and a subaccount holding the task-edit
    right receive the stored value; a view-only subaccount receives the { set, updatedAt } sentinel instead. On
    write, an absent field means unchanged, null clears it, and the read sentinel is never accepted as a literal
    value. """
    query: str | Unset = UNSET
    """ SQL to execute after connecting. """
    mode: DatabaseCheckSettingsMode | Unset = UNSET
    """ How the query's result is taken. """
    comparison_mode: DatabaseCheckSettingsComparisonMode | Unset = UNSET
    """ The predicate applied to the measured value. """
    value1: float | Unset = UNSET
    """ First comparison operand. Required when comparisonMode is not No. """
    value2: float | Unset = UNSET
    """ Second comparison operand. Required when comparisonMode is InInterval or OutInterval. """
    include_value_1: bool | Unset = False
    """ Make the lower interval bound inclusive. """
    include_value_2: bool | Unset = False
    """ Make the upper interval bound inclusive. """
    retrying: bool | Unset = False
    """ Retry the CONNECTION once before failing. """
    retrying_cmd: bool | Unset = False
    """ Retry the QUERY once before failing. """

    def to_dict(self) -> dict[str, Any]:
        server = self.server

        server_type: str | Unset = UNSET
        if not isinstance(self.server_type, Unset):
            server_type = self.server_type

        port = self.port

        database = self.database

        service = self.service

        login = self.login

        password = self.password

        query = self.query

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        comparison_mode: str | Unset = UNSET
        if not isinstance(self.comparison_mode, Unset):
            comparison_mode = self.comparison_mode

        value1 = self.value1

        value2 = self.value2

        include_value_1 = self.include_value_1

        include_value_2 = self.include_value_2

        retrying = self.retrying

        retrying_cmd = self.retrying_cmd

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server": server,
            }
        )
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if port is not UNSET:
            field_dict["port"] = port
        if database is not UNSET:
            field_dict["database"] = database
        if service is not UNSET:
            field_dict["service"] = service
        if login is not UNSET:
            field_dict["login"] = login
        if password is not UNSET:
            field_dict["password"] = password
        if query is not UNSET:
            field_dict["query"] = query
        if mode is not UNSET:
            field_dict["mode"] = mode
        if comparison_mode is not UNSET:
            field_dict["comparisonMode"] = comparison_mode
        if value1 is not UNSET:
            field_dict["value1"] = value1
        if value2 is not UNSET:
            field_dict["value2"] = value2
        if include_value_1 is not UNSET:
            field_dict["includeValue1"] = include_value_1
        if include_value_2 is not UNSET:
            field_dict["includeValue2"] = include_value_2
        if retrying is not UNSET:
            field_dict["retrying"] = retrying
        if retrying_cmd is not UNSET:
            field_dict["retryingCmd"] = retrying_cmd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = d.pop("server")

        _server_type = d.pop("serverType", UNSET)
        server_type: DatabaseCheckSettingsServerType | Unset
        if isinstance(_server_type, Unset):
            server_type = UNSET
        else:
            server_type = check_database_check_settings_server_type(_server_type)

        port = d.pop("port", UNSET)

        database = d.pop("database", UNSET)

        service = d.pop("service", UNSET)

        login = d.pop("login", UNSET)

        password = d.pop("password", UNSET)

        query = d.pop("query", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: DatabaseCheckSettingsMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_database_check_settings_mode(_mode)

        _comparison_mode = d.pop("comparisonMode", UNSET)
        comparison_mode: DatabaseCheckSettingsComparisonMode | Unset
        if isinstance(_comparison_mode, Unset):
            comparison_mode = UNSET
        else:
            comparison_mode = check_database_check_settings_comparison_mode(_comparison_mode)

        value1 = d.pop("value1", UNSET)

        value2 = d.pop("value2", UNSET)

        include_value_1 = d.pop("includeValue1", UNSET)

        include_value_2 = d.pop("includeValue2", UNSET)

        retrying = d.pop("retrying", UNSET)

        retrying_cmd = d.pop("retryingCmd", UNSET)

        database_check_settings = cls(
            server=server,
            server_type=server_type,
            port=port,
            database=database,
            service=service,
            login=login,
            password=password,
            query=query,
            mode=mode,
            comparison_mode=comparison_mode,
            value1=value1,
            value2=value2,
            include_value_1=include_value_1,
            include_value_2=include_value_2,
            retrying=retrying,
            retrying_cmd=retrying_cmd,
        )

        return database_check_settings
