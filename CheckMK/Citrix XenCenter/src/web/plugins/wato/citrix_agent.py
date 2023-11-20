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
    RulespecGroupDatasourceProgramsHardware,
)


def _valuespec_special_agents_citrix():
    return Dictionary(
        title = _("Citrix XenCenter via API"),
        help = _("This rule set selects the special agent for citrix"),
        elements = [
            ("-H", TextAscii(title = _("Xencenter FQDN"), allow_empty = False, help = _("Type or paste the Citrix Xencenter IP here."))),
            ("-u", TextAscii(title = _("Username"), allow_empty = False, help = _("Type or paste the username here."))),
            ("-p", Password(title = _("Password"), allow_empty = False, help = _("Type or paste the user password here."))),
        ],
        optional_keys=[],
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsHardware,
        name="special_agents:citrix",
        valuespec=_valuespec_special_agents_citrix,
    )
)
