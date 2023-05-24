#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# 2023 created by Carlo Kleinloog
##  /omd/sites/BIS/local/share/check_mk/web/plugins/wato
# Bakery-UI-File: file which creates the WATO-UI page for configuring the agent-plugin
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Password,
    Dictionary,
    TextUnicode,
    Integer,
    TextAscii,
    TextInput,
    TextAreaUnicode,
)
from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
)
from cmk.gui.plugins.wato.datasource_programs import (
    RulespecGroupDatasourceProgramsCustom,
)

def _valuespec_special_agents_atimo():
    return Dictionary(
        title = _("Atimo outstanding jobs"),
        help = _("This rule selects the specific data requested from the database."
                     "You can configure your connection settings here."),
        elements = [
            ("-H", TextAscii(title = _("Server Name"), allow_empty = False, help = _("Type or paste the database servername (fqdn) here."))),
            ("-u", TextAscii(title = _("UserName"), allow_empty = False, help = _("Type or paste the database username here."))),
            ("-p", Password(title = _("Password"), allow_empty = False, help = _("Type or paste the database user password here."))),
            ("-n", TextAscii(title = _("Database Name"), allow_empty = False, help = _("Type or paste the database name here."))),
            ("-i", TextAreaUnicode(title = _("Query"), size=60, rows=20, cols=50, allow_empty = False, help = _("Type or paste your query with 'quotes' here."))),
        ],
        optional_keys=[],
    )

rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsCustom,
        name="special_agents:atimo",
        valuespec=_valuespec_special_agents_atimo,
    )
)
