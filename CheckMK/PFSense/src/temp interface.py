def get_pfsense_openvpn_interface():
    print()
try:
    interface = requests.get(('https://' + hostname + ':4443/api/v1/status/interface'), verify=False, auth=(username, password)).text
    print("<<<pfsense_openvpn_interface>>>")
    interface_output = json.loads(interface.replace('if','vnic'))
    interface_print = interface_output['data']
    print('\n'' '.join(map(str, interface_print)))
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)

def get_pfsense_system():
    print("<<<>>>")
try:
    response = requests.get(('https://' + hostname + ':4443/api/v1/status/system'), verify=False, auth=(username, password)).text
    inline_system = json.loads(response.replace('_',''))
    system_print = inline_system['data']
    print("<<<pfsense_system>>>")
    for line_syst in response:
            if line_syst['status'] == 'ok':
                system_platform:str = line_syst['system_platform']
                system_netgate_id:str = line_syst['system_netgate_id']
                bios_vendor:str = line_syst['bios_vendor']
                bios_version:int = line_syst['bios_version']
                cpu_model:str = line_syst['cpu_model']
                kernel_pti:str = line_syst['kernel_pti']
                cpu_count:int = line_syst['cpu_count']
                mbuf_usage:int = line_syst['mbuf_usage']
                mem_usage:int = line_syst['mem_usage']
                swap_usage:int = line_syst['swap_usage']
                disk_usage:int = line_syst['disk_usage']
                print(f"{system_platform} {system_netgate_id} {bios_vendor} {bios_version} {cpu_model} {kernel_pti} {cpu_count} {mbuf_usage} {mem_usage} {swap_usage} {disk_usage}")
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)


def get_pfsense_openvpn_gateway():
    print("<<<pfsense_openvpn_gateway:sep(0)>>>")
try:
    gateway = requests.get(('https://' + hostname + ':4443/api/v1/status/gateway'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_gateway>>>")
    gatewayoutput = json.loads(gateway)
    print(gatewayoutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)

def get_pfsense_openvpn_system():
    print("<<<>>>")
try:
    system = requests.get(('https://' + hostname + ':4443/api/v1/status/system'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_system:sep(0)>>>")
    systemoutput = json.loads(system)
    print(systemoutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)

def get_pfsense_openvpn_server():
    print("<<<>>>")
try:
    server = requests.get(('https://' + hostname + ':4443/api/v1/services/openvpn/server'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_server:sep(0)>>>")
    serveroutput = json.loads(server)
    print(serveroutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)

def get_pfsense_openvpn_status():
    print("<<<>>>")
try:
    status = requests.get(('https://' + hostname + ':4443/api/v1/status/openvpn'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_status:sep(0)>>>")
    statusoutput = json.loads(status)
    print(statusoutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)
def get_pfsense_openvpn_gateway():
    print("<<<pfsense_openvpn_gateway:sep(0)>>>")
try:
    gateway = requests.get(('https://' + hostname + ':4443/api/v1/status/gateway'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_gateway>>>")
    gatewayoutput = json.loads(gateway)
    print(gatewayoutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)

def get_pfsense_openvpn_system():
    print("<<<>>>")
try:
    system = requests.get(('https://' + hostname + ':4443/api/v1/status/system'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_system:sep(0)>>>")
    systemoutput = json.loads(system)
    print(systemoutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)

def get_pfsense_openvpn_server():
    print("<<<>>>")
try:
    server = requests.get(('https://' + hostname + ':4443/api/v1/services/openvpn/server'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_server:sep(0)>>>")
    serveroutput = json.loads(server)
    print(serveroutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)

def get_pfsense_openvpn_status():
    print("<<<>>>")
try:
    status = requests.get(('https://' + hostname + ':4443/api/v1/status/openvpn'), verify=False, headers={"content-type": "application/json"}, auth=(username, password))
    print("<<<pfsense_openvpn_status:sep(0)>>>")
    statusoutput = json.loads(status)
    print(statusoutput['data'])
except OSError:
    print(f"Connection error to host {hostname}")
    sys.exit(1)



    get_pfsense_openvpn_gateway()
    get_pfsense_openvpn_system()
    get_pfsense_openvpn_server()
    get_pfsense_openvpn_status()