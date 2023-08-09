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
        (item, vpnid, mode, protocol, dev_mode, interface, ipaddr, local_port, custom_options, caref, crlref, ocspurl, certref, dh_length, ecdh_curve, cert_depth,remote_cert_tls, data_ciphers_fallback, digest, engine, tunnel_network, tunnel_networkv6, remote_network, remote_networkv6, gwredir, gwredir6, local_network, local_networkv6, maxclients, allow_compression, compression, compression_push, passtos, client2client, dynamic_ip, topology, serverbridge_dhcp, serverbridge_interface, serverbridge_routegateway, serverbridge_dhcp_start, serverbridge_dhcp_end, username_as_common_name, sndrcvbuf, netbios_enable, netbios_ntype, netbios_scope, create_gw, verbosity_level, data_ciphers, ncp_enable, ping_method, keepalive_interval, keepalive_timeout, ping_seconds, ping_push, ping_action, ping_action_seconds, ping_action_push, inactive_seconds)  = row

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
            custom_options:str=custom_options
        except ValueError:
            custom_options=0
        try:
            caref:str=caref
        except ValueError:
            caref=0
        try:
            crlref:str=crlref
        except ValueError:
            crlref=0
        try:
            ocspurl:str=ocspurl
        except ValueError:
            ocspurl=0
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
            remote_cert_tls:str=remote_cert_tls
        except ValueError:
            remote_cert_tls=0
        try:
            data_ciphers_fallback:str=data_ciphers_fallback
        except ValueError:
            data_ciphers_fallback=0
        try:
            digest:str=digest
        except ValueError:
            digest=0
        try:
            engine:str=engine
        except ValueError:
            engine=0            
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
            maxclients:int=maxclients
        except ValueError:
            maxclients=0
        try:
            allow_compression:str=allow_compression
        except ValueError:
            allow_compression=0
        try:
            compression:str=compression
        except ValueError:
            compression=0
        try:
            compression_push:str=compression_push
        except ValueError:
            compression_push=0
        try:
            passtos:str=passtos
        except ValueError:
            passtos=0            
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
            netbios_enable:str=netbios_enable
        except ValueError:
            netbios_enable=0
        try:
            netbios_ntype:int=netbios_ntype
        except ValueError:
            netbios_ntype=0
        try:
            netbios_scope:str=netbios_scope
        except ValueError:
            netbios_scope=0
        try:
            create_gw:str=create_gw
        except ValueError:
            create_gw=0            
        try:
            verbosity_level:int=verbosity_level
        except ValueError:
            verbosity_level=0
        try:
            data_ciphers:str=data_ciphers
        except ValueError:
            data_ciphers=0
        try:
            ncp_enable:str=ncp_enable
        except ValueError:
            ncp_enable=0
        try:
            ping_method:str=ping_method
        except ValueError:
            ping_method=0
        try:
            keepalive_interval=keepalive_interval
        except ValueError:
            keepalive_interval=0
        try:
            keepalive_timeout:int=keepalive_timeout
        except ValueError:
            keepalive_timeout=0
        try:
            ping_seconds:int=ping_seconds
        except ValueError:
            ping_seconds=0            
        try:
            ping_push:int=ping_push
        except ValueError:
            ping_push=0
        try:
            ping_action:str=ping_action
        except ValueError:
            ping_action=0
        try:
            ping_action_seconds:int=ping_action_seconds
        except ValueError:
            ping_action_seconds=0
        try:
            ping_action_push:int=ping_action_push
        except ValueError:
            ping_action_push=0
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
'custom_options' : custom_options,
'caref' : caref,
'crlref' : crlref,
'ocspurl' : ocspurl,
'certref' : certref,
'dh_length' : dh_length,
'ecdh_curve' : ecdh_curve,
'cert_depth' : cert_depth,
'remote_cert_tls' : remote_cert_tls,
'data_ciphers_fallback' : data_ciphers_fallback,
'digest' : digest,
'engine' : engine,
'tunnel_network' : tunnel_network,
'tunnel_networkv6' : tunnel_networkv6,
'remote_network' : remote_network,
'remote_networkv6' : remote_networkv6,
'gwredir' : gwredir,
'gwredir6' : gwredir6,
'local_network' : local_network,
'local_networkv6' : local_networkv6,
'maxclients' : maxclients,
'allow_compression' : allow_compression,
'compression' : compression,
'compression_push' : compression_push,
'passtos' : passtos,
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
'netbios_enable' : netbios_enable,
'netbios_ntype' : netbios_ntype,
'netbios_scope' : netbios_scope,
'create_gw' : create_gw,
'verbosity_level' : verbosity_level,
'data_ciphers' : data_ciphers,
'ncp_enable' : ncp_enable,
'ping_method' : ping_method,
'keepalive_interval' : keepalive_interval,
'keepalive_timeout' : keepalive_timeout,
'ping_seconds' : ping_seconds,
'ping_push' : ping_push,
'ping_action' : ping_action,
'ping_action_seconds' : ping_action_seconds,
'ping_action_push' : ping_action_push,
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
    custom_options:str = data['custom_options']
    caref:str = data['caref']
    ocspurl:str = data['ocspurl']
    crlref:str = data['crlref']
    certref:str = data['certref']
    dh_length:int = data['dh_length']
    ecdh_curve:str = data['ecdh_curve']
    cert_depth:str = data['cert_depth']
    remote_cert_tls:str = data['remote_cert_tls']
    data_ciphers_fallback:str = data['data_ciphers_fallback']
    digest:str = data['digest']
    engine:str = data['engine']
    tunnel_network:str = data['tunnel_network']
    tunnel_networkv6:str = data['tunnel_networkv6']
    remote_network:str = data['remote_network']
    remote_networkv6:str = data['remote_networkv6']
    gwredir:str = data['gwredir']
    gwredir6:str = data['gwredir6']
    local_network:str = data['local_network']
    local_networkv6:str = data['local_networkv6']
    maxclients:int = data['maxclients']
    allow_compression:str = data['allow_compression']
    compression:str = data['compression']
    compression_push:str = data['compression_push']
    passtos:str = data['passtos']
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
    netbios_enable:str = data['netbios_enable']
    netbios_ntype:int= data['netbios_ntype']
    netbios_scope:str = data['netbios_scope']
    create_gw:str = data['create_gw']
    verbosity_level:int  = data['verbosity_level']
    data_ciphers:str = data['data_ciphers']
    ncp_enable:str = data['ncp_enable']
    ping_method:str = data['ping_method']
    keepalive_interval:int  = data['keepalive_interval']
    keepalive_timeout:int  = data['keepalive_timeout']
    ping_seconds:int = data['ping_seconds']
    ping_push:str = data['ping_push']
    ping_action:str = data['ping_action']
    ping_action_seconds:int  = data['ping_action_seconds']
    ping_action_push:int  = data['ping_action_push']
    inactive_seconds:int  = data['inactive_seconds']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"VPN ID: {(vpnid)}, Mode: {(mode)}, Protocol: {protocol}, DEVMode: {dev_mode}, Port: {local_port}, Interface: {(interface)}, IP Address: {ipaddr}, local network: {(local_network)}, remote_network: {(remote_network)}, tunnel_network: {tunnel_network}, gwredir6: {gwredir6}",
           
            
            details = f" Custom Options: {custom_options}, Certificate: {certref}, CA Certificate: {caref}, CRL Certificate: {crlref} \n \
            dh_length: {(dh_length)}, ecdh_curve: {ecdh_curve}, cert_depth: {cert_depth}, remote_cert_tls: {remote_cert_tls} \n \
            data_ciphers_fallback: {(data_ciphers_fallback)}, digest: {digest}, tunnel_network: {tunnel_network}, tunnel_networkv6: {tunnel_networkv6} \n \
            remote_network: {(remote_network)}, remote_networkv6: {remote_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            local_network: {(local_network)}, local_networkv6: {local_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            allow_compression: {allow_compression},compression: {compression}, compression_push: {compression_push}, client2client: {client2client}, topology: {topology} \n \
            serverbridge_dhcp: {serverbridge_dhcp}, serverbridge_interface: {serverbridge_interface},serverbridge_routegateway: {serverbridge_routegateway} \n \
            serverbridge_dhcp_start:{serverbridge_dhcp_start}, serverbridge_dhcp_end:{serverbridge_dhcp_end} \n \
            username_as_common_name:{username_as_common_name}, sndrcvbuf:{sndrcvbuf}, netbios_enable:{netbios_enable}, netbios_ntype:{netbios_ntype} \n \
            netbios_scope:{netbios_scope}, create_gw:{create_gw}, verbosity_level:{verbosity_level}, data_ciphers:{data_ciphers}, ncp_enable:{ncp_enable} \n \
            ping_method:{ping_method}, keepalive_interval:{keepalive_interval}, keepalive_timeout:{keepalive_timeout}, ping_seconds:{ping_seconds} \n \
            ping_push:{ping_push}, ping_action:{ping_action}, ping_action_seconds:{ping_action_seconds} \n \
            ping_action_push:{ping_action_push}, inactive_seconds:{inactive_seconds}",
            )

    else:
        yield Result(
            state=State.CRIT,
            summary=f"VPN ID: {(vpnid)}, Mode: {(mode)}, Protocol: {protocol}, DEVMode: {dev_mode}, Port: {local_port}, Interface: {(interface)}, IP Address: {ipaddr}",
           
            
            details = f" Custom Options: {custom_options}, Certificate: {certref}, CA Certificate: {caref}, CRL Certificate: {crlref} \n \
            dh_length: {(dh_length)}, ecdh_curve: {ecdh_curve}, cert_depth: {cert_depth}, remote_cert_tls: {remote_cert_tls} \n \
            data_ciphers_fallback: {(data_ciphers_fallback)}, digest: {digest}, tunnel_network: {tunnel_network}, tunnel_networkv6: {tunnel_networkv6} \n \
            remote_network: {(remote_network)}, remote_networkv6: {remote_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            local_network: {(local_network)}, local_networkv6: {local_networkv6}, gwredir: {gwredir}, gwredir6: {gwredir6} \n \
            allow_compression: {allow_compression},compression: {compression}, compression_push: {compression_push}, client2client: {client2client}, topology: {topology} \n \
            serverbridge_dhcp: {serverbridge_dhcp}, serverbridge_interface: {serverbridge_interface},serverbridge_routegateway: {serverbridge_routegateway} \n \
            serverbridge_dhcp_start:{serverbridge_dhcp_start}, serverbridge_dhcp_end:{serverbridge_dhcp_end} \n \
            username_as_common_name:{username_as_common_name}, sndrcvbuf:{sndrcvbuf}, netbios_enable:{netbios_enable}, netbios_ntype:{netbios_ntype} \n \
            netbios_scope:{netbios_scope}, create_gw:{create_gw}, verbosity_level:{verbosity_level}, data_ciphers:{data_ciphers}, ncp_enable:{ncp_enable} \n \
            ping_method:{ping_method}, keepalive_interval:{keepalive_interval}, keepalive_timeout:{keepalive_timeout}, ping_seconds:{ping_seconds} \n \
            ping_push:{ping_push}, ping_action:{ping_action}, ping_action_seconds:{ping_action_seconds} \n \
            ping_action_push:{ping_action_push}, inactive_seconds:{inactive_seconds}",
            )


register.check_plugin(
    name="pfsense_server",
    service_name="OpenVPN Server %s",
    discovery_function=discovery_pfsense_server,
    check_function=check_pfsense_server,
)
