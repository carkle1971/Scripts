#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
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

metric_info["pure_1_datareduction"] = {
    "title": _("Data reduction for volume"),
    "unit": "count",
    "color": "52/a",
}

metric_info["pure_2_totalreduction"] = {
    "title": _("Total reduction for volume"),
    "unit": "count",
    "color": "52/b",
}

metric_info["pure_3_thinprovisioned"] = {
    "title": _("Thin Provisioned space"),
    "unit": "count",
    "color": "11/a",
}

metric_info["pure_4_snaphots"] = {
    "title": _("Space in use for snapshots"),
    "unit": "bytes",
    "color": "16/a",
}

metric_info["pure_provisioning"] = {
    "title": _("Provisioned filesystem space"),
    "unit": "bytes",
    "color": "23/a",
}

metric_info["pure_capacity"] = {
    "title": _("Array capacity"),
    "unit": "bytes",
    "color": "44/a",
}
metric_info["pure_provisioned"] = {
    "title": _("Provisioned space"),
    "unit": "bytes",
    "color": "23/a",
}
metric_info["pure_total"] = {
    "title": _("Total used space"),
    "unit": "bytes",
    "color": "33/a",
}

metric_info["pure_shared"] = {
    "title": _("Shared space"),
    "unit": "bytes",
    "color": "26/a",
}

metric_info["pure_volumes"] = {
    "title": _("Unique space used"),
    "unit": "bytes",
    "color": "13/a",
}

metric_info["pure_datareduction"] = {
    "title": _("Data reduction for array"),
    "unit": "count",
    "color": "52/a",
}

metric_info["pure_totalreduction"] = {
    "title": _("Total reduction for array"),
    "unit": "count",
    "color": "52/b",
}

metric_info["pure_snaphots"] = {
    "title": _("Space in use for snapshots"),
    "unit": "bytes",
    "color": "16/a",
}

metric_info["pure_percentage"] = {
    "title": _("Percentage Used"),
    "unit": "bytes",
    "color": "26/a",
}

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

graph_info["pure_details"] = {
    "title": _("Filesystem size and Used after deduplication"),
    "metrics": [
        ("fs_size", "area"),
        ("pure_provisioning", "stack"),
        ("fs_dedup_ratio", "line"),
    ],
    "scalars": [
        "fs_used:warn",
        "fs_provisioning:crit",
    ],
    "range": (0, "fs_used:max"),
}

graph_info["pure_array_info"] = {
    "title": _("Pure array information"),
    "metrics": [
        ("pure_capacity", "line"),
        ("pure_total", "line"),
        ("pure_volumes", "line"),
    ],
    "scalars": [
        "pure_capacity:warn",
        "pure_total:crit",
    ],
    "range": (0, "pure_capacity:max"),
}