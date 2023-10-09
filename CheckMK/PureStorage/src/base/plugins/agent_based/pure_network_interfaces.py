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

def parse_pure_network_interfaces(string_table):
    section = {}
    for row in string_table:
        (item, address, netmask, gateway, enabled, mtu, speed, hwaddr)  = row


        try:
            address=address
        except ValueError:
            address=0
        try:
            netmask=int(netmask)
        except ValueError:
            netmask=0
        try:
            gateway=gateway
        except ValueError:
            gateway=0
        try:
            enabled=int(enabled)
        except ValueError:
            enabled = 0
        try:
            mtu=int(mtu)
        except ValueError:
            mtu=0
        try:
            speed=int(speed)
        except ValueError:
            speed=0
        try:
            hwaddr=int(hwaddr)
        except ValueError:
            hwaddr=0

        section[item] = {
            'address': address,
            'netmask': netmask,
            'gateway': gateway,
            'enabled': enabled,
            'mtu': mtu,
            'speed': speed,
            'hwaddr': hwaddr,
        }
    return section

register.agent_section(
    name="pure_network_interfaces",
    parse_function=parse_pure_network_interfaces,
)

def discovery_pure_network_interfaces(section):
    for item in section.keys():
        yield Service(item=item)

def check_pure_network_interfaces(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    address=data['address']
    netmask=data['netmask']
    gateway=data['gateway']
    enabled=data['enabled']
    mtu=data['mtu']
    speed:int=data['speed']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"IP Address: {address} Subnet: {netmask} Gateway: {gateway}",
            details = f"MTU Value: {mtu}\n \
            Speed: {speed}",
            )
# Metrics
    else:
        yield Result(
            state=State.CRIT,
            summary=f"IP Address: {address} Subnet: {netmask} Gateway: {gateway}",
            details = f"MTU Value: {mtu}\n \
            Speed: {speed}",
            )

register.check_plugin(
    name="pure_network_interfaces",
    service_name="NIC %s",
    discovery_function=discovery_pure_network_interfaces,
    check_function=check_pure_network_interfaces,
)
