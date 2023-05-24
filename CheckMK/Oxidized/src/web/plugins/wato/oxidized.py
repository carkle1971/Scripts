# 2021 created by Sven Rueß, sritd.de

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Password,
)
from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
)
from cmk.gui.plugins.wato.datasource_programs import (
    RulespecGroupDatasourceProgramsHardware,
)


def _valuespec_special_agents_oxidized():
    return Dictionary(
        title = _("Oxidized via host"),
        help = _("This rule set selects the special agent for Oxidized"),
        elements = [
            ("PORT", Password(title = _("PORT"), allow_empty = False)),
        ],
        optional_keys=[],
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourceProgramsHardware,    
        name="special_agents:oxidized",
        valuespec=_valuespec_special_agents_oxidized,
    )
)

