#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# 2023 created by Carlo Kleinloog
##  /omd/sites/BIS/local/share/check_mk/web/plugins/wato
# Bakery-UI-File: file which creates the WATO-UI page for configuring the agent-plugin
from ipaddress import ip_address
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Password,
    Dictionary,
    TextUnicode,
    Integer,
    TextAscii,
    TextInput,
    TextAreaUnicode,
    NetworkPort,
)
from cmk.gui.plugins.wato import (
    HostRulespec,
    CheckParameterRulespecWithItem,
    IndividualOrStoredPassword,
    rulespec_registry,
)
from cmk.gui.plugins.wato.datasource_programs import (
    RulespecGroupDatasourceProgramsCustom,
)


def _valuespec_special_agents_oxidized():
    return Dictionary(
        title = _("Oxidized Config Backup Check"),
        help = _("This rule set selects the special agent for oxidized"),
        elements = [
            ("-H", TextAscii(title = _("Oxidized IP"), allow_empty = False, help = _("Type or paste the Oxidized IP here."))),
        ],
        optional_keys=[],
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsCustom,
        name="special_agents:oxidized",
        valuespec=_valuespec_special_agents_oxidized,
    )
)
