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

def parse_pfsense_gateway(string_table):
    section = {}
    for row in string_table:
        (item, monitorip, srcip, delay, stddev, loss, status)  = row

        try:
            monitorip=monitorip
        except ValueError:
            monitorip=0
        try:
            srcip=srcip
        except ValueError:
            srcip=0
        try:
            delay=int(delay)
        except ValueError:
            delay = 0
        try:
            stddev=int(stddev)
        except ValueError:
            stddev = 0
        try:
            loss=int(loss)
        except ValueError:
            loss=0
        try:
            status=status
        except ValueError:
            status=0

        section[item] = {
            'monitorip': monitorip,
            'srcip': srcip,
            'delay': delay,
            'stddev': stddev,
            'loss': loss,
            'status': status,
        }
    return section

register.agent_section(
    name="pfsense_gateway",
    parse_function=parse_pfsense_gateway,
)

def discovery_pfsense_gateway(section):
    for item in section.keys():
        yield Service(item=item)

def check_pfsense_gateway(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    monitorip:str=data['monitorip']
    srcip:str=data['srcip']
    delay:int=data['delay']
    stddev:int=data['stddev']
    loss:int=data['loss']
    status:str=data['status']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"status: {status},monitorip: {monitorip}, source ip: {srcip}",
            details = f"delay: {delay} \n \
            stddev: {stddev}\n \
            Lost packets: {loss}",
        )
# Metrics
        yield Metric("loss", int(loss))
        yield Metric("outerrs", int(delay))
        yield Metric("inbytespass", int(stddev))

    else:
        yield Result(
            state=State.CRIT,
            summary=f"status: {status},monitorip: {monitorip}, source ip: {srcip}",
            details = f"delay: {delay} \n \
            stddev: {stddev}\n \
            Lost packets: {loss}",
        )
# Metrics
        yield Metric("loss", int(loss))
        yield Metric("outerrs", int(delay))
        yield Metric("inbytespass", int(stddev))


register.check_plugin(
    name="pfsense_gateway",
    service_name="Gateway %s",
    discovery_function=discovery_pfsense_gateway,
    check_function=check_pfsense_gateway,
)
