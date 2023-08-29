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

def parse_pfsense_server(string_table):
    section = {}
    for row in string_table:
        (item, vpnid, mode, protocol, dev_mode, interface, ipaddr, local_port, caref, crlref, certref, dh_length, ecdh_curve, cert_depth, data_ciphers_fallback, tunnel_network, tunnel_networkv6, remote_network, remote_networkv6, gwredir, gwredir6, local_network, local_networkv6, client2client, dynamic_ip, topology, serverbridge_dhcp, serverbridge_interface, serverbridge_routegateway, serverbridge_dhcp_start, serverbridge_dhcp_end, username_as_common_name, sndrcvbuf, create_gw, data_ciphers, inactive_seconds)  = row

        try:
            vpnid:int=vpnid
        except ValueError:
            vpnid=0
        try:
            mode:str=mode
        except ValueError:
            mode=0
        try:
            protocol:str=protocol
        except ValueError:
            protocol=0
        try:
            dev_mode:str=dev_mode
        except ValueError:
            dev_mode=0
        try:
            interface:str=interface
        except ValueError:
            interface=0            
        try:
            ipaddr:str=ipaddr
        except ValueError:
            ipaddr=0
        try:
            local_port:int=local_port
        except ValueError:
            local_port = 0
        try:
            caref:str=caref
        except ValueError:
            caref=0
        try:
            crlref:str=crlref
        except ValueError:
            crlref=0
        try:
            certref:str=certref
        except ValueError:
            certref=0            
        try:
            dh_length:int=dh_length
        except ValueError:
            dh_length=0
        try:
            ecdh_curve:str=ecdh_curve
        except ValueError:
            ecdh_curve=0
        try:
            cert_depth:str=cert_depth
        except ValueError:
            cert_depth=0
        try:
            data_ciphers_fallback:str=data_ciphers_fallback
        except ValueError:
            data_ciphers_fallback=0
        try:
            tunnel_network:str=tunnel_network
        except ValueError:
            tunnel_network=0
        try:
            tunnel_networkv6:str=tunnel_networkv6
        except ValueError:
            tunnel_networkv6=0
        try:
            remote_network:str=remote_network
        except ValueError:
            remote_network=0
        try:
            remote_networkv6:str=remote_networkv6
        except ValueError:
            remote_networkv6=0
        try:
            gwredir:str=gwredir
        except ValueError:
            gwredir=0
        try:
            gwredir6:str=gwredir6
        except ValueError:
            gwredir6=0
        try:
            local_network:str=local_network
        except ValueError:
            local_network=0            
        try:
            local_networkv6:str=local_networkv6
        except ValueError:
            local_networkv6=0
        try:
            tunnel_networkv6:str=tunnel_networkv6
        except ValueError:
            tunnel_networkv6=0
        try:
            client2client:str=client2client
        except ValueError:
            client2client=0
        try:
            dynamic_ip=dynamic_ip
        except ValueError:
            dynamic_ip=0
        try:
            topology=topology
        except ValueError:
            topology=0
        try:
            serverbridge_dhcp:str=serverbridge_dhcp
        except ValueError:
            serverbridge_dhcp=0
        try:
            serverbridge_interface:str=serverbridge_interface
        except ValueError:
            serverbridge_interface=0
        try:
            serverbridge_routegateway:str=serverbridge_routegateway
        except ValueError:
            serverbridge_routegateway=0
        try:
            serverbridge_dhcp_start:str=serverbridge_dhcp_start
        except ValueError:
            serverbridge_dhcp_start=0            
        try:
            serverbridge_dhcp_end:str=serverbridge_dhcp_end
        except ValueError:
            serverbridge_dhcp_end=0
        try:
            username_as_common_name:str=username_as_common_name
        except ValueError:
            username_as_common_name=0
        try:
            sndrcvbuf:int=sndrcvbuf
        except ValueError:
            sndrcvbuf=0
        try:
            create_gw:str=create_gw
        except ValueError:
            create_gw=0            
        try:
            data_ciphers:str=data_ciphers
        except ValueError:
            data_ciphers=0
        try:
            inactive_seconds:int=inactive_seconds
        except ValueError:
            inactive_seconds=0

        section[item] = {
'vpnid' : vpnid,
'mode' : mode,
'protocol' : protocol,
'dev_mode' : dev_mode,
'interface' : interface,
'ipaddr' : ipaddr,
'local_port' : local_port,
'caref' : caref,
'crlref' : crlref,
'certref' : certref,
'dh_length' : dh_length,
'ecdh_curve' : ecdh_curve,
'cert_depth' : cert_depth,
'data_ciphers_fallback' : data_ciphers_fallback,
'tunnel_network' : tunnel_network,
'tunnel_networkv6' : tunnel_networkv6,
'remote_network' : remote_network,
'remote_networkv6' : remote_networkv6,
'gwredir' : gwredir,
'gwredir6' : gwredir6,
'local_network' : local_network,
'local_networkv6' : local_networkv6,
'client2client' : client2client,
'dynamic_ip' : dynamic_ip,
'topology' : topology,
'serverbridge_dhcp' : serverbridge_dhcp,
'serverbridge_interface' : serverbridge_interface,
'serverbridge_routegateway' : serverbridge_routegateway,
'serverbridge_dhcp_start' : serverbridge_dhcp_start,
'serverbridge_dhcp_end' : serverbridge_dhcp_end,
'username_as_common_name' : username_as_common_name,
'sndrcvbuf' : sndrcvbuf,
'create_gw' : create_gw,
'data_ciphers' : data_ciphers,
'inactive_seconds' : inactive_seconds,

        }
    return section
