#2023 created by Carlo Kleinloog
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based
import time
import json
from datetime import datetime, timedelta
from .agent_based_api.v1 import (
    register,
    Service,
    Result,
    State,
    Metric,
    render,
)

THRESHOLD = timedelta(days=1)

def parse_oxidized_status(string_table):
    section = {}
    for row in string_table:
        (item, last_status, ip_address, group, model, backup_time, last_start_date, last_start_time, last_end_date, last_end_time)  = row

        try:
            last_status:str=last_status
        except ValueError:
            last_status=0
        try:
            ip_address:str=ip_address
        except ValueError:
            ip_address=0
        try:
            group:str=group
        except ValueError:
            group = 0
        try:
            model:str=model
        except ValueError:
            model=0
        try:
            backup_time:str=backup_time
        except ValueError:
            backup_time=0
        try:
            last_start_date:str=last_start_date
        except ValueError:
            last_start_date=0
        try:
            last_start_time:str=last_start_time
        except ValueError:
            last_start_time=0
        try:
            last_end_date:str=last_end_date
        except ValueError:
            last_end_date=0
        try:
            last_end_time:str=last_end_time
        except ValueError:
            last_end_time=0
        section[item] = {

'last_status' : last_status,
'ip_address' : ip_address,
'group' : group,
'model' : model,
'backup_time' : backup_time,
'last_start_date' : last_start_date,
'last_start_time' : last_start_time,
'last_end_date' : last_end_date,
'last_end_time' : last_end_time,
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
    last_status:str = data['last_status']
    ip_address:str = data['ip_address']
    group:str = data['group']
    model :str= data['model']
    backup_time :str= data['backup_time']
    last_start_date :str= data['last_start_date']
    last_start_time :str= data['last_start_time']
    last_end_date :str= data['last_end_date']
    last_end_time :str= data['last_end_time']
    if last_status == 'never':
        yield Result(state=State.UNKNOWN, 
                    summary=f"No backup for {item}",
                    )
    if last_status == 'no_connection':
        yield Result(state=State.CRIT,
                    summary=f"Last backup at {(last_start_date)} {(last_start_time)}, ended {(last_end_time)} at was not successful",
                    details = f"Runtime backup in seconds: {(backup_time)} \n \
                    Group: {(group)}, Model: {model}, IP Address: {ip_address}",
                    )
    else:
        if last_status == 'success':
            yield Result(state=State.OK,
                    summary=f"Last backup at {(last_start_date)} {(last_start_time)}, ended {(last_end_time)} was successful",
                    details = f"Runtime backup in seconds: {(backup_time)} \n \
                    Group: {(group)}, Model: {model}, IP Address: {ip_address}",
                    )
# Metrics
        yield Metric("oxidized_time", float(backup_time))

register.check_plugin(
    name="oxidized_status",
    service_name="Config Backup %s",
    discovery_function=discovery_oxidized_status,
    check_function=check_oxidized_status,
)
