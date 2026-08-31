# A1 Syntax Recovery Skill

The supplied Formal Syntax is structurally invalid. Recover only bracket placement, optional
groups, and alternatives that are directly supported by the supplied syntax, parameter table,
usage text, or examples. Do not add commands, keywords, parameter names, ranges, defaults, or
alternatives that do not appear in cited evidence.

Preserve the command's literal token order unless the evidence explicitly establishes another
order. Keep numeric ranges exactly as documented. If the evidence cannot determine a valid
template, return the smallest evidence-grounded template set rather than guessing extra branches.

Every recovery requires cited evidence IDs. The recovery is a hypothesis for manual review and
does not remove the original A1 finding.