register.agent_section(
    name="pfsense_server",
    parse_function=parse_pfsense_server,
)

def discovery_pfsense_server(section):
    for item in section.keys():
        yield Service(item=item)

def check_pfsense_server(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    vpnid:int = data['vpnid']
    mode:str = data['mode']
    protocol:str = data['protocol']
    dev_mode:str = data['dev_mode']
    interface :str= data['interface']
    ipaddr:str = data['ipaddr']
    local_port:int  = data['local_port']
    caref:str = data['caref']
    crlref:str = data['crlref']
    certref:str = data['certref']
    dh_length:int = data['dh_length']
    ecdh_curve:str = data['ecdh_curve']
    cert_depth:str = data['cert_depth']
    data_ciphers_fallback:str = data['data_ciphers_fallback']
    tunnel_network:str = data['tunnel_network']
    tunnel_networkv6:str = data['tunnel_networkv6']
    remote_network:str = data['remote_network']
    remote_networkv6:str = data['remote_networkv6']
    gwredir:str = data['gwredir']
    gwredir6:str = data['gwredir6']
    local_network:str = data['local_network']
    local_networkv6:str = data['local_networkv6']
    client2client:str = data['client2client']
    dynamic_ip:str = data['dynamic_ip']
    topology:str = data['topology']
    serverbridge_dhcp:str = data['serverbridge_dhcp']
    serverbridge_interface:str = data['serverbridge_interface']
    serverbridge_routegateway:str = data['serverbridge_routegateway']
    serverbridge_dhcp_start:str = data['serverbridge_dhcp_start']
    serverbridge_dhcp_end:str = data['serverbridge_dhcp_end']
    username_as_common_name:str = data['username_as_common_name']
    sndrcvbuf:int = data['sndrcvbuf']
    create_gw:str = data['create_gw']
    data_ciphers:str = data['data_ciphers']
    inactive_seconds:int  = data['inactive_seconds']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"VPN ID: {(vpnid)}, Mode: {(mode)}, Protocol: {protocol}, DEVMode: {dev_mode}, Port: {local_port}, Interface: {(interface)}, IP Address: {ipaddr}, local network: {(local_network)}, remote_network: {(remote_network)}, tunnel_network: {tunnel_network}, gwredir6: {gwredir6}",
           
            
            details = f" Certificate: {certref}, CA Certificate: {caref}, CRL Certificate: {crlref} \n \
            dh_length: {(dh_length)}, ecdh_curve: {ecdh_curve}, cert_depth: {cert_depth}, \n \
            data_ciphers:{data_ciphers}, data_ciphers_fallback: {(data_ciphers_fallback)} \n \
            tunnel_network: {tunnel_network}, tunnel_networkv6: {tunnel_networkv6} \n \
            remote_network: {(remote_network)}, remote_networkv6: {remote_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            local_network: {(local_network)}, local_networkv6: {local_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            client2client: {client2client}, topology: {topology} \n \
            serverbridge_dhcp: {serverbridge_dhcp}, serverbridge_interface: {serverbridge_interface},serverbridge_routegateway: {serverbridge_routegateway} \n \
            serverbridge_dhcp_start:{serverbridge_dhcp_start}, serverbridge_dhcp_end:{serverbridge_dhcp_end} \n \
            username_as_common_name:{username_as_common_name}, create_gw:{create_gw} \n \
            sndrcvbuf:{sndrcvbuf}, inactive_seconds:{inactive_seconds}",
            )

    else:
        yield Result(
            state=State.CRIT,
            summary=f"VPN ID: {(vpnid)}, Mode: {(mode)}, Protocol: {protocol}, DEVMode: {dev_mode}, Port: {local_port}, Interface: {(interface)}, IP Address: {ipaddr}",
           
            
            details = f" Certificate: {certref}, CA Certificate: {caref}, CRL Certificate: {crlref} \n \
            dh_length: {(dh_length)}, ecdh_curve: {ecdh_curve}, cert_depth: {cert_depth}, \n \
            data_ciphers:{data_ciphers}, data_ciphers_fallback: {(data_ciphers_fallback)} \n \
            tunnel_network: {tunnel_network}, tunnel_networkv6: {tunnel_networkv6} \n \
            remote_network: {(remote_network)}, remote_networkv6: {remote_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            local_network: {(local_network)}, local_networkv6: {local_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            client2client: {client2client}, topology: {topology} \n \
            serverbridge_dhcp: {serverbridge_dhcp}, serverbridge_interface: {serverbridge_interface},serverbridge_routegateway: {serverbridge_routegateway} \n \
            serverbridge_dhcp_start:{serverbridge_dhcp_start}, serverbridge_dhcp_end:{serverbridge_dhcp_end} \n \
            username_as_common_name:{username_as_common_name}, create_gw:{create_gw} \n \
            sndrcvbuf:{sndrcvbuf}, inactive_seconds:{inactive_seconds}",
            )


register.check_plugin(
    name="pfsense_server",
    service_name="OpenVPN Server %s",
    discovery_function=discovery_pfsense_server,
    check_function=check_pfsense_server,
)
