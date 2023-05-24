#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# 2023 created by Carlo Kleinloog
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based/
# Check-File: file where the output of the agent is analyzed

import sys
import socket
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

def parse_sqlquery(string_table):
    section = {}
    for row in string_table:
        (item, collumn001, collumn002, collumn003)  = row  #Change this line and lines below if needed

        try:
            collumn001 = str(collumn001)
        except ValueError:
            collumn001 = 0
        try:
            collumn002 = str(collumn002)
        except ValueError:
            collumn002 = 0
        try:
            collumn003 = int(collumn003)
        except ValueError:
            collumn003=0

        section[item] = {
            'output1': collumn001,
            'output2': collumn002,
            'output3': collumn003,
        }

    return section


register.agent_section(
    name="sqlquery",
    parse_function=parse_sqlquery,
)

def discovery_sqlquery(section):
    for item in section.keys():
        yield Service(item=item)

def check_sqlquery(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    if section[item]['output1'] < 200: # You can change this value (200) if needed higher or lower. Make sure to change values below as wel.
        yield Result(
            state=State.OK,
            summary=f"output1: {(data['output1'])}, coutput2: {data['output2']}",
            details = f"output3: {(data['output3'])}",
        )
# Metrics
        yield Metric("output1_metric", int(data['output1']))
    else:
        if section[item]['output1'] > 201 and section[item]['output1'] < 1000: # You can change these values (201) or (1000) if needed higher or lower.
            yield Result(
            state=State.WARN,
            summary=f"output1: {(data['output1'])}, coutput2: {data['output2']}",
            details = f"output3: {(data['output3'])}",
        )
# Metrics
            yield Metric("output1", int(data['output1']))
        elif section[item]['output1'] > 1001: # You can change this value (1001) if needed higher or lower.
            yield Result(
            state=State.CRIT,
            summary=f"Location: {(data['location'])}, Remaining Jobs: {data['output1']}",
            details = f"IP Address: {(data['networkaddress'])}",
        )
# Metrics
            yield Metric("output1_metric", int(data['output1']))

register.check_plugin(
    name="sqlquery",
    service_name="Terminal %s",
    discovery_function=discovery_sqlquery,
    check_function=check_sqlquery,
)
