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

def parse_pure_host_connections(string_table):
    section = {}
    for row in string_table:
        (item, vol, name)  = row


        try:
            vol=str(vol)
        except ValueError:
            vol=0
        try:
            name=str(name)
        except ValueError:
            name=0

        section[item] = {
            'vol': vol,
            'name': name,
        }
    return section

register.agent_section(
    name="pure_host_connections",
    parse_function=parse_pure_host_connections,
)

def discovery_pure_host_connections(section):
    for item in section.keys():
        yield Service(item=item)

def check_pure_host_connections(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    vol=data['vol']
    name=data['name']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"Connected host: {name}",
            details=f"Connected volume: {vol}",
            )
# Metrics
    else:
        yield Result(
            state=State.CRIT,
            summary=f"Connected host: {name}",
            details=f"Connected volume: {vol}",
            )


register.check_plugin(
    name="pure_host_connections",
    service_name="Host Group %s",
    discovery_function=discovery_pure_host_connections,
    check_function=check_pure_host_connections,
)
