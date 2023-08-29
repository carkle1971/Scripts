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


def _valuespec_special_agents_pfsense():
    return Dictionary(
        title = _("PFSense via WebAPI"),
        help = _("This rule set selects the special agent for pfsense"),
        elements = [
            ("-H", TextAscii(title = _("Appliance IP"), allow_empty = False, help = _("Type or paste the PFSense Appliance IP here."))),
            ("port", NetworkPort(title = _("Port"),default_value = 4443, minvalue = 1, maxvalue = 65535,help = _("Type or paste appliance port here."))),
            ("-u", TextAscii(title = _("Username"), allow_empty = False, help = _("Type or paste the username here."))),
            ("-p", Password(title = _("Password"), allow_empty = False, help = _("Type or paste the user password here."))),
        ],
        optional_keys=[],
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsHardware,
        name="special_agents:pfsense",
        valuespec=_valuespec_special_agents_pfsense,
    )
)
