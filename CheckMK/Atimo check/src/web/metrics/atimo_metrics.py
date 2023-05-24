#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
# 2023 created by Carlo Kleinloog
#/omd/sites/SITE/local/share/check_mk/web/plugins/metrics
from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import (
    metric_info,
    graph_info,
    translation
)

# .
#   .--Metrics-------------------------------------------------------------.
#   |                   __  __      _        _                             |
#   |                  |  \/  | ___| |_ _ __(_) ___ ___                    |
#   |                  | |\/| |/ _ \ __| '__| |/ __/ __|                   |
#   |                  | |  | |  __/ |_| |  | | (__\__ \                   |
#   |                  |_|  |_|\___|\__|_|  |_|\___|___/                   |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definitions of metrics                                              |
#   '----------------------------------------------------------------------'

# Title are always lower case - except the first character!
# Colors: See indexed_color() in cmk/gui/plugins/metrics/utils.py

metric_info["remaining_jobs_metric"] = {
    "title": _("metric of jobs out of sync"),
    "unit": "count",
    "color": "33/a",
}

perfometer_info.append({
    "type": "linear",
    "segments": ["remaining_jobs_perfometer"],
    "total": 6000.0,
}) 

perfometer_info.append({
    "type": "linear",
    "segments": ["remaining_jobs_perfometer_warn"],
    "total": 201.0,
}) 

perfometer_info.append({
    "type": "linear",
    "segments": ["remaining_jobs_perfometer_crit"],
    "total": 1000.0,
}) 

perfometer_info.append({
    "type": "linear",
    "segments": ["remaining_jobs_perfometer_max"],
    "total": 6000.0,
}) 

# .
#   .--Graphs--------------------------------------------------------------.
#   |                    ____                 _                            |
#   |                   / ___|_ __ __ _ _ __ | |__  ___                    |
#   |                  | |  _| '__/ _` | '_ \| '_ \/ __|                   |
#   |                  | |_| | | | (_| | |_) | | | \__ \                   |
#   |                   \____|_|  \__,_| .__/|_| |_|___/                   |
#   |                                  |_|                                 |
#   +----------------------------------------------------------------------+
#   |  Definitions of time series graphs                                   |
#   '----------------------------------------------------------------------'

graph_info["atimo_details"] = {
    "title": _("perfometer of jobs out of sync history"),
    "perfometers": [
        ("remaining_jobs_perfometer", "line"),
    ],
    "scalars": [
        "remaining_jobs_perfometer_warn:warn",
        "remaining_jobs_perfometer_crit:crit",
    ],
    "range": (0, "remaining_jobs_perfometer_max:max"),
}