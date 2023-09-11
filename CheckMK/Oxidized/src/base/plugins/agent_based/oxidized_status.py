#2023 created by Carlo Kleinloog
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based
import time
import json
from datetime import datetime, timedelta
from cmk.base.check_api import get_bytes_human_readable, get_percent_human_readable
from .agent_based_api.v1 import (
    register,
    Service,
    Result,
    State,
    Metric,
    render,
)
def parse_oxidized_status(string_table):
    section = {}
    for row in string_table:
        (item, status, time, ip, group, model)  = row

        try:
            status:str=status
        except ValueError:
            status=0
        try:
            time:str=time
        except ValueError:
            time=0
        try:
            ip:str=ip
        except ValueError:
            ip=0
        try:
            group:str=group
        except ValueError:
            group = 0
        try:
            model:str=model
        except ValueError:
            model=0
        section[item] = {

'status' : status,
'time' : time,
'ip' : ip,
'group' : group,
'model' : model,
        }
    return section

register.agent_section(
    name="oxidized_status",
    parse_function=parse_oxidized_status,
)

def discovery_oxidized_status(section):
    for item in section.keys():
        yield Service(item=item)

def check_oxidized_status(item, section):
    
    data = section[item]
    status:str = data['status']
    time:str = data['time']
    ip:str = data['ip']
    group:str = data['group']
    model :str= data['model']


    if item in section.keys():
        yield Result(state=State.OK, 
                    summary=f"Last backup at {(time)} was successful",
                    details = f"Last Update: {(time)} \n \
                    Group: {(group)}, Model: {model}, IP Address: {ip}",
                    )
    else:
        yield Result(state=State.CRIT,
                    summary=f"Last backup at {(time)} was not successful",
                    details = f"Last Update: {(time)} \n \
                    Group: {(group)}, Model: {model}, IP Address: {ip}",
                    )

register.check_plugin(
    name="oxidized_status",
    service_name="Config Backup %s",
    discovery_function=discovery_oxidized_status,
    check_function=check_oxidized_status,
)
