#2023 created by Carlo Kleinloog
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based
import time
import json
from cmk.base.check_api import get_bytes_human_readable, get_percent_human_readable
from .agent_based_api.v1 import (
    register,
    Service,
    Result,
    State,
    Metric,
    render,
)

def parse_citrix_host(string_table):
    section = {}
    for row in string_table:
        (item, software_brand, software_version, address, memory_overhead, memory_total)  = row

        try:
            software_brand:int=software_brand
        except ValueError:
            software_brand=0
        try:
            software_version:str=software_version
        except ValueError:
            software_version=0
        try:
            address:int=address
        except ValueError:
            address=0
        try:
            memory_overhead:int=memory_overhead
        except ValueError:
            memory_overhead=0
        try:
            memory_total:int=memory_total
        except ValueError:
            memory_total=0

        section[item] = {
'software_brand' : software_brand,
'software_version' : software_version,
'address' : address,
'memory_overhead' : memory_overhead,
'memory_total' : memory_total,
        }
    return section

register.agent_section(
    name="citrix_host",
    parse_function=parse_citrix_host,
)

def discovery_citrix_host(section):
    for item in section.keys():
        yield Service(item=item)

def check_citrix_host(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    software_brand:int = data['software_brand']
    software_version:str = data['software_version']
    address:str = data['address']
    memory_overhead:int = data['memory_overhead']
    memory_total:int = data['memory_total']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"Software: {(software_brand)}, Version: {(software_version)}",
            details = f"IP Address: {(address)}, Memory Total: {(memory_total)}, Memory Overhead: {(memory_overhead)}",
            )
# Metrics
        yield Metric("citrix_memory_total", int(memory_total))
        yield Metric("citrix_memory_overhead", int(memory_overhead))
    else:
        yield Result(
            state=State.CRIT,
            summary=f"Software: {(software_brand)}, Version: {(software_version)}",
            details = f"IP Address: {(address)}, Memory Total: {(memory_total)}, Memory Overhead: {(memory_overhead)}",
            )

# Metrics
        yield Metric("citrix_memory_total", int(memory_total))
        yield Metric("citrix_memory_overhead", int(memory_overhead))

register.check_plugin(
    name="citrix_host",
    service_name="Citrix host %s",
    discovery_function=discovery_citrix_host,
    check_function=check_citrix_host,
)
