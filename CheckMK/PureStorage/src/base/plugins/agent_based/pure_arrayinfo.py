
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

def parse_pure_arrayinfo(string_table):

    section = {}
    for row in string_table:
        (item, parity, provisioned, system, snapshots, volumes, data_reduction, capacity, total)  = row


        try:
            parity=parity
        except ValueError:
            parity=0
        try:
            provisioned=provisioned
        except ValueError:
            provisioned=0
        try:
            system=int(system)
        except ValueError:
            system=0
        try:
            snapshots=snapshots
        except ValueError:
            snapshots=0
        try:
            volumes=int(volumes)
        except ValueError:
            volumes=0
        try:
            data_reduction=data_reduction
        except ValueError:
            data_reduction=0
        try:
            capacity=int(capacity)
        except ValueError:
            capacity=0
        try:
            total=int(total)
        except ValueError:
            total=0

        section[item] = {
            'parity': parity,
            'provisioned': provisioned,
            'system': system,
            'snapshots': snapshots,
            'volumes': volumes,
            'data_reduction': data_reduction,
            'capacity': capacity,
            'total': total,
        }
    return section

register.agent_section(
    name="pure_arrayinfo",
    parse_function=parse_pure_arrayinfo,
)

def discovery_pure_arrayinfo(section):
    for item in section.keys():
        yield Service(item=item)

def check_pure_arrayinfo(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    fs_parity:int=data['parity']
    fs_provisioning:int=data['provisioned']
    fs_system=data['system']
    fs_snapshots:int=data['snapshots']
    fs_volumes:int=data['volumes']
    fs_data_reduction=data['data_reduction']
    fs_capacity:int=data['capacity']
    fs_total:int=data['total']
    fs_shared = (int(data['volumes']) + int(data['snapshots']))
    fs_shared =  int(fs_shared) - int((data['total']))

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"Array capacity: {render.bytes(fs_capacity)}, Provisioned space: {render.bytes(fs_provisioning)}, Total used space: {render.bytes(fs_total)}",
            details = f"Array parity: {fs_parity} \n \
            Data Reduction: {fs_data_reduction} to 1 \n \
            Unique space used: {render.bytes(fs_volumes)} \n \
            Shared space: {render.bytes(fs_shared)} \n \
            Snapshots total size: {render.bytes(fs_snapshots)}",
            )
# Metrics
        yield Metric("pure_1_datareduction", float(data['data_reduction']))
        yield Metric("pure_4_snaphots", int(fs_snapshots))
    else:
        yield Result(
            state=State.CRIT,
            summary=f"Array capacity: {render.bytes(fs_capacity)}, Provisioned space: {render.bytes(fs_provisioning)}, Total used space: {render.bytes(fs_total)}",
            details = f"Array parity: {fs_parity} \n \
            Data Reduction: {fs_data_reduction} to 1 \n \
            Unique space used: {render.bytes(fs_volumes)} \n \
            Shared space: {render.bytes(fs_shared)} \n \
            Snapshots total size: {render.bytes(fs_snapshots)}",
            )

# Metrics
        yield Metric("pure_1_datareduction", float(data['data_reduction']))
        yield Metric("pure_4_snaphots", int(fs_snapshots))

register.check_plugin(
    name="pure_arrayinfo",
    service_name="Array storage %s",
    discovery_function=discovery_pure_arrayinfo,
    check_function=check_pure_arrayinfo,
)
