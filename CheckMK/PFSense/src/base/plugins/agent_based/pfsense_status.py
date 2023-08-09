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

def parse_pfsense_openvpn(string_table):
    section = {}
    for row in string_table:
        (item, remote_host, virtual_addr, bytes_recv, bytes_sent, connect_time, client_id, cipher)  = row


        try:
            remote_host=remote_host
        except ValueError:
            remote_host=0
        try:
            virtual_addr=virtual_addr
        except ValueError:
            virtual_addr=0
        try:
            bytes_recv=int(bytes_recv)
        except ValueError:
            bytes_recv=0
        try:
            bytes_sent=int(bytes_sent)
        except ValueError:
            bytes_sent=0            
        try:
            connect_time=connect_time
        except ValueError:
            connect_time=0
        try:
            client_id=client_id
        except ValueError:
            client_id = 0
        try:
            cipher=cipher
        except ValueError:
            cipher=0

        section[item] = {
            'remote_host': remote_host,
            'virtual_addr': virtual_addr,
            'bytes_recv': bytes_recv,
            'bytes_sent': bytes_sent,
            'connect_time': connect_time,
            'client_id': client_id,
            'cipher': cipher,
        }
    return section

register.agent_section(
    name="pfsense_openvpn",
    parse_function=parse_pfsense_openvpn,
)

def discovery_pfsense_openvpn(section):
    for item in section.keys():
        yield Service(item=item)

def check_pfsense_openvpn(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    remote_host=data['remote_host']
    virtual_addr=data['virtual_addr']
    bytes_recv:int=data['bytes_recv']
    bytes_sent:int=data['bytes_sent']
    connect_time=data['connect_time']
    client_id=data['client_id']
    cipher=data['cipher']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"Bytes received: {get_bytes_human_readable(bytes_recv)}, Bytes Sent: {render.bytes(bytes_sent)}",
            details = f"Remote Host: {remote_host} \n \
            Virtual Address: {virtual_addr} \n \
            Connection time: {connect_time} \n \
            Client ID: {client_id} \n \
            Cipher used: {cipher}",
            )
# Metrics
        #yield Metric("pfsense_1_datareduction", float(data['data_reduction']))
        #yield Metric("pfsense_2_totalreduction", float(data['total_reduction']))
        #yield Metric("pfsense_3_thinprovisioned", float(fs_thin_provisioning))
        #yield Metric("pfsense_4_snaphots", int(fs_snapshots))
    else:
        yield Result(
            state=State.CRIT,
            summary=f"Bytes received: {get_bytes_human_readable(bytes_recv)}, Bytes Sent: {render.bytes(bytes_sent)}",
            details = f"Remote Host: {remote_host} \n \
            Virtual Address: {virtual_addr} \n \
            Connection time: {connect_time} \n \
            Client ID: {client_id} \n \
            Cipher used: {cipher}",
            )

# Metrics
        #yield Metric("pfsense_1_datareduction", float(data['data_reduction']))
        #yield Metric("pfsense_2_totalreduction", float(data['total_reduction']))
        #yield Metric("pfsense_3_thinprovisioned", float(fs_thin_provisioning))
        #yield Metric("pfsense_4_snaphots", int(fs_snapshots))

register.check_plugin(
    name="pfsense_openvpn",
    service_name="OpenVPN %s",
    discovery_function=discovery_pfsense_openvpn,
    check_function=check_pfsense_openvpn,
)
