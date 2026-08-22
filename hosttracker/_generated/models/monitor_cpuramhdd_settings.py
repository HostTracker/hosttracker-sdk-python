from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_cpuramhdd_settings_counter_type import (
    MonitorCPURAMHDDSettingsCounterType,
    check_monitor_cpuramhdd_settings_counter_type,
)
from ..models.monitor_cpuramhdd_settings_deployment_type import (
    MonitorCPURAMHDDSettingsDeploymentType,
    check_monitor_cpuramhdd_settings_deployment_type,
)
from ..models.monitor_cpuramhdd_settings_error_condition import (
    MonitorCPURAMHDDSettingsErrorCondition,
    check_monitor_cpuramhdd_settings_error_condition,
)
from ..models.monitor_cpuramhdd_settings_monitor_type import (
    MonitorCPURAMHDDSettingsMonitorType,
    check_monitor_cpuramhdd_settings_monitor_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorCPURAMHDDSettings")


@_attrs_define
class MonitorCPURAMHDDSettings:
    """POSTs a probe to a customer-hosted endpoint, reads back ONE numeric server metric - CPU, RAM, disk, a TCP or DB
    connect time, or a Windows performance counter - and evaluates a threshold condition against it. It always runs from
    a fixed internal check network rather than the public agent fleet, so there is no location to choose -
    `locations.pools` is refused if sent; omit `locations` entirely when creating this type.

    """

    monitor_type: MonitorCPURAMHDDSettingsMonitorType | Unset = "custom"
    """ Which probe endpoint the check dials. """
    counter_type: MonitorCPURAMHDDSettingsCounterType | Unset = "cpu"
    """ Which metric the probe reports. Windows-only metrics are refused on a php monitorType; a `custom`
    monitorType skips the whole block and stores an empty value. """
    probe_url: str | Unset = UNSET
    """ The endpoint the probe is POSTed to. This is the DIALED target and is a separate, never-substituted field
    from the monitor's own `url`, which is the display identity composed from the counter configuration. """
    host: str | Unset = UNSET
    """ Host the probe connects to for a port counter. Required when counterType is port. """
    port: int | Unset = 80
    """ Port the probe connects to for a port counter. """
    label: str | Unset = UNSET
    """ Disk path or drive label for a disk counter. Required when counterType is disk. """
    connection_string: str | Unset = UNSET
    """ Connection string the probe dials for a database counter. Parsed for validity by the matching provider
    builder. It embeds credentials, so it is handled as one - the visibility rule the schema appends applies.
    Required when counterType is mssql or mysql. Credential. Read visibility is tiered: the monitor's owner and a
    subaccount holding the task-edit right receive the stored value; a view-only subaccount receives the { set,
    updatedAt } sentinel instead. On write, an absent field means unchanged, null clears it, and the read sentinel
    is never accepted as a literal value. """
    category: str | Unset = UNSET
    """ Windows performance-counter category. Required when counterType is perfCounter. """
    name: str | Unset = UNSET
    """ Windows performance-counter name. Required when counterType is perfCounter. """
    instance: str | Unset = ""
    """ Windows performance-counter instance. """
    deployment_type: MonitorCPURAMHDDSettingsDeploymentType | Unset = "manual"
    """ How the probe endpoint was deployed. `manual` is the only value the validator accepts today. """
    error_level_1: float | Unset = UNSET
    """ First threshold bound. For a two-level condition it must not exceed `errorLevel2`. Required when
    errorCondition is a one- or two-level condition. """
    error_level_2: float | Unset = UNSET
    """ Second threshold bound. Required when errorCondition is a two-level condition. """
    error_condition: MonitorCPURAMHDDSettingsErrorCondition | Unset = UNSET
    """ The threshold predicate applied to the reported value. Stored lower-cased. """
    error_check_count: int | Unset = UNSET
    """ How many consecutive overloaded readings make the monitor go down. Evaluated by CORE, not by the agent. """

    def to_dict(self) -> dict[str, Any]:
        monitor_type: str | Unset = UNSET
        if not isinstance(self.monitor_type, Unset):
            monitor_type = self.monitor_type

        counter_type: str | Unset = UNSET
        if not isinstance(self.counter_type, Unset):
            counter_type = self.counter_type

        probe_url = self.probe_url

        host = self.host

        port = self.port

        label = self.label

        connection_string = self.connection_string

        category = self.category

        name = self.name

        instance = self.instance

        deployment_type: str | Unset = UNSET
        if not isinstance(self.deployment_type, Unset):
            deployment_type = self.deployment_type

        error_level_1 = self.error_level_1

        error_level_2 = self.error_level_2

        error_condition: str | Unset = UNSET
        if not isinstance(self.error_condition, Unset):
            error_condition = self.error_condition

        error_check_count = self.error_check_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if monitor_type is not UNSET:
            field_dict["monitorType"] = monitor_type
        if counter_type is not UNSET:
            field_dict["counterType"] = counter_type
        if probe_url is not UNSET:
            field_dict["probeUrl"] = probe_url
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if label is not UNSET:
            field_dict["label"] = label
        if connection_string is not UNSET:
            field_dict["connectionString"] = connection_string
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if instance is not UNSET:
            field_dict["instance"] = instance
        if deployment_type is not UNSET:
            field_dict["deploymentType"] = deployment_type
        if error_level_1 is not UNSET:
            field_dict["errorLevel1"] = error_level_1
        if error_level_2 is not UNSET:
            field_dict["errorLevel2"] = error_level_2
        if error_condition is not UNSET:
            field_dict["errorCondition"] = error_condition
        if error_check_count is not UNSET:
            field_dict["errorCheckCount"] = error_check_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _monitor_type = d.pop("monitorType", UNSET)
        monitor_type: MonitorCPURAMHDDSettingsMonitorType | Unset
        if isinstance(_monitor_type, Unset):
            monitor_type = UNSET
        else:
            monitor_type = check_monitor_cpuramhdd_settings_monitor_type(_monitor_type)

        _counter_type = d.pop("counterType", UNSET)
        counter_type: MonitorCPURAMHDDSettingsCounterType | Unset
        if isinstance(_counter_type, Unset):
            counter_type = UNSET
        else:
            counter_type = check_monitor_cpuramhdd_settings_counter_type(_counter_type)

        probe_url = d.pop("probeUrl", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        label = d.pop("label", UNSET)

        connection_string = d.pop("connectionString", UNSET)

        category = d.pop("category", UNSET)

        name = d.pop("name", UNSET)

        instance = d.pop("instance", UNSET)

        _deployment_type = d.pop("deploymentType", UNSET)
        deployment_type: MonitorCPURAMHDDSettingsDeploymentType | Unset
        if isinstance(_deployment_type, Unset):
            deployment_type = UNSET
        else:
            deployment_type = check_monitor_cpuramhdd_settings_deployment_type(_deployment_type)

        error_level_1 = d.pop("errorLevel1", UNSET)

        error_level_2 = d.pop("errorLevel2", UNSET)

        _error_condition = d.pop("errorCondition", UNSET)
        error_condition: MonitorCPURAMHDDSettingsErrorCondition | Unset
        if isinstance(_error_condition, Unset):
            error_condition = UNSET
        else:
            error_condition = check_monitor_cpuramhdd_settings_error_condition(_error_condition)

        error_check_count = d.pop("errorCheckCount", UNSET)

        monitor_cpuramhdd_settings = cls(
            monitor_type=monitor_type,
            counter_type=counter_type,
            probe_url=probe_url,
            host=host,
            port=port,
            label=label,
            connection_string=connection_string,
            category=category,
            name=name,
            instance=instance,
            deployment_type=deployment_type,
            error_level_1=error_level_1,
            error_level_2=error_level_2,
            error_condition=error_condition,
            error_check_count=error_check_count,
        )

        return monitor_cpuramhdd_settings
