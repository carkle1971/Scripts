#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
##  MIT License
##  
##  Copyright (c) 2021 Bash Club
##  
##  Permission is hereby granted, free of charge, to any person obtaining a copy
##  of this software and associated documentation files (the "Software"), to deal
##  in the Software without restriction, including without limitation the rights
##  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##  copies of the Software, and to permit persons to whom the Software is
##  furnished to do so, subject to the following conditions:
##  
##  The above copyright notice and this permission notice shall be included in all
##  copies or substantial portions of the Software.
##  
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##  SOFTWARE.

from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import (
    metric_info,
    graph_info,
    translation
)


# Colors:
#
#                   red
#  magenta                       orange
#            11 12 13 14 15 16
#         46                   21
#         45                   22
#   blue  44                   23  yellow
#         43                   24
#         42                   25
#         41                   26
#            36 35 34 33 32 31
#     cyan                       yellow-green
#                  green
#
# Special colors:
# 51  gray
# 52  brown 1
# 53  brown 2
#
# For a new metric_info you have to choose a color. No more hex-codes are needed!
# Instead you can choose a number of the above color ring and a letter 'a' or 'b
# where 'a' represents the basic color and 'b' is a nuance/shading of the basic color.
# Both number and letter must be declared!
#
# Example:
# "color" : "23/a" (basic color yellow)
# "color" : "23/b" (nuance of color yellow)
#

metric_info["mbuf_usage"] = {
    "title": _("mbuf_usage"),
    "unit": "a",
    "color": "144/a",
}
metric_info["mem_usage"] = {
    "title": _("mem_usage"),
    "unit": "v",
    "color": "23/a",
}
metric_info["swap_usage"] = {
    "title": _("swap_usage"),
    "unit": "w",
    "color": "33/a",
}

metric_info["disk_usage"] = {
    "title": _("disk_usage"),
    "unit": "w",
    "color": "33/a",
}

metric_info["delay"] = {
    "title": _("delay"),
    "unit": "a",
    "color": "144/a",
}
metric_info["stddev"] = {
    "title": _("stddev"),
    "unit": "v",
    "color": "23/a",
}
metric_info["loss"] = {
    "title": _("loss"),
    "unit": "w",
    "color": "33/a",
}


metric_info["inerrs"] = {
    "title": _("inerrs"),
    "unit": "%",
    "color": "16/a",
}

metric_info["outerrs"] = {
    "title": _("outerrs"),
    "unit": "a",
    "color": "12/a",
}
metric_info["collisions"] = {
    "title": _("collisions"),
    "unit": "v",
    "color": "13/a",
}
metric_info["inbytespass"] = {
    "title": _("inbytespass"),
    "unit": "w",
    "color": "16/a",
}

metric_info["outbytespass"] = {
    "title": _("outbytespass"),
    "unit": "",
    "color": "12/b",
}
metric_info["inpktspass"] = {
    "title": _("inpktspass"),
    "unit": "",
    "color": "16/a",
}
metric_info["outpktspass"] = {
    "title": _("outpktspass"),
    "unit": "%",
    "color": "12/a",
}

metric_info["inbytesblock"] = {
    "title": _("inbytesblock"),
    "unit": "a",
    "color": "16/a",
}
metric_info["outbytesblock"] = {
    "title": _("outbytesblock"),
    "unit": "v",
    "color": "12/a",
}
metric_info["inpktsblock"] = {
    "title": _("inpktsblock"),
    "unit": "w",
    "color": "16/a",
}

metric_info["outpktsblock"] = {
    "title": _("outpktsblock"),
    "unit": "",
    "color": "12/a",
}
metric_info["inbytes"] = {
    "title": _("inbytes"),
    "unit": "%",
    "color": "16/a",
}

metric_info["outbytes"] = {
    "title": _("outbytes"),
    "unit": "a",
    "color": "12/a",
}
metric_info["inpkts"] = {
    "title": _("inpkts"),
    "unit": "v",
    "color": "16/a",
}
metric_info["outpkts"] = {
    "title": _("outpkts"),
    "unit": "w",
    "color": "11/a",
}


graph_info["inners_outers_combined"] = {
    "title" : _("inners_outers_combined"),
    "metrics" : [
        ("inerrs","area"),
        ("outerrs","stack"),
    ],
}

graph_info["inbytespass_outbytespass_combined"] = {
    "title" : _("inbytespass_outbytespass_combined"),
    "metrics" : [
        ("inbytespass","area"),
        ("outbytespass","stack"),
    ],
}

graph_info["inpktspass_outpktspass_sta_combined"] = {
    "title" : _("inpktspass_outpktspass_sta_combined"),
    "metrics" : [
        ("inpktspass","area"),
        ("outpktspass","stack"),
    ],
}

graph_info["inbytesblock_outbytesblock_combined"] = {
    "title" : _("inbytesblock_outbytesblock_combined"),
    "metrics" : [
        ("inbytesblock","area"),
        ("outbytesblock","stack"),
    ],
}

graph_info["inpktsblock_outpktsblock_combined"] = {
    "title" : _("inpktsblock_outpktsblock_combined"),
    "metrics" : [
        ("inpktsblock","area"),
        ("outpktsblock","stack"),
    ],
}

graph_info["inbytes_outbytes_combined"] = {
    "title" : _("inbytes_outbytes_combined"),
    "metrics" : [
        ("inbytes","area"),
        ("outbytes","stack"),
    ],
}

graph_info["inpkts_outpkts_combined"] = {
    "title" : _("inpkts_outpkts_combined"),
    "metrics" : [
        ("inpkts","area"),
        ("outpkts","stack"),
    ],
}
