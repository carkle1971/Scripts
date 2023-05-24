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

def parse_atimo(string_table):
    section = {}
    for row in string_table:
        (item, location, networkaddress, remaining_jobs)  = row

        try:
            location = str(location)
        except ValueError:
            location = 0
        try:
            networkaddress = str(networkaddress)
        except ValueError:
            networkaddress = 0
        try:
            remaining_jobs = int(remaining_jobs)
        except ValueError:
            remaining_jobs=0

        section[item] = {
            'location': location,
            'networkaddress': networkaddress,
            'remaining_jobs': remaining_jobs,
        }

    return section


register.agent_section(
    name="atimo",
    parse_function=parse_atimo,
)

def discovery_atimo(section):
    for item in section.keys():
        yield Service(item=item)

def check_atimo(item, section):
    failed = []

    if item not in section.keys():
        yield Result(
            state=State.UNKNOWN,
            summary=f"Item {item} not found",
        )

    data = section[item]
    if section[item]['remaining_jobs'] < 200:
        yield Result(
            state=State.OK,
            summary=f"Location: {(data['location'])}, Remaining Jobs: {data['remaining_jobs']}",
            details = f"IP Address: {(data['networkaddress'])}",
        )
# Metrics
        yield Metric("remaining_jobs_metric", int(data['remaining_jobs']))
    else:
        if section[item]['remaining_jobs'] > 201 and section[item]['remaining_jobs'] < 1000:
            yield Result(
            state=State.WARN,
            summary=f"Location: {(data['location'])}, Remaining Jobs: {data['remaining_jobs']}",
            details = f"IP Address: {(data['networkaddress'])}",
        )
# Metrics
            yield Metric("remaining_jobs_metric", int(data['remaining_jobs']))
        elif section[item]['remaining_jobs'] > 1001:
            yield Result(
            state=State.CRIT,
            summary=f"Location: {(data['location'])}, Remaining Jobs: {data['remaining_jobs']}",
            details = f"IP Address: {(data['networkaddress'])}",
        )
# Metrics
            yield Metric("remaining_jobs_metric", int(data['remaining_jobs']))

register.check_plugin(
    name="atimo",
    service_name="Terminal %s",
    discovery_function=discovery_atimo,
    check_function=check_atimo,
)
