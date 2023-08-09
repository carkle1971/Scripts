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

def parse_pfsense_openvpn_status(string_table):
    section = {}
    for row in string_table:
        (item, remote_host, virtual_addr, virtual_addr6, bytes_recv, bytes_sent, connect_time, connect_time_unix, user_name, client_id, peer_id, cipher)  = row

        try:
            remote_host:str=remote_host
        except ValueError:
            remote_host=0            
        try:
            virtual_addr:str=virtual_addr
        except ValueError:
            virtual_addr=0
        try:
            virtual_addr6:str=virtual_addr6
        except ValueError:
            virtual_addr6 = 0
        try:
            bytes_recv:int=bytes_recv
        except ValueError:
            bytes_recv=0
        try:
            bytes_sent:int=bytes_sent
        except ValueError:
            bytes_sent=0
        try:
            connect_time:str=connect_time
        except ValueError:
            connect_time=0
        try:
            connect_time_unix:str=connect_time_unix
        except ValueError:
            connect_time_unix=0
        try:
            user_name:str=user_name
        except ValueError:
            user_name=0            
        try:
            client_id:str=client_id
        except ValueError:
            client_id=0
        try:
            peer_id:str=peer_id
        except ValueError:
            peer_id=0
        try:
            cipher:str=cipher
        except ValueError:
            cipher=0

        section[item] = {
'remote_host' : remote_host,
'virtual_addr' : virtual_addr,
'virtual_addr6' : virtual_addr6,
'bytes_recv' : bytes_recv,
'bytes_sent' : bytes_sent,
'connect_time' : connect_time,
'connect_time_unix' : connect_time_unix,
'user_name' : user_name,
'client_id' : peer_id,
'peer_id' : connect_time_unix,
'cipher' : cipher,
        }
    return section

register.agent_section(
    name="pfsense_openvpn_status",
    parse_function=parse_pfsense_openvpn_status,
)

def discovery_pfsense_openvpn_status(section):
    for item in section.keys():
        yield Service(item=item)

def check_pfsense_openvpn_status(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    remote_host:str = data['remote_host']
    virtual_addr:str = data['virtual_addr']
    virtual_addr6:str = data['virtual_addr6']
    bytes_recv :int= data['bytes_recv']
    bytes_sent:int = data['bytes_sent']
    connect_time:str  = data['connect_time']
    connect_time_unix:str = data['connect_time_unix']
    user_name:str = data['user_name']
    client_id:str = data['client_id']
    peer_id:str = data['peer_id']
    cipher:str = data['cipher']
    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"connected since: {connect_time}, Remote Host: {(remote_host)}, Client ID: {(client_id)}, Peer ID: {(peer_id)}",

            details = f"virtual_addr {(virtual_addr)}, virtual_addr6: {virtual_addr6} \n \
            Bytes received: {(bytes_recv)}, Bytes sent: {bytes_sent}, Username: {user_name}\n \
            , Unix Time: {connect_time_unix}, Cipher used: {cipher}",
            )

    else:
        yield Result(
            state=State.CRIT,
            summary=f"connected since: {connect_time}, Remote Host: {(remote_host)}, Client ID: {(client_id)}, Peer ID: {(peer_id)}",

            details = f"virtual_addr {(virtual_addr)}, virtual_addr6: {virtual_addr6} \n \
            Bytes received: {(bytes_recv)}, Bytes sent: {bytes_sent}, Username: {user_name}\n \
            , Unix Time: {connect_time_unix}, Cipher used: {cipher}",
            )


register.check_plugin(
    name="pfsense_openvpn_status",
    service_name="OpenVPN Status %s",
    discovery_function=discovery_pfsense_openvpn_status,
    check_function=check_pfsense_openvpn_status,
)
