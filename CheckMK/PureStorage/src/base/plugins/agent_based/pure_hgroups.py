#2023 created by Carlo Kleinloog
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based
from cmk.base.check_api import get_bytes_human_readable, get_percent_human_readable
from .agent_based_api.v1 import (
    register,
    Service,
    Result,
    State,
    Metric,
    render
)

def parse_pure_hgroups(string_table):
    section = {}
    for row in string_table:
        (item, hosts)  = row


        try:
            hosts=str(hosts)
        except ValueError:
            hosts=0

        section[item] = {
            'hosts': hosts,
        }
    return section

register.agent_section(
    name="pure_hgroups",
    parse_function=parse_pure_hgroups,
)

def discovery_pure_hgroups(section):
    for item in section.keys():
        yield Service(item=item)

def check_pure_hgroups(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    hosts=data['hosts']


    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"Connected hosts: {hosts}",
            )
# Metrics
    else:
        yield Result(
            state=State.CRIT,
            summary=f"Connected hosts: {hosts}",
            )

register.check_plugin(
    name="pure_hgroups",
    service_name="Host Group %s",
    discovery_function=discovery_pure_hgroups,
    check_function=check_pure_hgroups,
)
