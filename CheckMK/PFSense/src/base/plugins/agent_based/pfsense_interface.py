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

def parse_pfsense_interface(string_table):
    section = {}
    for row in string_table:
        (item, hwvnic, enable, status, ipaddr, subnet, linklocal, inerrs, outerrs, collisions, inbytespass, outbytespass, inpktspass, outpktspass, inbytesblock, outbytesblock, inpktsblock, outpktsblock, outpktsblock, inbytes, outbytes, inpkts, outpkts, gateway)  = row

        try:
            hwvnic=hwvnic
        except ValueError:
            hwvnic=0
        try:
            enable=enable
        except ValueError:
            enable=0
        try:
            status=status
        except ValueError:
            status=0
        try:
            ipaddr=ipaddr
        except ValueError:
            ipaddr = 0
        try:
            subnet=subnet
        except ValueError:
            subnet = 0
        try:
            linklocal=linklocal
        except ValueError:
            linklocal=0
        try:
            inerrs=int(inerrs)
        except ValueError:
            inerrs=0
        try:
            outerrs=int(outerrs)
        except ValueError:
            outerrs=0
        try:
            collisions=int(collisions)
        except ValueError:
            mtu=0
        try:
            inbytespass=int(inbytespass)
        except ValueError:
            inbytespass=0
        try:
            outbytespass=int(outbytespass)
        except ValueError:
            outbytespass=0
        try:
            inpktspass=int(inpktspass)
        except ValueError:
            inpktspass=0
        try:
            outpktspass=int(outpktspass)
        except ValueError:
            outpktspass=0
        try:
            inbytesblock=int(inbytesblock)
        except ValueError:
            inbytesblock=0
        try:
            outbytesblock=int(outbytesblock)
        except ValueError:
            outbytesblock=0
        try:
            inpktsblock=int(inpktsblock)
        except ValueError:
            inpktsblock=0
        try:
            outpktsblock=int(outpktsblock)
        except ValueError:
            outpktsblock=0
        try:
            inbytes=int(inbytes)
        except ValueError:
            inbytes=0
        try:
            outbytes=int(outbytes)
        except ValueError:
            outbytes=0
        try:
            inpkts=int(inpkts)
        except ValueError:
            inpkts=0
        try:
            outpkts=int(outpkts)
        except ValueError:
            outpkts=0
        try:
            gateway=gateway
        except ValueError:
            gateway=0

        section[item] = {
            'hwvnic': hwvnic,
            'enable': enable,
            'status': status,
            'ipaddr': ipaddr,
            'subnet': subnet,
            'linklocal': linklocal,
            'inerrs': inerrs,
            'outerrs': outerrs,
            'collisions': collisions,
            'inbytespass': inbytespass,
            'outbytespass': outbytespass,
            'inpktspass': inpktspass,
            'outpktspass': outpktspass,
            'inbytesblock': inbytesblock,
            'outbytesblock': outbytesblock,
            'inpktsblock': inpktsblock,
            'outpktsblock': outpktsblock,
            'outpktsblock': outpktsblock,
            'inbytes': inbytes,
            'outbytes': outbytes,
            'inpkts': inpkts,
            'outpkts': outpkts,
            'gateway': gateway,
        }
    return section

register.agent_section(
    name="pfsense_interface",
    parse_function=parse_pfsense_interface,
)

def discovery_pfsense_interface(section):
    for item in section.keys():
        yield Service(item=item)

def check_pfsense_interface(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    hwvnic:str=data['hwvnic']
    enable:str=data['enable']
    status:str=data['status']
    ipaddr:str=data['ipaddr']
    subnet:str=data['subnet']
    linklocal:str=data['linklocal']
    inerrs:int=data['inerrs']
    outerrs:int=data['outerrs']
    collisions:int=data['collisions']
    inbytespass:int=data['inbytespass']
    outbytespass:int=data['outbytespass']
    inpktspass:int=data['inpktspass']
    outpktspass:int=data['outpktspass']
    inbytesblock:int=data['inbytesblock']
    outbytesblock:int=data['outbytesblock']
    inpktsblock:int=data['inpktsblock']
    outpktsblock:int=data['outpktsblock']
    outpktsblock:int=data['outpktsblock']
    inbytes:int=data['inbytes']
    outbytes:int=data['outbytes']
    inpkts:int=data['inpkts']
    outpkts:int=data['outpkts']
    gateway:str=data['gateway']

    if item in section.keys():
        yield Result(
            state=State.OK,
            summary=f"status: {status},Enabled: {enable}, vNIC: {hwvnic},LinkLocal: {linklocal},IP Address: {ipaddr},Subnet: {subnet},Gateway: {gateway}",
            details = f"Errors out: {inerrs} \n \
            Errors in: {outerrs}\n \
            incomming packets pass: {inpktspass}\n \
            outgoing packets pass: {outpktspass}\n \
            incomming packets blocked: {inpktsblock}\n \
            outgoing packets blocked: {outpktsblock}\n \
            incomming packets: {inpkts}\n \
            outgoing packets: {outpkts}\n \
            collisions: {collisions}",
        )
# Metrics
        yield Metric("inerrs", int(inerrs))
        yield Metric("outerrs", int(outerrs))
        yield Metric("inbytespass", int(inbytespass))
        yield Metric("outbytespass", int(outbytespass))
        yield Metric("inpktspass", int(inpktspass))
        yield Metric("outpktspass", int(outpktspass))
        yield Metric("inbytesblock", int(inbytesblock))
        yield Metric("outbytesblock", int(outbytesblock))
        yield Metric("inpktsblock", int(inpktsblock))
        yield Metric("outpktsblock", int(outpktsblock))
        yield Metric("inbytes", int(inbytes))
        yield Metric("outbytes", int(outbytes))
        yield Metric("inpkts", int(inpkts))
        yield Metric("outpkts", int(outpkts))
    else:
        yield Result(
            state=State.CRIT,
            summary=f"status: {status},Enabled: {enable}, vNIC: {hwvnic},LinkLocal: {linklocal},IP Address: {ipaddr},Subnet: {subnet},Gateway: {gateway}",
            details = f"Errors out: {inerrs} \n \
            Errors in: {outerrs}\n \
            incomming packets pass: {inpktspass}\n \
            outgoing packets pass: {outpktspass}\n \
            incomming packets blocked: {inpktsblock}\n \
            outgoing packets blocked: {outpktsblock}\n \
            incomming packets: {inpkts}\n \
            outgoing packets: {outpkts}\n \
            collisions: {collisions}",
            )
# Metrics
        yield Metric("inerrs", int(inerrs))
        yield Metric("outerrs", int(outerrs))
        yield Metric("inbytespass", int(inbytespass))
        yield Metric("outbytespass", int(outbytespass))
        yield Metric("inpktspass", int(inpktspass))
        yield Metric("outpktspass", int(outpktspass))
        yield Metric("inbytesblock", int(inbytesblock))
        yield Metric("outbytesblock", int(outbytesblock))
        yield Metric("inpktsblock", int(inpktsblock))
        yield Metric("outpktsblock", int(outpktsblock))
        yield Metric("inbytes", int(inbytes))
        yield Metric("outbytes", int(outbytes))
        yield Metric("inpkts", int(inpkts))
        yield Metric("outpkts", int(outpkts))

register.check_plugin(
    name="pfsense_interface",
    service_name="Interface %s",
    discovery_function=discovery_pfsense_interface,
    check_function=check_pfsense_interface,
)
