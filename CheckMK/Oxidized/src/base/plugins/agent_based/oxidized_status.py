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
        (item, status, backup_date, backup_time, ip_address, group, model, start_date, start_time, end_date, end_time)  = row

        try:
            status:str=status
        except ValueError:
            status=0
        try:
            backup_date:str=backup_date
        except ValueError:
            backup_date=0
        try:
            backup_time:str=backup_time
        except ValueError:
            backup_time=0
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
            start_date:str=start_date
        except ValueError:
            start_date=0
        try:
            start_time:str=start_time
        except ValueError:
            start_time=0
        try:
            end_date:str=end_date
        except ValueError:
            end_date=0
        try:
            end_time:str=end_time
        except ValueError:
            end_time=0
        section[item] = {

'status' : status,
'backup_date' : backup_date,
'backup_time' : backup_time,
'ip_address' : ip_address,
'group' : group,
'model' : model,
'start_date' : start_date,
'start_time' : start_time,
'end_date' : end_date,
'end_time' : end_time,
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
    backup_date:str = data['backup_date']
    backup_time:str = data['backup_time']
    ip_address:str = data['ip_address']
    group:str = data['group']
    model :str= data['model']
    start_date :str= data['start_date']
    start_time :str= data['start_time']
    end_date :str= data['end_date']
    end_time :str= data['end_time']
    if status == 'never':
        yield Result(state=State.UNKNOWN, 
                    summary=f"No backup for {item}",
                    )
    if status == 'no_connection':
        yield Result(state=State.CRIT,
                    summary=f"Last backup at {(start_date)} {(start_time)}, ended {(end_date)} {(end_time)} at was not successful",
                    details = f"Last Update: {(backup_date)} {(backup_time)} \n \
                    Group: {(group)}, Model: {model}, IP Address: {ip_address}",
                    )
    else:
        if status == 'success':
            yield Result(state=State.OK,
                    summary=f"Last backup at {(start_date)} {(start_time)}, ended {(end_date)} {(end_time)} was successful",
                    details = f"Last Update: {(backup_date)} {(backup_time)} \n \
                    Group: {(group)}, Model: {model}, IP Address: {ip_address}",
                    )

register.check_plugin(
    name="oxidized_status",
    service_name="Config Backup %s",
    discovery_function=discovery_oxidized_status,
    check_function=check_oxidized_status,
)
