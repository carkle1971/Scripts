#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# 2023 created by Carlo Kleinloog
##  /omd/sites/BIS/local/share/check_mk/web/plugins/wato
# Check-Parameters-UI-File: file which create the WATO-UI page for configuring the parameters of the check
from cmk.gui.i18n import _

from cmk.gui.valuespec import (
    Dictionary,
    Tuple,
    Integer,
    MonitoringState,
)

# we use CheckParameterRulespecWithoutItem because we only have one line in the output of sqlquery
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)

# looks similar to old checkmk versions - still can get pretty messy if you have a lot of parameter options
# for a check
def _parameter_valuespec_sqlquery():
    return Dictionary(
        elements=[
            (
                "sqlquery",
                Tuple(
                    title="Thresholds",
                    elements=[
                       Integer(title="Warning threshold", default_value=201), #you can change these values higher or lower.
                       Integer(title="Critical threshold", default_value=1001) #you can change these values higher or lower.
                    ]
                )
            )
        ],
    )
# enddef

# need to register the thing so it works - again "WithoutItem" as we only receive one single "item"
rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="sqlquery",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_sqlquery,
        title=lambda: _("Thresholds sqlquery jobs not synced"),
    )
)