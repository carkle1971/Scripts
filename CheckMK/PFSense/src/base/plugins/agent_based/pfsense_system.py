#2023 created by Carlo Kleinloog
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based
from cmk.base.check_api import get_bytes_human_readable, get_percent_human_readable
from .agent_based_api.v1 import (
    register,
    Service,
    Result,
    State,
    Metric,
    render,
)

def parse_pfsense_system(string_table):
    section = {}
    for row in string_table:
        (item, system_platform, bios_vendor, bios_version, loss, cpu_model, kernel_pti, cpu_count, mbuf_usage, mem_usage, swap_usage, disk_usage)  = row

        try:
            system_platform=system_platform
        except ValueError:
            system_platform=0
        try:
            bios_vendor=int(bios_vendor)
        except ValueError:
            bios_vendor = 0
        try:
            bios_version=int(bios_version)
        except ValueError:
            bios_version = 0
        try:
            loss=int(loss)
        except ValueError:
            loss=0
        try:
            cpu_model=cpu_model
        except ValueError:
            cpu_model=0
        try:
            kernel_pti=kernel_pti
        except ValueError:
            kernel_pti=0
        try:
            cpu_count=cpu_count
        except ValueError:
            cpu_count=0
        try:
            mbuf_usage=int(mbuf_usage)
        except ValueError:
            mbuf_usage = 0
        try:
            mem_usage=int(mem_usage)
        except ValueError:
            mem_usage = 0
        try:
            swap_usage=int(swap_usage)
        except ValueError:
            swap_usage=0
        try:
            disk_usage=disk_usage
        except ValueError:
            disk_usage=0

        section[item] = {
            'system_platform': system_platform,
            'bios_vendor': bios_vendor,
            'bios_version': bios_version,
            'cpu_model': cpu_model,
            'kernel_pti': kernel_pti,
            'cpu_count': cpu_count,
            'mbuf_usage': mbuf_usage,
            'mem_usage': mem_usage,
            'swap_usage': swap_usage,
            'disk_usage': disk_usage,
        }
    return section

register.agent_section(
    name="pfsense_system",
    parse_function=parse_pfsense_system,
)

def discovery_pfsense_system(section):
    for item in section.keys():
        yield Service(item=item)

def check_pfsense_system(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    system_platform:str=data['system_platform']
    bios_vendor:str=data['bios_vendor']
    bios_version:int=data['bios_version']
    cpu_model:str=data['cpu_model']
    kernel_pti:str=data['kernel_pti']
    cpu_count:str=data['cpu_count']
    mbuf_usage:int=data['mbuf_usage']
    mem_usage:int=data['mem_usage']
    swap_usage:int=data['swap_usage']
    disk_usage:int=data['disk_usage']
    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"system_platform: {system_platform}, cpu_model: {cpu_model}, Bios: {bios_vendor}, Bios version: {bios_version}",
            details = f"Kernel PTI: {kernel_pti} \n \
            bios_vendor: {cpu_count}\n \
            bios_vendor: {mbuf_usage}\n \
            bios_vendor: {mem_usage}\n \
            bios_vendor: {swap_usage}\n \
            Lost packets: {disk_usage}",
        )
# Metrics
        yield Metric("mbuf_usage", int(mbuf_usage))
        yield Metric("mem_usage", int(mem_usage))
        yield Metric("swap_usage", int(swap_usage))
        yield Metric("disk_usage", int(disk_usage))

    else:
        yield Result(
            state=State.CRIT,
            summary=f"system_platform: {system_platform}, cpu_model: {cpu_model}, Bios: {bios_vendor}, Bios version: {bios_version}",
            details = f"Kernel PTI: {kernel_pti} \n \
            bios_vendor: {cpu_count}\n \
            bios_vendor: {mbuf_usage}\n \
            bios_vendor: {mem_usage}\n \
            bios_vendor: {swap_usage}\n \
            Lost packets: {disk_usage}",
        )
# Metrics
        yield Metric("mbuf_usage", int(mbuf_usage))
        yield Metric("mem_usage", int(mem_usage))
        yield Metric("swap_usage", int(swap_usage))
        yield Metric("disk_usage", int(disk_usage))


register.check_plugin(
    name="pfsense_system",
    service_name="system ID %s",
    discovery_function=discovery_pfsense_system,
    check_function=check_pfsense_system,
)
