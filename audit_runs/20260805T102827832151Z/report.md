# Probe-Driven Cisco Manual Audit

> Findings are evidence-backed candidates; the device was not revalidated.

## Summary

- Probe groups: 977
- Findings: 980
- Coverage undocumented: 977
- C1: 3
- C2: 977

## Findings

### C1 Version Ambiguity

#### F00001

- Status: confirmed
- Probe template: `N/A`
- Probe view: N/A
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/segment-routing/command/reference/b-seg-routing-cr-asr9k.html
- Reason: Page metadata and command history do not establish applicability to target version 7.7.1.
- LLM conclusion: confirmed
- Confidence: 0.90
- Review rationale: The supplied page metadata identifies a generic command reference but provides no release/version applicability for IOS XR 7.7.1.
- Evidence `M1:page` (page_metadata): Segment Routing Command Reference for Cisco ASR 9000 Series Routers - Cisco | https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/segment-routing/command/reference/b-seg-routing-cr-asr9k.html [https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/segment-routing/command/reference/b-seg-routing-cr-asr9k.html]

#### F00002

- Status: confirmed
- Probe template: `N/A`
- Probe view: N/A
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k-r7-8/routing/configuration/guide/b-routing-cg-asr9000-79x.html
- Reason: Page metadata and command history do not establish applicability to target version 7.7.1.
- LLM conclusion: confirmed
- Confidence: 0.98
- Review rationale: The supplied page metadata explicitly identifies IOS XR Release 7.9.x, which does not establish applicability to the 7.7.1 target.
- Evidence `M2:page` (page_metadata): Routing Configuration Guide for Cisco ASR 9000 Series Routers, IOS XR Release 7.9.x - Cisco | https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k-r7-8/routing/configuration/guide/b-routing-cg-asr9000-79x.html [https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k-r7-8/routing/configuration/guide/b-routing-cg-asr9000-79x.html]

#### F00003

- Status: confirmed
- Probe template: `N/A`
- Probe view: N/A
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/routing/command/reference/b-routing-cr-asr9000.html
- Reason: Page metadata and command history do not establish applicability to target version 7.7.1.
- LLM conclusion: confirmed
- Confidence: 0.90
- Review rationale: The supplied page metadata identifies a generic routing command reference and does not provide version applicability for IOS XR 7.7.1.
- Evidence `M3:page` (page_metadata): Routing Command Reference for Cisco ASR 9000 Series Routers - Cisco | https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/routing/command/reference/b-routing-cr-asr9000.html [https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/routing/command/reference/b-routing-cr-asr9000.html]

### C2 Command Undercoverage

#### F00004

- Status: unresolved
- Probe template: `<WORD> bit-position <0-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence supplies the probe template, but it contains no manual-topic or command-reference evidence that can establish that no matching command topic exists.
- Evidence `P00001:probe` (probe_template): <WORD> bit-position <0-255>

#### F00005

- Status: unresolved
- Probe template: `<WORD> bit-position <0-255>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual corpus or command-topic evidence to support or refute the asserted absence of a matching manual command.
- Evidence `P00002:probe` (probe_template): <WORD> bit-position <0-255>

#### F00006

- Status: unresolved
- Probe template: `address-family ipv4 [unicast]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template and does not substantiate that no supplied manual topic matches it in the router semantic view.
- Evidence `P00003:probe` (probe_template): address-family ipv4 [unicast]

#### F00007

- Status: unresolved
- Probe template: `address-family ipv4 [unicast]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template and does not substantiate that no supplied manual topic matches it in the VRF semantic view.
- Evidence `P00004:probe` (probe_template): address-family ipv4 [unicast]

#### F00008

- Status: unresolved
- Probe template: `adjacency stagger {<1-65535> <1-65535>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template. No manual-command or manual-coverage evidence is supplied to determine whether the claimed undercoverage exists.
- Evidence `P00005:probe` (probe_template): adjacency stagger {<1-65535> <1-65535>|disable}

#### F00009

- Status: unresolved
- Probe template: `adjacency stagger {disable|<1-65535> <1-65535>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00006:probe` (probe_template): adjacency stagger {disable|<1-65535> <1-65535>}

#### F00010

- Status: unresolved
- Probe template: `adjacency-sid absolute <15000-1048575> [neighbor-address <A.B.C.D>|protected]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00007:probe` (probe_template): adjacency-sid absolute <15000-1048575> [neighbor-address <A.B.C.D>|protected]

#### F00011

- Status: unresolved
- Probe template: `adjacency-sid absolute <15000-1048575> [protected|neighbor-address <A.B.C.D>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00008:probe` (probe_template): adjacency-sid absolute <15000-1048575> [protected|neighbor-address <A.B.C.D>]

#### F00012

- Status: unresolved
- Probe template: `adjacency-sid index <0-1048575> [neighbor-address <A.B.C.D>|protected]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00009:probe` (probe_template): adjacency-sid index <0-1048575> [neighbor-address <A.B.C.D>|protected]

#### F00013

- Status: unresolved
- Probe template: `adjacency-sid index <0-1048575> [protected|neighbor-address <A.B.C.D>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual-command evidence or a complete manual corpus from which absence of a matching topic can be verified.
- Evidence `P00010:probe` (probe_template): adjacency-sid index <0-1048575> [protected|neighbor-address <A.B.C.D>]

#### F00014

- Status: unresolved
- Probe template: `admin-weight <0-65535>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual-command evidence or a complete manual corpus from which absence of a matching topic can be verified.
- Evidence `P00011:probe` (probe_template): admin-weight <0-65535>

#### F00015

- Status: unresolved
- Probe template: `advertise prefix route-policy <WORD>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual-command evidence or a complete manual corpus from which absence of a matching topic can be verified.
- Evidence `P00012:probe` (probe_template): advertise prefix route-policy <WORD>

#### F00016

- Status: unresolved
- Probe template: `advertise-definition`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual-command evidence or a complete manual corpus from which absence of a matching topic can be verified.
- Evidence `P00013:probe` (probe_template): advertise-definition

#### F00017

- Status: unresolved
- Probe template: `affinity exclude-any`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence identifies the probe command, but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00014:probe` (probe_template): affinity exclude-any

#### F00018

- Status: unresolved
- Probe template: `affinity exclude-any <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The probe template is evidenced, but absence of a matching manual topic cannot be established without manual-search or manual-content evidence.
- Evidence `P00015:probe` (probe_template): affinity exclude-any <WORD>

#### F00019

- Status: unresolved
- Probe template: `affinity flex-algo`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes only the probe template. It does not substantiate the claimed lack of a matching command topic in the manuals.
- Evidence `P00016:probe` (probe_template): affinity flex-algo

#### F00020

- Status: unresolved
- Probe template: `affinity flex-algo <WORD>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The probe template is supported, but no evidence of the supplied manuals or their command-topic coverage is provided to confirm the undercoverage claim.
- Evidence `P00017:probe` (probe_template): affinity flex-algo <WORD>

#### F00021

- Status: unresolved
- Probe template: `affinity include-all`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual-content evidence sufficient to verify that no matching command topic exists.
- Evidence `P00018:probe` (probe_template): affinity include-all

#### F00022

- Status: unresolved
- Probe template: `affinity include-all <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual-content evidence sufficient to verify that no matching command topic exists.
- Evidence `P00019:probe` (probe_template): affinity include-all <WORD>

#### F00023

- Status: unresolved
- Probe template: `affinity include-any`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual-content evidence sufficient to verify that no matching command topic exists.
- Evidence `P00020:probe` (probe_template): affinity include-any

#### F00024

- Status: unresolved
- Probe template: `affinity include-any <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual-content evidence sufficient to verify that no matching command topic exists.
- Evidence `P00021:probe` (probe_template): affinity include-any <WORD>

#### F00025

- Status: unresolved
- Probe template: `affinity-map`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe template but provides no supplied manual-command evidence to establish that no matching command topic exists.
- Evidence `P00022:probe` (probe_template): affinity-map

#### F00026

- Status: unresolved
- Probe template: `affinity-map <WORD> bit-position <0-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is evidenced, but the absence of a matching supplied manual topic cannot be verified from the provided evidence alone.
- Evidence `P00023:probe` (probe_template): affinity-map <WORD> bit-position <0-255>

#### F00027

- Status: unresolved
- Probe template: `ag`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence shows only the probe template; it does not support a determination that supplied manuals lack a corresponding command topic.
- Evidence `P00024:probe` (probe_template): ag

#### F00028

- Status: unresolved
- Probe template: `ag bit-position <0-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only and contains no manual-topic evidence sufficient to confirm undercoverage.
- Evidence `P00025:probe` (probe_template): ag bit-position <0-255>

#### F00029

- Status: unresolved
- Probe template: `ah`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "ah". It provides no supplied manual inventory or matching analysis to support the claimed absence of a corresponding command topic.
- Evidence `P00026:probe` (probe_template): ah

#### F00030

- Status: unresolved
- Probe template: `ah bit-position <0-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "ah bit-position <0-255>". It does not establish that the supplied manuals lack a matching command topic.
- Evidence `P00027:probe` (probe_template): ah bit-position <0-255>

#### F00031

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "apply-group <WORD>". No manual evidence is supplied to substantiate the asserted command undercoverage in the area semantic view.
- Evidence `P00028:probe` (probe_template): apply-group <WORD>

#### F00032

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "apply-group <WORD>". No manual evidence is supplied to substantiate the asserted command undercoverage in the interface semantic view.
- Evidence `P00029:probe` (probe_template): apply-group <WORD>

#### F00033

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not provide supplied manual content or command-topic coverage information needed to verify undercoverage for the multi-area view.
- Evidence `P00030:probe` (probe_template): apply-group <WORD>

#### F00034

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not provide supplied manual content or command-topic coverage information needed to verify undercoverage for the router view.
- Evidence `P00031:probe` (probe_template): apply-group <WORD>

#### F00035

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not provide supplied manual content or command-topic coverage information needed to verify undercoverage for the sham-link view.
- Evidence `P00032:probe` (probe_template): apply-group <WORD>

#### F00036

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not provide supplied manual content or command-topic coverage information needed to verify undercoverage for the unknown view.
- Evidence `P00033:probe` (probe_template): apply-group <WORD>

#### F00037

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify the claimed absence of a matching manual command.
- Evidence `P00034:probe` (probe_template): apply-group <WORD>

#### F00038

- Status: unresolved
- Probe template: `apply-group <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but does not support a determination that supplied manuals lack a matching command topic.
- Evidence `P00035:probe` (probe_template): apply-group <WORD>

#### F00039

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe template is evidenced, but there is no evidence of the manuals searched or their command-topic coverage to confirm undercoverage.
- Evidence `P00036:probe` (probe_template): apply-group-append <WORD>

#### F00040

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence identifies the probe template only and cannot verify that no corresponding command topic exists in the supplied manuals.
- Evidence `P00037:probe` (probe_template): apply-group-append <WORD>

#### F00041

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual content or coverage inventory to support the claimed absence of a matching command topic.
- Evidence `P00038:probe` (probe_template): apply-group-append <WORD>

#### F00042

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual content or coverage inventory to support the claimed absence of a matching command topic.
- Evidence `P00039:probe` (probe_template): apply-group-append <WORD>

#### F00043

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual content or coverage inventory to support the claimed absence of a matching command topic.
- Evidence `P00040:probe` (probe_template): apply-group-append <WORD>

#### F00044

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual content or coverage inventory to support the claimed absence of a matching command topic.
- Evidence `P00041:probe` (probe_template): apply-group-append <WORD>

#### F00045

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00042:probe` (probe_template): apply-group-append <WORD>

#### F00046

- Status: unresolved
- Probe template: `apply-group-append <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00043:probe` (probe_template): apply-group-append <WORD>

#### F00047

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00044:probe` (probe_template): apply-group-remove <WORD>

#### F00048

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00045:probe` (probe_template): apply-group-remove <WORD>

#### F00049

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00046:probe` (probe_template): apply-group-remove <WORD>

#### F00050

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00047:probe` (probe_template): apply-group-remove <WORD>

#### F00051

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00048:probe` (probe_template): apply-group-remove <WORD>

#### F00052

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00049:probe` (probe_template): apply-group-remove <WORD>

#### F00053

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template but supplies no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00050:probe` (probe_template): apply-group-remove <WORD>

#### F00054

- Status: unresolved
- Probe template: `apply-group-remove <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template but supplies no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00051:probe` (probe_template): apply-group-remove <WORD>

#### F00055

- Status: unresolved
- Probe template: `apply-weight bandwidth [<1-4294967>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template but supplies no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00052:probe` (probe_template): apply-weight bandwidth [<1-4294967>]

#### F00056

- Status: unresolved
- Probe template: `apply-weight bandwidth [<1-4294967>]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template but supplies no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00053:probe` (probe_template): apply-weight bandwidth [<1-4294967>]

#### F00057

- Status: unresolved
- Probe template: `apply-weight default-weight <1-16777214>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00054:probe` (probe_template): apply-weight default-weight <1-16777214>

#### F00058

- Status: unresolved
- Probe template: `apply-weight default-weight <1-16777214>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00055:probe` (probe_template): apply-weight default-weight <1-16777214>

#### F00059

- Status: unresolved
- Probe template: `area <A.B.C.D>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00056:probe` (probe_template): area <A.B.C.D>

#### F00060

- Status: unresolved
- Probe template: `area <0-4294967295>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe template. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00057:probe` (probe_template): area <0-4294967295>

#### F00061

- Status: unresolved
- Probe template: `authentication`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the authentication probe but provides no manual coverage evidence sufficient to verify that no matching command topic exists for the area view.
- Evidence `P00058:probe` (probe_template): authentication

#### F00062

- Status: unresolved
- Probe template: `authentication`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the authentication probe but provides no manual coverage evidence sufficient to verify that no matching command topic exists for the interface view.
- Evidence `P00059:probe` (probe_template): authentication

#### F00063

- Status: unresolved
- Probe template: `authentication`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the authentication probe but provides no manual coverage evidence sufficient to verify that no matching command topic exists for the multi-area view.
- Evidence `P00060:probe` (probe_template): authentication

#### F00064

- Status: unresolved
- Probe template: `authentication`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the authentication probe but provides no manual coverage evidence sufficient to verify that no matching command topic exists for the router view.
- Evidence `P00061:probe` (probe_template): authentication

#### F00065

- Status: unresolved
- Probe template: `authentication`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence identifies the probe template only; it does not establish the contents or coverage of the supplied manuals.
- Evidence `P00062:probe` (probe_template): authentication

#### F00066

- Status: unresolved
- Probe template: `authentication`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence identifies the probe template only; it does not establish the contents or coverage of the supplied manuals.
- Evidence `P00063:probe` (probe_template): authentication

#### F00067

- Status: unresolved
- Probe template: `authentication`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence identifies the probe template only; it does not establish the contents or coverage of the supplied manuals.
- Evidence `P00064:probe` (probe_template): authentication

#### F00068

- Status: unresolved
- Probe template: `authentication message-digest`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence identifies the probe template only; it does not establish the contents or coverage of the supplied manuals.
- Evidence `P00065:probe` (probe_template): authentication message-digest

#### F00069

- Status: unresolved
- Probe template: `authentication message-digest`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to support or refute the claimed absence of a matching manual command.
- Evidence `P00066:probe` (probe_template): authentication message-digest

#### F00070

- Status: unresolved
- Probe template: `authentication message-digest`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to support or refute the claimed absence of a matching manual command.
- Evidence `P00067:probe` (probe_template): authentication message-digest

#### F00071

- Status: unresolved
- Probe template: `authentication message-digest`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to support or refute the claimed absence of a matching manual command.
- Evidence `P00068:probe` (probe_template): authentication message-digest

#### F00072

- Status: unresolved
- Probe template: `authentication message-digest`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to support or refute the claimed absence of a matching manual command.
- Evidence `P00069:probe` (probe_template): authentication message-digest

#### F00073

- Status: unresolved
- Probe template: `authentication message-digest`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied-manual command topics or search results to support or refute the claimed undercoverage.
- Evidence `P00070:probe` (probe_template): authentication message-digest

#### F00074

- Status: unresolved
- Probe template: `authentication message-digest`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied-manual command topics or search results to support or refute the claimed undercoverage.
- Evidence `P00071:probe` (probe_template): authentication message-digest

#### F00075

- Status: unresolved
- Probe template: `authentication-key {clear LINE|encrypted LINE|LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied-manual command topics or search results to support or refute the claimed undercoverage.
- Evidence `P00072:probe` (probe_template): authentication-key {clear LINE|encrypted LINE|LINE}

#### F00076

- Status: unresolved
- Probe template: `authentication-key {clear LINE|encrypted LINE|LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It provides no supplied-manual command topics or search results to support or refute the claimed undercoverage.
- Evidence `P00073:probe` (probe_template): authentication-key {clear LINE|encrypted LINE|LINE}

#### F00077

- Status: unresolved
- Probe template: `authentication-key {clear LINE|encrypted LINE|LINE}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It provides no manual-command evidence or manual corpus coverage information to determine whether a matching topic exists.
- Evidence `P00074:probe` (probe_template): authentication-key {clear LINE|encrypted LINE|LINE}

#### F00078

- Status: unresolved
- Probe template: `authentication-key {clear LINE|encrypted LINE|LINE}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It provides no manual-command evidence or manual corpus coverage information to determine whether a matching topic exists.
- Evidence `P00075:probe` (probe_template): authentication-key {clear LINE|encrypted LINE|LINE}

#### F00079

- Status: unresolved
- Probe template: `authentication-key {clear LINE|LINE|encrypted LINE}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It provides no manual-command evidence or manual corpus coverage information to determine whether a matching topic exists.
- Evidence `P00076:probe` (probe_template): authentication-key {clear LINE|LINE|encrypted LINE}

#### F00080

- Status: unresolved
- Probe template: `authentication-key {clear LINE|LINE|encrypted LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It provides no manual-command evidence or manual corpus coverage information to determine whether a matching topic exists.
- Evidence `P00077:probe` (probe_template): authentication-key {clear LINE|LINE|encrypted LINE}

#### F00081

- Status: unresolved
- Probe template: `authentication-key {clear LINE|LINE|encrypted LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00078:probe` (probe_template): authentication-key {clear LINE|LINE|encrypted LINE}

#### F00082

- Status: unresolved
- Probe template: `authentication-key {clear LINE|LINE|encrypted LINE}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00079:probe` (probe_template): authentication-key {clear LINE|LINE|encrypted LINE}

#### F00083

- Status: unresolved
- Probe template: `authentication-key {encrypted LINE|clear LINE|LINE}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00080:probe` (probe_template): authentication-key {encrypted LINE|clear LINE|LINE}

#### F00084

- Status: unresolved
- Probe template: `authentication-key {encrypted LINE|clear LINE|LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00081:probe` (probe_template): authentication-key {encrypted LINE|clear LINE|LINE}

#### F00085

- Status: unresolved
- Probe template: `authentication-key {encrypted LINE|LINE|clear LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe command is evidenced, but there is no supplied manual evidence establishing whether a matching command topic is absent.
- Evidence `P00082:probe` (probe_template): authentication-key {encrypted LINE|LINE|clear LINE}

#### F00086

- Status: unresolved
- Probe template: `authentication-key {encrypted LINE|LINE|clear LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe command is evidenced, but there is no supplied manual evidence establishing whether a matching command topic is absent.
- Evidence `P00083:probe` (probe_template): authentication-key {encrypted LINE|LINE|clear LINE}

#### F00087

- Status: unresolved
- Probe template: `authentication-key {LINE|clear LINE|encrypted LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe command is evidenced, but there is no supplied manual evidence establishing whether a matching command topic is absent.
- Evidence `P00084:probe` (probe_template): authentication-key {LINE|clear LINE|encrypted LINE}

#### F00088

- Status: unresolved
- Probe template: `authentication-key {LINE|clear LINE|encrypted LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe command is evidenced, but there is no supplied manual evidence establishing whether a matching command topic is absent.
- Evidence `P00085:probe` (probe_template): authentication-key {LINE|clear LINE|encrypted LINE}

#### F00089

- Status: unresolved
- Probe template: `authentication-key {LINE|clear LINE|encrypted LINE}`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent for the sham-link view.
- Evidence `P00086:probe` (probe_template): authentication-key {LINE|clear LINE|encrypted LINE}

#### F00090

- Status: unresolved
- Probe template: `authentication-key {LINE|clear LINE|encrypted LINE}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent for the virtual-link view.
- Evidence `P00087:probe` (probe_template): authentication-key {LINE|clear LINE|encrypted LINE}

#### F00091

- Status: unresolved
- Probe template: `authentication-key {LINE|clear LINE|encrypted LINE}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent for the VRF view.
- Evidence `P00088:probe` (probe_template): authentication-key {LINE|clear LINE|encrypted LINE}

#### F00092

- Status: unresolved
- Probe template: `authentication-key {LINE|encrypted LINE|clear LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent for the interface view.
- Evidence `P00089:probe` (probe_template): authentication-key {LINE|encrypted LINE|clear LINE}

#### F00093

- Status: unresolved
- Probe template: `authentication-key {LINE|encrypted LINE|clear LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe command template. It contains no supplied manual inventory or command-topic evidence to support or refute the claimed absence of a matching manual command.
- Evidence `P00090:probe` (probe_template): authentication-key {LINE|encrypted LINE|clear LINE}

#### F00094

- Status: unresolved
- Probe template: `authentication-key {LINE|encrypted LINE|clear LINE}`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence shows the probe template but provides no manual-command evidence for the sham-link semantic view. The undercoverage claim cannot be decided.
- Evidence `P00091:probe` (probe_template): authentication-key {LINE|encrypted LINE|clear LINE}

#### F00095

- Status: unresolved
- Probe template: `authentication-key {LINE|encrypted LINE|clear LINE}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is evidenced, but there is no supplied manual evidence establishing whether a corresponding virtual-link command topic exists. The finding remains undecidable.
- Evidence `P00092:probe` (probe_template): authentication-key {LINE|encrypted LINE|clear LINE}

#### F00096

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|message-digest keychain <WORD>|null}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supports the existence of the probe template only. It does not provide manual-command coverage evidence for the area semantic view, so the asserted undercoverage cannot be confirmed or dismissed.
- Evidence `P00093:probe` (probe_template): authentication {keychain <WORD>|message-digest keychain <WORD>|null}

#### F00097

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|message-digest keychain <WORD>|null}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists for the interface view.
- Evidence `P00094:probe` (probe_template): authentication {keychain <WORD>|message-digest keychain <WORD>|null}

#### F00098

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|message-digest keychain <WORD>|null}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists for the multi-area view.
- Evidence `P00095:probe` (probe_template): authentication {keychain <WORD>|message-digest keychain <WORD>|null}

#### F00099

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|message-digest keychain <WORD>|null}`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists for the sham-link view.
- Evidence `P00096:probe` (probe_template): authentication {keychain <WORD>|message-digest keychain <WORD>|null}

#### F00100

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|message-digest keychain <WORD>|null}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists for the virtual-link view.
- Evidence `P00097:probe` (probe_template): authentication {keychain <WORD>|message-digest keychain <WORD>|null}

#### F00101

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|null|message-digest keychain <WORD>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists for the interface view.
- Evidence `P00098:probe` (probe_template): authentication {keychain <WORD>|null|message-digest keychain <WORD>}

#### F00102

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|null|message-digest keychain <WORD>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists for the multi-area view.
- Evidence `P00099:probe` (probe_template): authentication {keychain <WORD>|null|message-digest keychain <WORD>}

#### F00103

- Status: unresolved
- Probe template: `authentication {keychain <WORD>|null|message-digest keychain <WORD>}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists for the virtual-link view.
- Evidence `P00100:probe` (probe_template): authentication {keychain <WORD>|null|message-digest keychain <WORD>}

#### F00104

- Status: unresolved
- Probe template: `authentication {message-digest keychain <WORD>|keychain <WORD>|null}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists for the interface view.
- Evidence `P00101:probe` (probe_template): authentication {message-digest keychain <WORD>|keychain <WORD>|null}

#### F00105

- Status: unresolved
- Probe template: `authentication {message-digest keychain <WORD>|keychain <WORD>|null}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template but provides no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00102:probe` (probe_template): authentication {message-digest keychain <WORD>|keychain <WORD>|null}

#### F00106

- Status: unresolved
- Probe template: `authentication {message-digest keychain <WORD>|null|keychain <WORD>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template but provides no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00103:probe` (probe_template): authentication {message-digest keychain <WORD>|null|keychain <WORD>}

#### F00107

- Status: unresolved
- Probe template: `authentication {message-digest keychain <WORD>|null|keychain <WORD>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template but provides no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00104:probe` (probe_template): authentication {message-digest keychain <WORD>|null|keychain <WORD>}

#### F00108

- Status: unresolved
- Probe template: `authentication {message-digest keychain <WORD>|null|keychain <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template but provides no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00105:probe` (probe_template): authentication {message-digest keychain <WORD>|null|keychain <WORD>}

#### F00109

- Status: unresolved
- Probe template: `authentication {message-digest keychain <WORD>|null|keychain <WORD>}`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence from which to determine whether a matching command topic exists for the sham-link view.
- Evidence `P00106:probe` (probe_template): authentication {message-digest keychain <WORD>|null|keychain <WORD>}

#### F00110

- Status: unresolved
- Probe template: `authentication {message-digest keychain <WORD>|null|keychain <WORD>}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence from which to determine whether a matching command topic exists for the virtual-link view.
- Evidence `P00107:probe` (probe_template): authentication {message-digest keychain <WORD>|null|keychain <WORD>}

#### F00111

- Status: unresolved
- Probe template: `authentication {null|keychain <WORD>|message-digest keychain <WORD>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence from which to determine whether a matching command topic exists for the area view.
- Evidence `P00108:probe` (probe_template): authentication {null|keychain <WORD>|message-digest keychain <WORD>}

#### F00112

- Status: unresolved
- Probe template: `authentication {null|keychain <WORD>|message-digest keychain <WORD>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence from which to determine whether a matching command topic exists for the interface view.
- Evidence `P00109:probe` (probe_template): authentication {null|keychain <WORD>|message-digest keychain <WORD>}

#### F00113

- Status: unresolved
- Probe template: `authentication {null|keychain <WORD>|message-digest keychain <WORD>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template, but provides no manual content or command-topic evidence to verify that no supplied manual matches it.
- Evidence `P00110:probe` (probe_template): authentication {null|keychain <WORD>|message-digest keychain <WORD>}

#### F00114

- Status: unresolved
- Probe template: `authentication {null|keychain <WORD>|message-digest keychain <WORD>}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template, but provides no manual content or command-topic evidence to verify that no supplied manual matches it.
- Evidence `P00111:probe` (probe_template): authentication {null|keychain <WORD>|message-digest keychain <WORD>}

#### F00115

- Status: unresolved
- Probe template: `authentication {null|message-digest keychain <WORD>|keychain <WORD>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template, but provides no manual content or command-topic evidence to verify that no supplied manual matches it.
- Evidence `P00112:probe` (probe_template): authentication {null|message-digest keychain <WORD>|keychain <WORD>}

#### F00116

- Status: unresolved
- Probe template: `authentication {null|message-digest keychain <WORD>|keychain <WORD>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template, but provides no manual content or command-topic evidence to verify that no supplied manual matches it.
- Evidence `P00113:probe` (probe_template): authentication {null|message-digest keychain <WORD>|keychain <WORD>}

#### F00117

- Status: unresolved
- Probe template: `authentication {null|message-digest keychain <WORD>|keychain <WORD>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content with which to verify absence of a matching command topic.
- Evidence `P00114:probe` (probe_template): authentication {null|message-digest keychain <WORD>|keychain <WORD>}

#### F00118

- Status: unresolved
- Probe template: `auto-cost {disable|reference-bandwidth <1-4294967>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content with which to verify absence of a matching command topic.
- Evidence `P00115:probe` (probe_template): auto-cost {disable|reference-bandwidth <1-4294967>}

#### F00119

- Status: unresolved
- Probe template: `auto-cost {reference-bandwidth <1-4294967>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content with which to verify absence of a matching command topic.
- Evidence `P00116:probe` (probe_template): auto-cost {reference-bandwidth <1-4294967>|disable}

#### F00120

- Status: unresolved
- Probe template: `aya bit-position <0-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content with which to verify absence of a matching command topic.
- Evidence `P00117:probe` (probe_template): aya bit-position <0-255>

#### F00121

- Status: unresolved
- Probe template: `bfd fast-detect [disable|strict-mode]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but provides no supplied manual content or command inventory to verify that no matching manual topic exists.
- Evidence `P00118:probe` (probe_template): bfd fast-detect [disable|strict-mode]

#### F00122

- Status: unresolved
- Probe template: `bfd fast-detect [disable|strict-mode]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but provides no supplied manual content or command inventory to verify that no matching manual topic exists.
- Evidence `P00119:probe` (probe_template): bfd fast-detect [disable|strict-mode]

#### F00123

- Status: unresolved
- Probe template: `bfd fast-detect [strict-mode]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but provides no supplied manual content or command inventory to verify that no matching manual topic exists.
- Evidence `P00120:probe` (probe_template): bfd fast-detect [strict-mode]

#### F00124

- Status: unresolved
- Probe template: `bfd fast-detect [strict-mode]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but provides no supplied manual content or command inventory to verify that no matching manual topic exists.
- Evidence `P00121:probe` (probe_template): bfd fast-detect [strict-mode]

#### F00125

- Status: unresolved
- Probe template: `bfd fast-detect [strict-mode|disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence to verify that no matching command topic exists.
- Evidence `P00122:probe` (probe_template): bfd fast-detect [strict-mode|disable]

#### F00126

- Status: unresolved
- Probe template: `bfd fast-detect [strict-mode|disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence to verify that no matching command topic exists in the interface view.
- Evidence `P00123:probe` (probe_template): bfd fast-detect [strict-mode|disable]

#### F00127

- Status: unresolved
- Probe template: `bfd {minimum-interval <50-30000>|multiplier <3-50>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence to verify that no matching command topic exists in the interface view.
- Evidence `P00124:probe` (probe_template): bfd {minimum-interval <50-30000>|multiplier <3-50>}

#### F00128

- Status: unresolved
- Probe template: `bfd {minimum-interval <50-30000>|multiplier <3-50>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence to verify that no matching command topic exists in the router view.
- Evidence `P00125:probe` (probe_template): bfd {minimum-interval <50-30000>|multiplier <3-50>}

#### F00129

- Status: unresolved
- Probe template: `bfd {minimum-interval <50-30000>|multiplier <3-50>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only; it does not provide manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00126:probe` (probe_template): bfd {minimum-interval <50-30000>|multiplier <3-50>}

#### F00130

- Status: unresolved
- Probe template: `bfd {multiplier <3-50>|minimum-interval <50-30000>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is supplied, but no manual excerpts, index, or command-coverage evidence is available to support or refute the claimed undercoverage.
- Evidence `P00127:probe` (probe_template): bfd {multiplier <3-50>|minimum-interval <50-30000>}

#### F00131

- Status: unresolved
- Probe template: `bfd {multiplier <3-50>|minimum-interval <50-30000>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the interface-context probe but cannot establish whether supplied manuals contain a matching command topic.
- Evidence `P00128:probe` (probe_template): bfd {multiplier <3-50>|minimum-interval <50-30000>}

#### F00132

- Status: unresolved
- Probe template: `capability {lls disable|opaque disable|type7 prefer}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The capability probe is evidenced, but there is no supplied manual evidence from which to determine whether a corresponding topic is absent.
- Evidence `P00129:probe` (probe_template): capability {lls disable|opaque disable|type7 prefer}

#### F00133

- Status: unresolved
- Probe template: `capability {vrf-lite|opaque disable|lls disable|type7 prefer}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00130:probe` (probe_template): capability {vrf-lite|opaque disable|lls disable|type7 prefer}

#### F00134

- Status: unresolved
- Probe template: `cost <1-65535>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is evidenced, but the claimed absence of a matching manual topic cannot be determined without manual evidence or coverage results.
- Evidence `P00131:probe` (probe_template): cost <1-65535>

#### F00135

- Status: unresolved
- Probe template: `cost <1-65535>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supports only the interface-scoped probe template; it does not support or refute the asserted manual undercoverage.
- Evidence `P00132:probe` (probe_template): cost <1-65535>

#### F00136

- Status: unresolved
- Probe template: `cost <1-65535>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The multi-area probe template is present, but there is no manual evidence to establish whether a corresponding command topic is absent.
- Evidence `P00133:probe` (probe_template): cost <1-65535>

#### F00137

- Status: unresolved
- Probe template: `cost <1-65535>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or coverage comparison to support or refute the claimed absence of a matching command topic.
- Evidence `P00134:probe` (probe_template): cost <1-65535>

#### F00138

- Status: unresolved
- Probe template: `cost <1-65535>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or coverage comparison to support or refute the claimed absence of a matching command topic.
- Evidence `P00135:probe` (probe_template): cost <1-65535>

#### F00139

- Status: unresolved
- Probe template: `cost <1-65535>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or coverage comparison to support or refute the claimed absence of a matching command topic.
- Evidence `P00136:probe` (probe_template): cost <1-65535>

#### F00140

- Status: unresolved
- Probe template: `cost-fallback <1-65535> threshold <1-4294967>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or coverage comparison to support or refute the claimed absence of a matching command topic.
- Evidence `P00137:probe` (probe_template): cost-fallback <1-65535> threshold <1-4294967>

#### F00141

- Status: unresolved
- Probe template: `cost-fallback <1-65535> threshold <1-4294967>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe command template, but provides no manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00138:probe` (probe_template): cost-fallback <1-65535> threshold <1-4294967>

#### F00142

- Status: unresolved
- Probe template: `cost-fallback anomaly delay igp-metric {increment <1-65534>|value <1-65535>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The probe template is evidenced, but absence of a matching command topic cannot be confirmed without supplied manual-search or manual-content evidence.
- Evidence `P00139:probe` (probe_template): cost-fallback anomaly delay igp-metric {increment <1-65534>|value <1-65535>}

#### F00143

- Status: unresolved
- Probe template: `cost-fallback anomaly delay igp-metric {increment <1-65534>|value <1-65535>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence supports only the interface-context probe template; it does not support the claimed lack of matching manual coverage.
- Evidence `P00140:probe` (probe_template): cost-fallback anomaly delay igp-metric {increment <1-65534>|value <1-65535>}

#### F00144

- Status: unresolved
- Probe template: `cost-fallback anomaly delay igp-metric {value <1-65535>|increment <1-65534>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence identifies the probe template but does not demonstrate that the applicable manuals contain no matching command topic.
- Evidence `P00141:probe` (probe_template): cost-fallback anomaly delay igp-metric {value <1-65535>|increment <1-65534>}

#### F00145

- Status: unresolved
- Probe template: `cost-fallback anomaly delay igp-metric {value <1-65535>|increment <1-65534>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-command coverage or evidence that no matching manual topic exists.
- Evidence `P00142:probe` (probe_template): cost-fallback anomaly delay igp-metric {value <1-65535>|increment <1-65534>}

#### F00146

- Status: unresolved
- Probe template: `cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-command coverage or evidence that no matching manual topic exists.
- Evidence `P00143:probe` (probe_template): cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}

#### F00147

- Status: unresolved
- Probe template: `cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-command coverage or evidence that no matching manual topic exists.
- Evidence `P00144:probe` (probe_template): cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}

#### F00148

- Status: unresolved
- Probe template: `cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-command coverage or evidence that no matching manual topic exists.
- Evidence `P00145:probe` (probe_template): cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}

#### F00149

- Status: unresolved
- Probe template: `cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It does not provide manual content or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00146:probe` (probe_template): cost-fallback anomaly delay te-metric {increment <1-4294967294>|value <1-4294967295>}

#### F00150

- Status: unresolved
- Probe template: `cost-fallback anomaly delay te-metric {value <1-4294967295>|increment <1-4294967294>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It does not provide manual content or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00147:probe` (probe_template): cost-fallback anomaly delay te-metric {value <1-4294967295>|increment <1-4294967294>}

#### F00151

- Status: unresolved
- Probe template: `cost-fallback anomaly delay te-metric {value <1-4294967295>|increment <1-4294967294>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It does not provide manual content or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00148:probe` (probe_template): cost-fallback anomaly delay te-metric {value <1-4294967295>|increment <1-4294967294>}

#### F00152

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {disable|increment <1-65534>|value <1-65535>|multiplier <1-255>}|te-metric {disable|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command only. It does not provide manual content or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00149:probe` (probe_template): cost-fallback anomaly delay {igp-metric {disable|increment <1-65534>|value <1-65535>|multiplier <1-255>}|te-metric {disable|multiplier <1-255>}}

#### F00153

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {disable|multiplier <1-255>}|te-metric {increment <1-4294967294>|value <1-4294967295>|disable|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only; it provides no manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00150:probe` (probe_template): cost-fallback anomaly delay {igp-metric {disable|multiplier <1-255>}|te-metric {increment <1-4294967294>|value <1-4294967295>|disable|multiplier <1-255>}}

#### F00154

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {disable|value <1-65535>|multiplier <1-255>|increment <1-65534>}|te-metric {disable|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only; it provides no manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00151:probe` (probe_template): cost-fallback anomaly delay {igp-metric {disable|value <1-65535>|multiplier <1-255>|increment <1-65534>}|te-metric {disable|multiplier <1-255>}}

#### F00155

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {increment <1-65534>|disable|value <1-65535>|multiplier <1-255>}|te-metric {disable|multiplier <1-255>}}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only; it provides no manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00152:probe` (probe_template): cost-fallback anomaly delay {igp-metric {increment <1-65534>|disable|value <1-65535>|multiplier <1-255>}|te-metric {disable|multiplier <1-255>}}

#### F00156

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {increment <1-65534>|disable|value <1-65535>|multiplier <1-255>}|te-metric {disable|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only; it provides no manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00153:probe` (probe_template): cost-fallback anomaly delay {igp-metric {increment <1-65534>|disable|value <1-65535>|multiplier <1-255>}|te-metric {disable|multiplier <1-255>}}

#### F00157

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {increment <1-65534>|value <1-65535>|multiplier <1-255>}|te-metric multiplier <1-255>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but supplies no manual content or coverage inventory that can substantiate absence of a matching command topic.
- Evidence `P00154:probe` (probe_template): cost-fallback anomaly delay {igp-metric {increment <1-65534>|value <1-65535>|multiplier <1-255>}|te-metric multiplier <1-255>}

#### F00158

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {multiplier <1-255>|disable|increment <1-65534>|value <1-65535>}|te-metric {multiplier <1-255>|disable}}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but supplies no manual content or coverage inventory that can substantiate absence of a matching command topic.
- Evidence `P00155:probe` (probe_template): cost-fallback anomaly delay {igp-metric {multiplier <1-255>|disable|increment <1-65534>|value <1-65535>}|te-metric {multiplier <1-255>|disable}}

#### F00159

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {multiplier <1-255>|disable}|te-metric {multiplier <1-255>|disable|increment <1-4294967294>|value <1-4294967295>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but supplies no manual content or coverage inventory that can substantiate absence of a matching command topic.
- Evidence `P00156:probe` (probe_template): cost-fallback anomaly delay {igp-metric {multiplier <1-255>|disable}|te-metric {multiplier <1-255>|disable|increment <1-4294967294>|value <1-4294967295>}}

#### F00160

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {multiplier <1-255>|disable}|te-metric {multiplier <1-255>|increment <1-4294967294>|value <1-4294967295>|disable}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but supplies no manual content or coverage inventory that can substantiate absence of a matching command topic.
- Evidence `P00157:probe` (probe_template): cost-fallback anomaly delay {igp-metric {multiplier <1-255>|disable}|te-metric {multiplier <1-255>|increment <1-4294967294>|value <1-4294967295>|disable}}

#### F00161

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {multiplier <1-255>|increment <1-65534>|value <1-65535>}|te-metric multiplier <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command only; it does not establish that the supplied manuals contain no matching command topic.
- Evidence `P00158:probe` (probe_template): cost-fallback anomaly delay {igp-metric {multiplier <1-255>|increment <1-65534>|value <1-65535>}|te-metric multiplier <1-255>}

#### F00162

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {igp-metric {multiplier <1-255>|value <1-65535>|increment <1-65534>|disable}|te-metric {multiplier <1-255>|disable}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command only; it does not establish that the supplied manuals contain no matching command topic.
- Evidence `P00159:probe` (probe_template): cost-fallback anomaly delay {igp-metric {multiplier <1-255>|value <1-65535>|increment <1-65534>|disable}|te-metric {multiplier <1-255>|disable}}

#### F00163

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>|increment <1-4294967294>|value <1-4294967295>}|igp-metric {disable|multiplier <1-255>}}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command only; it does not establish that the supplied manuals contain no matching command topic.
- Evidence `P00160:probe` (probe_template): cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>|increment <1-4294967294>|value <1-4294967295>}|igp-metric {disable|multiplier <1-255>}}

#### F00164

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {disable|value <1-65535>|increment <1-65534>|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command only; it does not establish that the supplied manuals contain no matching command topic.
- Evidence `P00161:probe` (probe_template): cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {disable|value <1-65535>|increment <1-65534>|multiplier <1-255>}}

#### F00165

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {disable|value <1-65535>|multiplier <1-255>|increment <1-65534>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual corpus or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00162:probe` (probe_template): cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {disable|value <1-65535>|multiplier <1-255>|increment <1-65534>}}

#### F00166

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {value <1-65535>|disable|increment <1-65534>|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual corpus or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00163:probe` (probe_template): cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {value <1-65535>|disable|increment <1-65534>|multiplier <1-255>}}

#### F00167

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {value <1-65535>|increment <1-65534>|disable|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual corpus or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00164:probe` (probe_template): cost-fallback anomaly delay {te-metric {disable|multiplier <1-255>}|igp-metric {value <1-65535>|increment <1-65534>|disable|multiplier <1-255>}}

#### F00168

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {increment <1-4294967294>|disable|value <1-4294967295>|multiplier <1-255>}|igp-metric {disable|multiplier <1-255>}}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual corpus or coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00165:probe` (probe_template): cost-fallback anomaly delay {te-metric {increment <1-4294967294>|disable|value <1-4294967295>|multiplier <1-255>}|igp-metric {disable|multiplier <1-255>}}

#### F00169

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {increment <1-4294967294>|multiplier <1-255>|disable|value <1-4294967295>}|igp-metric {multiplier <1-255>|disable}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00166:probe` (probe_template): cost-fallback anomaly delay {te-metric {increment <1-4294967294>|multiplier <1-255>|disable|value <1-4294967295>}|igp-metric {multiplier <1-255>|disable}}

#### F00170

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {multiplier <1-255>|disable}|igp-metric {increment <1-65534>|multiplier <1-255>|disable|value <1-65535>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00167:probe` (probe_template): cost-fallback anomaly delay {te-metric {multiplier <1-255>|disable}|igp-metric {increment <1-65534>|multiplier <1-255>|disable|value <1-65535>}}

#### F00171

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {multiplier <1-255>|increment <1-4294967294>|disable|value <1-4294967295>}|igp-metric {multiplier <1-255>|disable}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00168:probe` (probe_template): cost-fallback anomaly delay {te-metric {multiplier <1-255>|increment <1-4294967294>|disable|value <1-4294967295>}|igp-metric {multiplier <1-255>|disable}}

#### F00172

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {multiplier <1-255>|value <1-4294967295>|increment <1-4294967294>|disable}|igp-metric {multiplier <1-255>|disable}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00169:probe` (probe_template): cost-fallback anomaly delay {te-metric {multiplier <1-255>|value <1-4294967295>|increment <1-4294967294>|disable}|igp-metric {multiplier <1-255>|disable}}

#### F00173

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {value <1-4294967295>|disable|increment <1-4294967294>|multiplier <1-255>}|igp-metric {disable|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent.
- Evidence `P00170:probe` (probe_template): cost-fallback anomaly delay {te-metric {value <1-4294967295>|disable|increment <1-4294967294>|multiplier <1-255>}|igp-metric {disable|multiplier <1-255>}}

#### F00174

- Status: unresolved
- Probe template: `cost-fallback anomaly delay {te-metric {value <1-4294967295>|increment <1-4294967294>|disable|multiplier <1-255>}|igp-metric {disable|multiplier <1-255>}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent.
- Evidence `P00171:probe` (probe_template): cost-fallback anomaly delay {te-metric {value <1-4294967295>|increment <1-4294967294>|disable|multiplier <1-255>}|igp-metric {disable|multiplier <1-255>}}

#### F00175

- Status: unresolved
- Probe template: `database-filter all out [disable|enable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent for the area semantic view.
- Evidence `P00172:probe` (probe_template): database-filter all out [disable|enable]

#### F00176

- Status: unresolved
- Probe template: `database-filter all out [disable|enable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent for the interface semantic view.
- Evidence `P00173:probe` (probe_template): database-filter all out [disable|enable]

#### F00177

- Status: unresolved
- Probe template: `database-filter all out [disable|enable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only. It provides no supplied manual corpus or command-topic evidence from which to verify the claimed absence of a matching topic.
- Evidence `P00174:probe` (probe_template): database-filter all out [disable|enable]

#### F00178

- Status: unresolved
- Probe template: `database-filter all out [disable|enable]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only. It provides no supplied manual corpus or command-topic evidence from which to verify the claimed absence of a matching topic.
- Evidence `P00175:probe` (probe_template): database-filter all out [disable|enable]

#### F00179

- Status: unresolved
- Probe template: `database-filter all out [enable|disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only. It provides no supplied manual corpus or command-topic evidence from which to verify the claimed absence of a matching topic.
- Evidence `P00176:probe` (probe_template): database-filter all out [enable|disable]

#### F00180

- Status: unresolved
- Probe template: `database-filter all out [enable|disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only. It provides no supplied manual corpus or command-topic evidence from which to verify the claimed absence of a matching topic.
- Evidence `P00177:probe` (probe_template): database-filter all out [enable|disable]

#### F00181

- Status: unresolved
- Probe template: `database-filter all out [enable|disable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but does not establish that the supplied manuals lack a matching command topic.
- Evidence `P00178:probe` (probe_template): database-filter all out [enable|disable]

#### F00182

- Status: unresolved
- Probe template: `database-filter all out [enable|disable]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but does not establish that the supplied manuals lack a matching command topic for the VRF view.
- Evidence `P00179:probe` (probe_template): database-filter all out [enable|disable]

#### F00183

- Status: unresolved
- Probe template: `dead-interval`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no manual-content evidence to verify command undercoverage for the sham-link view.
- Evidence `P00180:probe` (probe_template): dead-interval

#### F00184

- Status: unresolved
- Probe template: `dead-interval`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no manual-content evidence to verify command undercoverage for the virtual-link view.
- Evidence `P00181:probe` (probe_template): dead-interval

#### F00185

- Status: unresolved
- Probe template: `dead-interval {<1-65535>|minimal hello-multiplier <3-20>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage results to support the claimed absence of a matching command topic for the area view.
- Evidence `P00182:probe` (probe_template): dead-interval {<1-65535>|minimal hello-multiplier <3-20>}

#### F00186

- Status: unresolved
- Probe template: `dead-interval {<1-65535>|minimal hello-multiplier <3-20>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage results to support the claimed absence of a matching command topic for the interface view.
- Evidence `P00183:probe` (probe_template): dead-interval {<1-65535>|minimal hello-multiplier <3-20>}

#### F00187

- Status: unresolved
- Probe template: `dead-interval {<1-65535>|minimal hello-multiplier <3-20>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage results to support the claimed absence of a matching command topic for the multi-area view.
- Evidence `P00184:probe` (probe_template): dead-interval {<1-65535>|minimal hello-multiplier <3-20>}

#### F00188

- Status: unresolved
- Probe template: `dead-interval {<1-65535>|minimal hello-multiplier <3-20>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage results to support the claimed absence of a matching command topic for the router view.
- Evidence `P00185:probe` (probe_template): dead-interval {<1-65535>|minimal hello-multiplier <3-20>}

#### F00189

- Status: unresolved
- Probe template: `dead-interval {<1-65535>|minimal hello-multiplier <3-20>}`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but it provides no manual-command coverage evidence to verify that no matching command topic exists for the sham-link view.
- Evidence `P00186:probe` (probe_template): dead-interval {<1-65535>|minimal hello-multiplier <3-20>}

#### F00190

- Status: unresolved
- Probe template: `dead-interval {<1-65535>|minimal hello-multiplier <3-20>}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but it provides no manual-command coverage evidence to verify that no matching command topic exists for the virtual-link view.
- Evidence `P00187:probe` (probe_template): dead-interval {<1-65535>|minimal hello-multiplier <3-20>}

#### F00191

- Status: unresolved
- Probe template: `dead-interval {<1-65535>|minimal hello-multiplier <3-20>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but it provides no manual-command coverage evidence to verify that no matching command topic exists for the VRF view.
- Evidence `P00188:probe` (probe_template): dead-interval {<1-65535>|minimal hello-multiplier <3-20>}

#### F00192

- Status: unresolved
- Probe template: `dead-interval {minimal hello-multiplier <3-20>|<1-65535>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template, but it provides no manual-command coverage evidence to verify that no matching command topic exists for the area view.
- Evidence `P00189:probe` (probe_template): dead-interval {minimal hello-multiplier <3-20>|<1-65535>}

#### F00193

- Status: unresolved
- Probe template: `dead-interval {minimal hello-multiplier <3-20>|<1-65535>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template; it provides no manual-command evidence to verify that no matching topic exists.
- Evidence `P00190:probe` (probe_template): dead-interval {minimal hello-multiplier <3-20>|<1-65535>}

#### F00194

- Status: unresolved
- Probe template: `dead-interval {minimal hello-multiplier <3-20>|<1-65535>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template; it provides no manual-command evidence to verify that no matching topic exists for the multi-area view.
- Evidence `P00191:probe` (probe_template): dead-interval {minimal hello-multiplier <3-20>|<1-65535>}

#### F00195

- Status: unresolved
- Probe template: `dead-interval {minimal hello-multiplier <3-20>|<1-65535>}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template; it provides no manual-command evidence to verify that no matching topic exists for the virtual-link view.
- Evidence `P00192:probe` (probe_template): dead-interval {minimal hello-multiplier <3-20>|<1-65535>}

#### F00196

- Status: unresolved
- Probe template: `default-cost <1-16777215>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template; it provides no manual-command evidence to verify that no matching topic exists for the area view.
- Evidence `P00193:probe` (probe_template): default-cost <1-16777215>

#### F00197

- Status: unresolved
- Probe template: `default-information originate [always|metric-type <1-2>|metric <1-16777214>|route-policy <WORD>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00194:probe` (probe_template): default-information originate [always|metric-type <1-2>|metric <1-16777214>|route-policy <WORD>]

#### F00198

- Status: unresolved
- Probe template: `default-information originate [metric <1-16777214>|metric-type <1-2>|route-policy <WORD>|always]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00195:probe` (probe_template): default-information originate [metric <1-16777214>|metric-type <1-2>|route-policy <WORD>|always]

#### F00199

- Status: unresolved
- Probe template: `default-metric <1-16777214>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00196:probe` (probe_template): default-metric <1-16777214>

#### F00200

- Status: unresolved
- Probe template: `default-metric <1-16777214>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual-command evidence from which to verify that no supplied manual topic matches it.
- Evidence `P00197:probe` (probe_template): default-metric <1-16777214>

#### F00201

- Status: unresolved
- Probe template: `delay normalize interval <1-16777215> [offset <0-16777215>]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes only the probe command template. It does not provide manual content or coverage results sufficient to verify that no matching command topic exists for the area view.
- Evidence `P00198:probe` (probe_template): delay normalize interval <1-16777215> [offset <0-16777215>]

#### F00202

- Status: unresolved
- Probe template: `delay normalize interval <1-16777215> [offset <0-16777215>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes only the probe command template. It does not provide manual content or coverage results sufficient to verify that no matching command topic exists for the interface view.
- Evidence `P00199:probe` (probe_template): delay normalize interval <1-16777215> [offset <0-16777215>]

#### F00203

- Status: unresolved
- Probe template: `delay normalize interval <1-16777215> [offset <0-16777215>]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes only the probe command template. It does not provide manual content or coverage results sufficient to verify that no matching command topic exists for the multi-area view.
- Evidence `P00200:probe` (probe_template): delay normalize interval <1-16777215> [offset <0-16777215>]

#### F00204

- Status: unresolved
- Probe template: `delay normalize interval <1-16777215> [offset <0-16777215>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes only the probe command template. It does not provide manual content or coverage results sufficient to verify that no matching command topic exists for the router view.
- Evidence `P00201:probe` (probe_template): delay normalize interval <1-16777215> [offset <0-16777215>]

#### F00205

- Status: unresolved
- Probe template: `delay normalize interval <1-16777215> [offset <0-16777215>]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template, but supplies no manual-content evidence to verify that no matching command topic exists.
- Evidence `P00202:probe` (probe_template): delay normalize interval <1-16777215> [offset <0-16777215>]

#### F00206

- Status: unresolved
- Probe template: `demand-circuit`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but does not provide manual evidence supporting the asserted absence of a matching topic.
- Evidence `P00203:probe` (probe_template): demand-circuit

#### F00207

- Status: unresolved
- Probe template: `demand-circuit`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe command is evidenced, but the supplied evidence cannot establish undercoverage in the interface semantic view.
- Evidence `P00204:probe` (probe_template): demand-circuit

#### F00208

- Status: unresolved
- Probe template: `demand-circuit`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe command is evidenced, but there is no supplied manual-content evidence to determine whether a matching router-level topic exists.
- Evidence `P00205:probe` (probe_template): demand-circuit

#### F00209

- Status: unresolved
- Probe template: `demand-circuit`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-topic inventory to verify that no matching manual command exists.
- Evidence `P00206:probe` (probe_template): demand-circuit

#### F00210

- Status: unresolved
- Probe template: `demand-circuit {disable|enable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is evidenced, but absence of a matching command topic cannot be determined without manual evidence or a documented manual-command inventory.
- Evidence `P00207:probe` (probe_template): demand-circuit {disable|enable}

#### F00211

- Status: unresolved
- Probe template: `demand-circuit {disable|enable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the interface-scoped probe template only; it does not support or refute the claimed lack of corresponding manual coverage.
- Evidence `P00208:probe` (probe_template): demand-circuit {disable|enable}

#### F00212

- Status: unresolved
- Probe template: `demand-circuit {disable|enable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is present, but no manual evidence is supplied from which to confirm that the VRF command lacks a matching command topic.
- Evidence `P00209:probe` (probe_template): demand-circuit {disable|enable}

#### F00213

- Status: unresolved
- Probe template: `demand-circuit {enable|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual corpus or command-topic evidence to verify the claimed absence of a matching manual command in the area view.
- Evidence `P00210:probe` (probe_template): demand-circuit {enable|disable}

#### F00214

- Status: unresolved
- Probe template: `demand-circuit {enable|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but does not establish that no matching command topic exists in the supplied manuals for the interface view.
- Evidence `P00211:probe` (probe_template): demand-circuit {enable|disable}

#### F00215

- Status: unresolved
- Probe template: `demand-circuit {enable|disable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but lacks manual-command evidence sufficient to determine whether the router-view undercoverage claim is correct.
- Evidence `P00212:probe` (probe_template): demand-circuit {enable|disable}

#### F00216

- Status: unresolved
- Probe template: `disable-dn-bit-check`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but contains no manual corpus or command-topic evidence to substantiate its claimed absence for the VRF view.
- Evidence `P00213:probe` (probe_template): disable-dn-bit-check

#### F00217

- Status: unresolved
- Probe template: `distance <1-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to substantiate that no matching manual command exists.
- Evidence `P00214:probe` (probe_template): distance <1-255>

#### F00218

- Status: unresolved
- Probe template: `distance <1-255>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to substantiate that no matching manual command exists.
- Evidence `P00215:probe` (probe_template): distance <1-255>

#### F00219

- Status: unresolved
- Probe template: `distance <1-255> <A.B.C.D> <A.B.C.D> [<WORD>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to substantiate that no matching manual command exists.
- Evidence `P00216:probe` (probe_template): distance <1-255> <A.B.C.D> <A.B.C.D> [<WORD>]

#### F00220

- Status: unresolved
- Probe template: `distance <1-255> <A.B.C.D> <A.B.C.D> [<WORD>]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to substantiate that no matching manual command exists.
- Evidence `P00217:probe` (probe_template): distance <1-255> <A.B.C.D> <A.B.C.D> [<WORD>]

#### F00221

- Status: unresolved
- Probe template: `distance ospf {external <1-255>|inter-area <1-255>|intra-area <1-255>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence or manual corpus content to verify that no matching command topic exists.
- Evidence `P00218:probe` (probe_template): distance ospf {external <1-255>|inter-area <1-255>|intra-area <1-255>}

#### F00222

- Status: unresolved
- Probe template: `distance ospf {intra-area <1-255>|external <1-255>|inter-area <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence or manual corpus content to verify that no matching command topic exists.
- Evidence `P00219:probe` (probe_template): distance ospf {intra-area <1-255>|external <1-255>|inter-area <1-255>}

#### F00223

- Status: unresolved
- Probe template: `distribute bgp-ls [excl-external]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence or manual corpus content to verify that no matching command topic exists.
- Evidence `P00220:probe` (probe_template): distribute bgp-ls [excl-external]

#### F00224

- Status: unresolved
- Probe template: `distribute link-state {disable|excl-nssa|excl-summary}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes only the probe command. It provides no manual-command evidence or manual corpus content to verify that no matching command topic exists.
- Evidence `P00221:probe` (probe_template): distribute link-state {disable|excl-nssa|excl-summary}

#### F00225

- Status: unresolved
- Probe template: `distribute link-state {excl-nssa|disable|excl-summary}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual evidence to verify that no matching command topic exists.
- Evidence `P00222:probe` (probe_template): distribute link-state {excl-nssa|disable|excl-summary}

#### F00226

- Status: unresolved
- Probe template: `distribute-list <WORD> in`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe command is evidenced, but the supplied evidence does not establish absence of a matching command topic in the manuals.
- Evidence `P00223:probe` (probe_template): distribute-list <WORD> in

#### F00227

- Status: unresolved
- Probe template: `distribute-list <WORD> in`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe command and view only; it contains no manual evidence supporting the asserted undercoverage.
- Evidence `P00224:probe` (probe_template): distribute-list <WORD> in

#### F00228

- Status: unresolved
- Probe template: `distribute-list <WORD> out`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied probe evidence cannot substantiate the claim that the manuals lack a matching command topic.
- Evidence `P00225:probe` (probe_template): distribute-list <WORD> out

#### F00229

- Status: unresolved
- Probe template: `distribute-list <WORD> out`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no supplied manual inventory or matching analysis to substantiate that no command topic exists.
- Evidence `P00226:probe` (probe_template): distribute-list <WORD> out

#### F00230

- Status: unresolved
- Probe template: `distribute-list <WORD> out bgp {<1-65535>. <0-65535>|<1-65535>|<65536-4294967295>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no supplied manual inventory or matching analysis to substantiate that no command topic exists.
- Evidence `P00227:probe` (probe_template): distribute-list <WORD> out bgp {<1-65535>. <0-65535>|<1-65535>|<65536-4294967295>}

#### F00231

- Status: unresolved
- Probe template: `distribute-list <WORD> out bgp {<65536-4294967295>|<1-65535>. <0-65535>|<1-65535>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no supplied manual inventory or matching analysis to substantiate that no command topic exists.
- Evidence `P00228:probe` (probe_template): distribute-list <WORD> out bgp {<65536-4294967295>|<1-65535>. <0-65535>|<1-65535>}

#### F00232

- Status: unresolved
- Probe template: `distribute-list <WORD> out {connected|ospf <WORD>|static|dagr}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no supplied manual inventory or matching analysis to substantiate that no command topic exists.
- Evidence `P00229:probe` (probe_template): distribute-list <WORD> out {connected|ospf <WORD>|static|dagr}

#### F00233

- Status: unresolved
- Probe template: `distribute-list <WORD> out {dagr|connected|ospf <WORD>|static}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-search evidence sufficient to verify that no matching command topic exists.
- Evidence `P00230:probe` (probe_template): distribute-list <WORD> out {dagr|connected|ospf <WORD>|static}

#### F00234

- Status: unresolved
- Probe template: `distribute-list route-policy <WORD> in`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-search evidence sufficient to verify that no matching command topic exists.
- Evidence `P00231:probe` (probe_template): distribute-list route-policy <WORD> in

#### F00235

- Status: unresolved
- Probe template: `distribute-list route-policy <WORD> in`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-search evidence sufficient to verify that no matching command topic exists.
- Evidence `P00232:probe` (probe_template): distribute-list route-policy <WORD> in

#### F00236

- Status: unresolved
- Probe template: `distribute-list {<WORD>|route-policy <WORD>} in`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-search evidence sufficient to verify that no matching command topic exists.
- Evidence `P00233:probe` (probe_template): distribute-list {<WORD>|route-policy <WORD>} in

#### F00237

- Status: unresolved
- Probe template: `distribute-list {<WORD>|route-policy <WORD>} in`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00234:probe` (probe_template): distribute-list {<WORD>|route-policy <WORD>} in

#### F00238

- Status: unresolved
- Probe template: `distribute-list {<WORD>|route-policy <WORD>} in`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual corpus or command-topic evidence to verify that no matching topic exists for the multi-area view.
- Evidence `P00235:probe` (probe_template): distribute-list {<WORD>|route-policy <WORD>} in

#### F00239

- Status: unresolved
- Probe template: `distribute-list {route-policy <WORD>|<WORD>} in`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual corpus or command-topic evidence to verify the asserted absence of a matching command topic for the area view.
- Evidence `P00236:probe` (probe_template): distribute-list {route-policy <WORD>|<WORD>} in

#### F00240

- Status: unresolved
- Probe template: `distribute-list {route-policy <WORD>|<WORD>} in`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual corpus or command-topic evidence to verify the asserted absence of a matching command topic for the interface view.
- Evidence `P00237:probe` (probe_template): distribute-list {route-policy <WORD>|<WORD>} in

#### F00241

- Status: unresolved
- Probe template: `distribute-list {route-policy <WORD>|<WORD>} in`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00238:probe` (probe_template): distribute-list {route-policy <WORD>|<WORD>} in

#### F00242

- Status: unresolved
- Probe template: `distribute {link-state [throttle <1-3600>|instance-id <0-4294967295>|excl-external|allow-prefix route-policy <WORD>]|bgp-ls {throttle <1-3600>|instance-id <0-4294967295>|allow-prefix route-policy <WORD>}}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00239:probe` (probe_template): distribute {link-state [throttle <1-3600>|instance-id <0-4294967295>|excl-external|allow-prefix route-policy <WORD>]|bgp-ls {throttle <1-3600>|instance-id <0-4294967295>|allow-prefix route-policy <WORD>}}

#### F00243

- Status: unresolved
- Probe template: `domain-id {secondary type|type} {0005 value <WORD>|8005 value <WORD>|0105 value <WORD>|0205 value <WORD>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00240:probe` (probe_template): domain-id {secondary type|type} {0005 value <WORD>|8005 value <WORD>|0105 value <WORD>|0205 value <WORD>}

#### F00244

- Status: unresolved
- Probe template: `domain-tag <1-4294967295>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00241:probe` (probe_template): domain-tag <1-4294967295>

#### F00245

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide the supplied manual corpus or search results needed to verify that no matching command topic exists for the area view.
- Evidence `P00242:probe` (probe_template): exclude-group <WORD>

#### F00246

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide the supplied manual corpus or search results needed to verify that no matching command topic exists for the interface view.
- Evidence `P00243:probe` (probe_template): exclude-group <WORD>

#### F00247

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide the supplied manual corpus or search results needed to verify that no matching command topic exists for the multi-area view.
- Evidence `P00244:probe` (probe_template): exclude-group <WORD>

#### F00248

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide the supplied manual corpus or search results needed to verify that no matching command topic exists for the router view.
- Evidence `P00245:probe` (probe_template): exclude-group <WORD>

#### F00249

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual-command inventory or other evidence to verify that no matching command topic exists for the sham-link view.
- Evidence `P00246:probe` (probe_template): exclude-group <WORD>

#### F00250

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not substantiate the asserted absence of a matching command topic in the supplied manuals for the unknown view.
- Evidence `P00247:probe` (probe_template): exclude-group <WORD>

#### F00251

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. No supplied manual evidence supports deciding whether a matching command topic exists for the virtual-link view.
- Evidence `P00248:probe` (probe_template): exclude-group <WORD>

#### F00252

- Status: unresolved
- Probe template: `exclude-group <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It lacks manual-command evidence needed to verify the claimed undercoverage for the vrf view.
- Evidence `P00249:probe` (probe_template): exclude-group <WORD>

#### F00253

- Status: unresolved
- Probe template: `external-out`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no manual corpus or command-topic evidence to substantiate undercoverage.
- Evidence `P00250:probe` (probe_template): external-out

#### F00254

- Status: unresolved
- Probe template: `external-out`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no manual corpus or command-topic evidence to substantiate undercoverage.
- Evidence `P00251:probe` (probe_template): external-out

#### F00255

- Status: unresolved
- Probe template: `external-out`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no manual corpus or command-topic evidence to substantiate undercoverage.
- Evidence `P00252:probe` (probe_template): external-out

#### F00256

- Status: unresolved
- Probe template: `external-out {disable|enable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no manual corpus or command-topic evidence to substantiate undercoverage.
- Evidence `P00253:probe` (probe_template): external-out {disable|enable}

#### F00257

- Status: unresolved
- Probe template: `external-out {enable|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence identifies the probe template but provides no manual-command or manual-corpus evidence to establish that no matching command topic exists.
- Evidence `P00254:probe` (probe_template): external-out {enable|disable}

#### F00258

- Status: unresolved
- Probe template: `external-out {enable|disable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence identifies the probe template but provides no manual-command or manual-corpus evidence to establish that no matching command topic exists.
- Evidence `P00255:probe` (probe_template): external-out {enable|disable}

#### F00259

- Status: unresolved
- Probe template: `external-out {enable|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence identifies the probe template but provides no manual-command or manual-corpus evidence to establish that no matching command topic exists.
- Evidence `P00256:probe` (probe_template): external-out {enable|disable}

#### F00260

- Status: unresolved
- Probe template: `fast-reroute disable`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence identifies the probe template but provides no manual-command or manual-corpus evidence to establish that no matching command topic exists.
- Evidence `P00257:probe` (probe_template): fast-reroute disable

#### F00261

- Status: unresolved
- Probe template: `fast-reroute disable`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00258:probe` (probe_template): fast-reroute disable

#### F00262

- Status: unresolved
- Probe template: `fast-reroute disable`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00259:probe` (probe_template): fast-reroute disable

#### F00263

- Status: unresolved
- Probe template: `fast-reroute disable`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00260:probe` (probe_template): fast-reroute disable

#### F00264

- Status: unresolved
- Probe template: `fast-reroute disable`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00261:probe` (probe_template): fast-reroute disable

#### F00265

- Status: unresolved
- Probe template: `fast-reroute disable`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe command template; it provides no supplied manual content or coverage inventory to verify that no matching command topic exists.
- Evidence `P00262:probe` (probe_template): fast-reroute disable

#### F00266

- Status: unresolved
- Probe template: `fast-reroute per-link`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is evidenced, but the absence of a matching command topic in the supplied manuals cannot be verified from the supplied evidence.
- Evidence `P00263:probe` (probe_template): fast-reroute per-link

#### F00267

- Status: unresolved
- Probe template: `fast-reroute per-link`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supports the stated probe template only. It does not support or refute the claimed lack of manual coverage for the interface semantic view.
- Evidence `P00264:probe` (probe_template): fast-reroute per-link

#### F00268

- Status: unresolved
- Probe template: `fast-reroute per-link`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence contains the probe template but no manual-command evidence, so the claimed absence of a matching manual topic cannot be decided.
- Evidence `P00265:probe` (probe_template): fast-reroute per-link

#### F00269

- Status: unresolved
- Probe template: `fast-reroute per-link`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual coverage or command-topic evidence to establish undercoverage.
- Evidence `P00266:probe` (probe_template): fast-reroute per-link

#### F00270

- Status: unresolved
- Probe template: `fast-reroute per-link`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual coverage or command-topic evidence to establish undercoverage.
- Evidence `P00267:probe` (probe_template): fast-reroute per-link

#### F00271

- Status: unresolved
- Probe template: `fast-reroute per-link priority-limit {critical|high|medium}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual coverage or command-topic evidence to establish undercoverage.
- Evidence `P00268:probe` (probe_template): fast-reroute per-link priority-limit {critical|high|medium}

#### F00272

- Status: unresolved
- Probe template: `fast-reroute per-link priority-limit {high|medium|critical}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual coverage or command-topic evidence to establish undercoverage.
- Evidence `P00269:probe` (probe_template): fast-reroute per-link priority-limit {high|medium|critical}

#### F00273

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The supplied evidence establishes the probe command, but contains no manual-topic evidence to verify that no matching command topic exists.
- Evidence `P00270:probe` (probe_template): fast-reroute per-link use-candidate-only

#### F00274

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The supplied evidence establishes the probe command, but contains no manual-topic evidence to verify that no matching command topic exists for the interface view.
- Evidence `P00271:probe` (probe_template): fast-reroute per-link use-candidate-only

#### F00275

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only [disable|enable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The supplied evidence establishes the probe command variant, but contains no manual-topic evidence to support the asserted absence of a matching command topic.
- Evidence `P00272:probe` (probe_template): fast-reroute per-link use-candidate-only [disable|enable]

#### F00276

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only [disable|enable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The supplied evidence establishes the probe command variant, but contains no manual-topic evidence to support the asserted absence of a matching command topic for the multi-area view.
- Evidence `P00273:probe` (probe_template): fast-reroute per-link use-candidate-only [disable|enable]

#### F00277

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only [disable|enable]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but contains no manual content or command-topic evidence to verify that no matching topic exists.
- Evidence `P00274:probe` (probe_template): fast-reroute per-link use-candidate-only [disable|enable]

#### F00278

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only [disable|enable]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but contains no manual content or command-topic evidence to verify that no matching topic exists in the VRF view.
- Evidence `P00275:probe` (probe_template): fast-reroute per-link use-candidate-only [disable|enable]

#### F00279

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only [enable|disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but contains no manual content or command-topic evidence to verify that no matching topic exists in the area view.
- Evidence `P00276:probe` (probe_template): fast-reroute per-link use-candidate-only [enable|disable]

#### F00280

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only [enable|disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but contains no manual content or command-topic evidence to verify that no matching topic exists in the interface view.
- Evidence `P00277:probe` (probe_template): fast-reroute per-link use-candidate-only [enable|disable]

#### F00281

- Status: unresolved
- Probe template: `fast-reroute per-link use-candidate-only [enable|disable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual-command inventory or documentation evidence to verify that no matching command topic exists.
- Evidence `P00278:probe` (probe_template): fast-reroute per-link use-candidate-only [enable|disable]

#### F00282

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual-command inventory or documentation evidence to verify that no matching command topic exists.
- Evidence `P00279:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00283

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual-command inventory or documentation evidence to verify that no matching command topic exists.
- Evidence `P00280:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00284

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template only. It contains no manual-command inventory or documentation evidence to verify that no matching command topic exists.
- Evidence `P00281:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00285

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the supplied manual-command coverage or absence of a matching topic.
- Evidence `P00282:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00286

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the supplied manual-command coverage or absence of a matching topic.
- Evidence `P00283:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00287

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the supplied manual-command coverage or absence of a matching topic.
- Evidence `P00284:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00288

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the supplied manual-command coverage or absence of a matching topic.
- Evidence `P00285:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00289

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command template, but provides no manual content or coverage comparison to support that no matching command topic exists.
- Evidence `P00286:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00290

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command template, but does not establish absence of a corresponding command topic in the supplied manuals.
- Evidence `P00287:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface Serial <R/S/I/P>

#### F00291

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface Serial <R/S/I/P>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command template, but contains no manual evidence from which command undercoverage can be confirmed or dismissed.
- Evidence `P00288:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface Serial <R/S/I/P>

#### F00292

- Status: unresolved
- Probe template: `fast-reroute per-link {exclude|lfa-candidate} interface Serial <R/S/I/P>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command template only; it cannot support the claimed absence of a matching manual command topic.
- Evidence `P00289:probe` (probe_template): fast-reroute per-link {exclude|lfa-candidate} interface Serial <R/S/I/P>

#### F00293

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no manual-source evidence to verify that no matching command topic exists.
- Evidence `P00290:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00294

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no manual-source evidence to verify that no matching command topic exists for the interface view.
- Evidence `P00291:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00295

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no manual-source evidence to verify that no matching command topic exists for the multi-area view.
- Evidence `P00292:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00296

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command variant but provides no manual-source evidence to verify that no matching command topic exists.
- Evidence `P00293:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00297

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but provides no manual-command evidence to verify that no matching command topic exists.
- Evidence `P00294:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00298

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but provides no manual-command evidence to verify that no matching command topic exists for the multi-area view.
- Evidence `P00295:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00299

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command, but provides no manual-command evidence to verify that no matching command topic exists for the router view.
- Evidence `P00296:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00300

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the MgmtEth probe command, but provides no manual-command evidence to verify the asserted absence of a matching topic.
- Evidence `P00297:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00301

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It does not provide manual-command coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00298:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00302

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It does not provide manual-command coverage evidence sufficient to verify that no matching command topic exists for the multi-area view.
- Evidence `P00299:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00303

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command variant. It does not provide manual-command coverage evidence sufficient to verify the claimed undercoverage.
- Evidence `P00300:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00304

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command variant. It does not provide manual-command coverage evidence sufficient to verify the claimed undercoverage for the multi-area view.
- Evidence `P00301:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00305

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The supplied probe establishes the command being assessed, but provides no manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00302:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00306

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The supplied probe establishes the command being assessed, but provides no manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00303:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>

#### F00307

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The supplied probe establishes the command being assessed, but provides no manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00304:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>

#### F00308

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The supplied probe establishes the command being assessed, but provides no manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00305:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>

#### F00309

- Status: unresolved
- Probe template: `fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but supplies no manual-command evidence or manual corpus coverage from which to verify that no matching topic exists.
- Evidence `P00306:probe` (probe_template): fast-reroute per-link {lfa-candidate|exclude} interface Serial <R/S/I/P>

#### F00310

- Status: unresolved
- Probe template: `fast-reroute per-prefix`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but does not provide the supplied manuals or matching-command results needed to substantiate undercoverage.
- Evidence `P00307:probe` (probe_template): fast-reroute per-prefix

#### F00311

- Status: unresolved
- Probe template: `fast-reroute per-prefix`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe is evidenced, but the absence of manual evidence prevents confirmation or dismissal of the claimed missing command topic.
- Evidence `P00308:probe` (probe_template): fast-reroute per-prefix

#### F00312

- Status: unresolved
- Probe template: `fast-reroute per-prefix`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the probe command only; it cannot establish whether the supplied manuals contain a matching topic.
- Evidence `P00309:probe` (probe_template): fast-reroute per-prefix

#### F00313

- Status: unresolved
- Probe template: `fast-reroute per-prefix`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe command. It provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00310:probe` (probe_template): fast-reroute per-prefix

#### F00314

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe command. It provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00311:probe` (probe_template): fast-reroute per-prefix exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00315

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe command. It provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00312:probe` (probe_template): fast-reroute per-prefix exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00316

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes only the probe command. It provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00313:probe` (probe_template): fast-reroute per-prefix exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00317

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists for the area view.
- Evidence `P00314:probe` (probe_template): fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00318

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists for the interface view.
- Evidence `P00315:probe` (probe_template): fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00319

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists for the multi-area view.
- Evidence `P00316:probe` (probe_template): fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00320

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists for the VRF view.
- Evidence `P00317:probe` (probe_template): fast-reroute per-prefix exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00321

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00318:probe` (probe_template): fast-reroute per-prefix exclude interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00322

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00319:probe` (probe_template): fast-reroute per-prefix exclude interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00323

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00320:probe` (probe_template): fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00324

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00321:probe` (probe_template): fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00325

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence supplies the probe command only and provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00322:probe` (probe_template): fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00326

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence supplies the probe command only and provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00323:probe` (probe_template): fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00327

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence supplies the probe command only and provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00324:probe` (probe_template): fast-reroute per-prefix exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00328

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface Serial <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence supplies the probe command only and provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00325:probe` (probe_template): fast-reroute per-prefix exclude interface Serial <R/S/I/P>

#### F00329

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual evidence to verify that no matching command topic exists for the interface view.
- Evidence `P00326:probe` (probe_template): fast-reroute per-prefix exclude interface Serial <R/S/I/P>

#### F00330

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface Serial <R/S/I/P>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual evidence to verify that no matching command topic exists for the multi-area view.
- Evidence `P00327:probe` (probe_template): fast-reroute per-prefix exclude interface Serial <R/S/I/P>

#### F00331

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface Serial <R/S/I/P>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual evidence to verify that no matching command topic exists for the router view.
- Evidence `P00328:probe` (probe_template): fast-reroute per-prefix exclude interface Serial <R/S/I/P>

#### F00332

- Status: unresolved
- Probe template: `fast-reroute per-prefix exclude interface Serial <R/S/I/P>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual evidence to verify that no matching command topic exists for the VRF view.
- Evidence `P00329:probe` (probe_template): fast-reroute per-prefix exclude interface Serial <R/S/I/P>

#### F00333

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual corpus or command-coverage evidence to verify that no matching manual topic exists for the area view.
- Evidence `P00330:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00334

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but does not support the asserted absence of a matching manual topic for the interface view.
- Evidence `P00331:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00335

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe evidence alone cannot establish that supplied manuals contain no matching command topic for the multi-area view.
- Evidence `P00332:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00336

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence provides only the probe template and cannot verify the claimed lack of a matching command topic for the VRF view.
- Evidence `P00333:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00337

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00334:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00338

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00335:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00339

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00336:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00340

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00337:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00341

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide supplied-manual content or search results sufficient to verify that no matching command topic exists.
- Evidence `P00338:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00342

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide supplied-manual content or search results sufficient to verify that no matching command topic exists.
- Evidence `P00339:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00343

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide supplied-manual content or search results sufficient to verify that no matching command topic exists.
- Evidence `P00340:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00344

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide supplied-manual content or search results sufficient to verify that no matching command topic exists.
- Evidence `P00341:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00345

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence identifies the probe command but provides no manual-content evidence to verify that no matching command topic exists for the area semantic view.
- Evidence `P00342:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00346

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence identifies the probe command but does not establish whether supplied manuals contain a matching topic for the interface semantic view.
- Evidence `P00343:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00347

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence contains only the probe template and cannot support or refute absence of a matching manual command topic for the multi-area semantic view.
- Evidence `P00344:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00348

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence identifies the probe command but lacks manual-topic evidence needed to confirm command undercoverage for the router semantic view.
- Evidence `P00345:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00349

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage inventory to verify that no matching command topic exists for the area view.
- Evidence `P00346:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>

#### F00350

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage inventory to verify that no matching command topic exists for the interface view.
- Evidence `P00347:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>

#### F00351

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage inventory to verify that no matching command topic exists for the multi-area view.
- Evidence `P00348:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>

#### F00352

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage inventory to verify that no matching command topic exists for the router view.
- Evidence `P00349:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>

#### F00353

- Status: unresolved
- Probe template: `fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00350:probe` (probe_template): fast-reroute per-prefix lfa-candidate interface Serial <R/S/I/P>

#### F00354

- Status: unresolved
- Probe template: `fast-reroute per-prefix priority-limit {high|medium|critical}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00351:probe` (probe_template): fast-reroute per-prefix priority-limit {high|medium|critical}

#### F00355

- Status: unresolved
- Probe template: `fast-reroute per-prefix priority-limit {medium|high|critical}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00352:probe` (probe_template): fast-reroute per-prefix priority-limit {medium|high|critical}

#### F00356

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {disable|maximum-cost <1-4294967295>|tunnel mpls-ldp}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command coverage evidence to verify that no matching topic exists.
- Evidence `P00353:probe` (probe_template): fast-reroute per-prefix remote-lfa {disable|maximum-cost <1-4294967295>|tunnel mpls-ldp}

#### F00357

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {disable|tunnel mpls-ldp|maximum-cost <1-4294967295>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence from which to verify the claimed absence of a match.
- Evidence `P00354:probe` (probe_template): fast-reroute per-prefix remote-lfa {disable|tunnel mpls-ldp|maximum-cost <1-4294967295>}

#### F00358

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {disable|tunnel mpls-ldp|maximum-cost <1-4294967295>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence from which to verify the claimed absence of a match for the multi-area view.
- Evidence `P00355:probe` (probe_template): fast-reroute per-prefix remote-lfa {disable|tunnel mpls-ldp|maximum-cost <1-4294967295>}

#### F00359

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {maximum-cost <1-4294967295>|disable|tunnel mpls-ldp}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but does not provide the relevant manual coverage needed to confirm that no matching command topic exists.
- Evidence `P00356:probe` (probe_template): fast-reroute per-prefix remote-lfa {maximum-cost <1-4294967295>|disable|tunnel mpls-ldp}

#### F00360

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {maximum-cost <1-4294967295>|tunnel mpls-ldp|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but does not support determining whether a matching interface-view manual command topic exists.
- Evidence `P00357:probe` (probe_template): fast-reroute per-prefix remote-lfa {maximum-cost <1-4294967295>|tunnel mpls-ldp|disable}

#### F00361

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {maximum-cost <1-4294967295>|tunnel mpls-ldp|disable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify the asserted absence of a matching manual command.
- Evidence `P00358:probe` (probe_template): fast-reroute per-prefix remote-lfa {maximum-cost <1-4294967295>|tunnel mpls-ldp|disable}

#### F00362

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|disable|maximum-cost <1-4294967295>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify the asserted absence of a matching manual command.
- Evidence `P00359:probe` (probe_template): fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|disable|maximum-cost <1-4294967295>}

#### F00363

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|disable|maximum-cost <1-4294967295>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify the asserted absence of a matching manual command.
- Evidence `P00360:probe` (probe_template): fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|disable|maximum-cost <1-4294967295>}

#### F00364

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|maximum-cost <1-4294967295>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify the asserted absence of a matching manual command.
- Evidence `P00361:probe` (probe_template): fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|maximum-cost <1-4294967295>|disable}

#### F00365

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|maximum-cost <1-4294967295>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage comparison to verify that no matching command topic exists.
- Evidence `P00362:probe` (probe_template): fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|maximum-cost <1-4294967295>|disable}

#### F00366

- Status: unresolved
- Probe template: `fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|maximum-cost <1-4294967295>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage comparison to verify that no matching command topic exists.
- Evidence `P00363:probe` (probe_template): fast-reroute per-prefix remote-lfa {tunnel mpls-ldp|maximum-cost <1-4294967295>|disable}

#### F00367

- Status: unresolved
- Probe template: `fast-reroute per-prefix ti-lfa [disable|enable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage comparison to verify that no matching command topic exists.
- Evidence `P00364:probe` (probe_template): fast-reroute per-prefix ti-lfa [disable|enable]

#### F00368

- Status: unresolved
- Probe template: `fast-reroute per-prefix ti-lfa [disable|enable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage comparison to verify that no matching command topic exists.
- Evidence `P00365:probe` (probe_template): fast-reroute per-prefix ti-lfa [disable|enable]

#### F00369

- Status: unresolved
- Probe template: `fast-reroute per-prefix ti-lfa [disable|enable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00366:probe` (probe_template): fast-reroute per-prefix ti-lfa [disable|enable]

#### F00370

- Status: unresolved
- Probe template: `fast-reroute per-prefix ti-lfa [enable|disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00367:probe` (probe_template): fast-reroute per-prefix ti-lfa [enable|disable]

#### F00371

- Status: unresolved
- Probe template: `fast-reroute per-prefix ti-lfa [enable|disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00368:probe` (probe_template): fast-reroute per-prefix ti-lfa [enable|disable]

#### F00372

- Status: unresolved
- Probe template: `fast-reroute per-prefix ti-lfa [enable|disable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command coverage evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00369:probe` (probe_template): fast-reroute per-prefix ti-lfa [enable|disable]

#### F00373

- Status: unresolved
- Probe template: `fast-reroute per-prefix ti-lfa [enable|disable]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual content or command-topic inventory to support or refute the claimed absence of a matching manual topic.
- Evidence `P00370:probe` (probe_template): fast-reroute per-prefix ti-lfa [enable|disable]

#### F00374

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual content or command-topic inventory to support or refute the claimed absence of a matching manual topic.
- Evidence `P00371:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}

#### F00375

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual content or command-topic inventory to support or refute the claimed absence of a matching manual topic.
- Evidence `P00372:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}

#### F00376

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual content or command-topic inventory to support or refute the claimed absence of a matching manual topic.
- Evidence `P00373:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}

#### F00377

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence establishes the probe command, but contains no manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00374:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {disable|index <1-255>}

#### F00378

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence establishes the probe command, but does not establish absence of a matching command topic in the manuals.
- Evidence `P00375:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}

#### F00379

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe template is supported, but no supplied manual-search or command-topic evidence supports the claimed undercoverage.
- Evidence `P00376:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}

#### F00380

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence identifies the probe template only; it cannot confirm that the manuals lack a matching command topic.
- Evidence `P00377:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}

#### F00381

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00378:probe` (probe_template): fast-reroute per-prefix tiebreaker downstream {index <1-255>|disable}

#### F00382

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00379:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {disable|index <1-255>}

#### F00383

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00380:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {disable|index <1-255>}

#### F00384

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00381:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {disable|index <1-255>}

#### F00385

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual corpus or command-topic evidence to verify that no matching topic exists for the area view.
- Evidence `P00382:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}

#### F00386

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual corpus or command-topic evidence to verify that no matching topic exists for the interface view.
- Evidence `P00383:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}

#### F00387

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual corpus or command-topic evidence to verify that no matching topic exists for the multi-area view.
- Evidence `P00384:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}

#### F00388

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual corpus or command-topic evidence to verify that no matching topic exists for the router view.
- Evidence `P00385:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}

#### F00389

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual corpus or command-topic evidence to verify that no match exists.
- Evidence `P00386:probe` (probe_template): fast-reroute per-prefix tiebreaker interface-disjoint {index <1-255>|disable}

#### F00390

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual corpus or command-topic evidence to verify that no match exists.
- Evidence `P00387:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}

#### F00391

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual corpus or command-topic evidence to verify that no match exists.
- Evidence `P00388:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}

#### F00392

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual corpus or command-topic evidence to verify that no match exists.
- Evidence `P00389:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}

#### F00393

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the contents or coverage of the supplied manuals needed to verify that no matching command topic exists.
- Evidence `P00390:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}

#### F00394

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the contents or coverage of the supplied manuals needed to verify that no matching command topic exists.
- Evidence `P00391:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {disable|index <1-255>}

#### F00395

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the contents or coverage of the supplied manuals needed to verify that no matching command topic exists.
- Evidence `P00392:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {index <1-255>|disable}

#### F00396

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not establish the contents or coverage of the supplied manuals needed to verify that no matching command topic exists.
- Evidence `P00393:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {index <1-255>|disable}

#### F00397

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lc-disjoint {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes the probe command, but contains no manual content or coverage inventory that can substantiate the claimed absence of a matching command topic.
- Evidence `P00394:probe` (probe_template): fast-reroute per-prefix tiebreaker lc-disjoint {index <1-255>|disable}

#### F00398

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes the probe command, but contains no manual content or coverage inventory that can substantiate the claimed absence of a matching command topic.
- Evidence `P00395:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}

#### F00399

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes the probe command, but contains no manual content or coverage inventory that can substantiate the claimed absence of a matching command topic.
- Evidence `P00396:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}

#### F00400

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes the probe command, but contains no manual content or coverage inventory that can substantiate the claimed absence of a matching command topic.
- Evidence `P00397:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}

#### F00401

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command text only. It does not establish the contents or coverage of the supplied manuals, so the claimed absence of a matching command topic cannot be verified.
- Evidence `P00398:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {disable|index <1-255>}

#### F00402

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command text only. It does not establish the contents or coverage of the supplied manuals, so the claimed absence of a matching command topic cannot be verified.
- Evidence `P00399:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}

#### F00403

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command text only. It does not establish the contents or coverage of the supplied manuals, so the claimed absence of a matching command topic cannot be verified.
- Evidence `P00400:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}

#### F00404

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command text only. It does not establish the contents or coverage of the supplied manuals, so the claimed absence of a matching command topic cannot be verified.
- Evidence `P00401:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}

#### F00405

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command template, but provides no manual-command evidence from which to verify that no matching topic exists.
- Evidence `P00402:probe` (probe_template): fast-reroute per-prefix tiebreaker lowest-backup-metric {index <1-255>|disable}

#### F00406

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe template is evidenced, but the supplied evidence does not establish the absence of a corresponding manual command topic.
- Evidence `P00403:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}

#### F00407

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence identifies the probe command only; it cannot support or refute the claimed manual undercoverage for the interface semantic view.
- Evidence `P00404:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}

#### F00408

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence shows the probe template but contains no manual-topic coverage data sufficient to confirm the claimed undercoverage for the multi-area semantic view.
- Evidence `P00405:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}

#### F00409

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00406:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {disable|index <1-255>}

#### F00410

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00407:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}

#### F00411

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00408:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}

#### F00412

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify or refute the claimed absence of a matching topic.
- Evidence `P00409:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}

#### F00413

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the Probe command template, but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00410:probe` (probe_template): fast-reroute per-prefix tiebreaker node-protecting {index <1-255>|disable}

#### F00414

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the Probe command template, but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00411:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}

#### F00415

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the Probe command template, but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00412:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}

#### F00416

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the Probe command template, but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00413:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}

#### F00417

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching topic exists.
- Evidence `P00414:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {disable|index <1-255>}

#### F00418

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but does not support the asserted absence of a matching command topic in the supplied manuals.
- Evidence `P00415:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}

#### F00419

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: Only the probe template is supplied; no manual evidence is available to confirm or dismiss the claimed command undercoverage.
- Evidence `P00416:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}

#### F00420

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command only and cannot establish whether a matching manual command topic is absent.
- Evidence `P00417:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}

#### F00421

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe command, but supplies no manual evidence by which to verify that no matching command topic exists.
- Evidence `P00418:probe` (probe_template): fast-reroute per-prefix tiebreaker primary-path {index <1-255>|disable}

#### F00422

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe command, but supplies no manual evidence by which to verify that no matching command topic exists.
- Evidence `P00419:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {disable|index <1-255>}

#### F00423

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe command, but supplies no manual evidence by which to verify that no matching command topic exists.
- Evidence `P00420:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {disable|index <1-255>}

#### F00424

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe command, but supplies no manual evidence by which to verify that no matching command topic exists.
- Evidence `P00421:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {disable|index <1-255>}

#### F00425

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe command template. It provides no supplied manual-command inventory or coverage evidence to substantiate that no matching command topic exists for the area view.
- Evidence `P00422:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}

#### F00426

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe command template. It provides no supplied manual-command inventory or coverage evidence to substantiate that no matching command topic exists for the interface view.
- Evidence `P00423:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}

#### F00427

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe command template. It provides no supplied manual-command inventory or coverage evidence to substantiate that no matching command topic exists for the multi-area view.
- Evidence `P00424:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}

#### F00428

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe command template. It provides no supplied manual-command inventory or coverage evidence to substantiate that no matching command topic exists for the router view.
- Evidence `P00425:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}

#### F00429

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual corpus or command-topic evidence from which absence of a match can be verified.
- Evidence `P00426:probe` (probe_template): fast-reroute per-prefix tiebreaker secondary-path {index <1-255>|disable}

#### F00430

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but does not substantiate that no supplied manual command topic matches it in the area view.
- Evidence `P00427:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}

#### F00431

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but does not provide manual-command evidence sufficient to determine coverage in the interface view.
- Evidence `P00428:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}

#### F00432

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but lacks the manual corpus or command-topic evidence required to verify undercoverage in the multi-area view.
- Evidence `P00429:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}

#### F00433

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content from which to verify that no matching command topic exists.
- Evidence `P00430:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}

#### F00434

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content from which to verify that no matching command topic exists for the VRF semantic view.
- Evidence `P00431:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {disable|index <1-255>}

#### F00435

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {index <1-255>|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content from which to verify that no matching command topic exists for the area semantic view.
- Evidence `P00432:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {index <1-255>|disable}

#### F00436

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {index <1-255>|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual content from which to verify that no matching command topic exists for the interface semantic view.
- Evidence `P00433:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {index <1-255>|disable}

#### F00437

- Status: unresolved
- Probe template: `fast-reroute per-prefix tiebreaker srlg-disjoint {index <1-255>|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe establishes the command under review, but no supplied manual evidence supports or disproves the claimed absence of a matching command topic.
- Evidence `P00434:probe` (probe_template): fast-reroute per-prefix tiebreaker srlg-disjoint {index <1-255>|disable}

#### F00438

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command only; it does not substantiate that the supplied manuals lack a matching topic.
- Evidence `P00435:probe` (probe_template): fast-reroute per-prefix use-candidate-only

#### F00439

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only [disable|enable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe text alone cannot verify the asserted manual-command undercoverage.
- Evidence `P00436:probe` (probe_template): fast-reroute per-prefix use-candidate-only [disable|enable]

#### F00440

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only [disable|enable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence provides only the command probe and contains no manual material from which to confirm or dismiss the claimed absence.
- Evidence `P00437:probe` (probe_template): fast-reroute per-prefix use-candidate-only [disable|enable]

#### F00441

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only [disable|enable]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00438:probe` (probe_template): fast-reroute per-prefix use-candidate-only [disable|enable]

#### F00442

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only [enable|disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00439:probe` (probe_template): fast-reroute per-prefix use-candidate-only [enable|disable]

#### F00443

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only [enable|disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00440:probe` (probe_template): fast-reroute per-prefix use-candidate-only [enable|disable]

#### F00444

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only [enable|disable]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00441:probe` (probe_template): fast-reroute per-prefix use-candidate-only [enable|disable]

#### F00445

- Status: unresolved
- Probe template: `fast-reroute per-prefix use-candidate-only [enable|disable]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no manual-command evidence from which to verify that no matching topic exists.
- Evidence `P00442:probe` (probe_template): fast-reroute per-prefix use-candidate-only [enable|disable]

#### F00446

- Status: unresolved
- Probe template: `fast-reroute per-prefix [load-sharing disable]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but does not substantiate the asserted absence of a corresponding manual command topic.
- Evidence `P00443:probe` (probe_template): fast-reroute per-prefix [load-sharing disable]

#### F00447

- Status: unresolved
- Probe template: `fast-reroute per-prefix {load-sharing disable|srlg-protection weighted-global}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe template only; it cannot confirm or dismiss manual-command undercoverage without manual-topic evidence.
- Evidence `P00444:probe` (probe_template): fast-reroute per-prefix {load-sharing disable|srlg-protection weighted-global}

#### F00448

- Status: unresolved
- Probe template: `fast-reroute {per-link use-candidate-only [enable|disable]|per-prefix use-candidate-only {enable|disable}}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe template is supported, but no evidence of the supplied manuals or their command topics is provided to validate the undercoverage claim.
- Evidence `P00445:probe` (probe_template): fast-reroute {per-link use-candidate-only [enable|disable]|per-prefix use-candidate-only {enable|disable}}

#### F00449

- Status: unresolved
- Probe template: `fast-reroute {per-link use-candidate-only {disable|enable}|per-prefix use-candidate-only [disable|enable]}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus information from which to verify that no matching command topic exists.
- Evidence `P00446:probe` (probe_template): fast-reroute {per-link use-candidate-only {disable|enable}|per-prefix use-candidate-only [disable|enable]}

#### F00450

- Status: unresolved
- Probe template: `fast-reroute {per-link use-candidate-only {enable|disable}|per-prefix use-candidate-only [enable|disable]}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but does not establish the asserted absence of a matching topic in the supplied manuals.
- Evidence `P00447:probe` (probe_template): fast-reroute {per-link use-candidate-only {enable|disable}|per-prefix use-candidate-only [enable|disable]}

#### F00451

- Status: unresolved
- Probe template: `fast-reroute {per-link use-candidate-only {enable|disable}|per-prefix use-candidate-only [enable|disable]}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template alone cannot confirm or dismiss whether the manuals contain a corresponding command topic.
- Evidence `P00448:probe` (probe_template): fast-reroute {per-link use-candidate-only {enable|disable}|per-prefix use-candidate-only [enable|disable]}

#### F00452

- Status: unresolved
- Probe template: `fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence contains only the probe template and lacks manual-command or coverage evidence needed to support the undercoverage claim.
- Evidence `P00449:probe` (probe_template): fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00453

- Status: unresolved
- Probe template: `fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00450:probe` (probe_template): fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00454

- Status: unresolved
- Probe template: `fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00451:probe` (probe_template): fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00455

- Status: unresolved
- Probe template: `fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00452:probe` (probe_template): fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00456

- Status: unresolved
- Probe template: `fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence establishes the probe command only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00453:probe` (probe_template): fast-reroute {per-link {exclude|lfa-candidate}|per-prefix {lfa-candidate|exclude}} interface Serial <R/S/I/P>

#### F00457

- Status: confirmed
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: confirmed
- Confidence: 0.96
- Review rationale: The supplied candidate contains the probe command and an empty manual_commands list, so no supplied manual command topic matches it.
- Evidence `P00454:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00458

- Status: confirmed
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: confirmed
- Confidence: 0.96
- Review rationale: The supplied candidate contains the probe command and an empty manual_commands list, so no supplied manual command topic matches it.
- Evidence `P00455:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00459

- Status: confirmed
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: confirmed
- Confidence: 0.96
- Review rationale: The supplied candidate contains the probe command and an empty manual_commands list, so no supplied manual command topic matches it.
- Evidence `P00456:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00460

- Status: confirmed
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: confirmed
- Confidence: 0.96
- Review rationale: The supplied candidate contains the probe command and an empty manual_commands list, so no supplied manual command topic matches it.
- Evidence `P00457:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00461

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command, but provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00458:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {exclude|lfa-candidate}} interface Serial <R/S/I/P>

#### F00462

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command, but provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00459:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00463

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command, but provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00460:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00464

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command, but provides no manual-command evidence to establish that no matching command topic exists.
- Evidence `P00461:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00465

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00462:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00466

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00463:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00467

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface Serial <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00464:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface Serial <R/S/I/P>

#### F00468

- Status: unresolved
- Probe template: `fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00465:probe` (probe_template): fast-reroute {per-link {lfa-candidate|exclude}|per-prefix {lfa-candidate|exclude}} interface Serial <R/S/I/P>

#### F00469

- Status: unresolved
- Probe template: `fast-reroute {per-prefix use-candidate-only [enable|disable]|per-link use-candidate-only {enable|disable}}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00466:probe` (probe_template): fast-reroute {per-prefix use-candidate-only [enable|disable]|per-link use-candidate-only {enable|disable}}

#### F00470

- Status: unresolved
- Probe template: `fast-reroute {per-prefix use-candidate-only {disable|enable}|per-link use-candidate-only [disable|enable]}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00467:probe` (probe_template): fast-reroute {per-prefix use-candidate-only {disable|enable}|per-link use-candidate-only [disable|enable]}

#### F00471

- Status: unresolved
- Probe template: `fast-reroute {per-prefix use-candidate-only {enable|disable}|per-link use-candidate-only [enable|disable]}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00468:probe` (probe_template): fast-reroute {per-prefix use-candidate-only {enable|disable}|per-link use-candidate-only [enable|disable]}

#### F00472

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00469:probe` (probe_template): fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00473

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command template, but supplies no manual content or coverage inventory to verify that no matching command topic exists.
- Evidence `P00470:probe` (probe_template): fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00474

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe template is evidenced, but the absence of matching manual commands cannot be verified from the supplied evidence alone.
- Evidence `P00471:probe` (probe_template): fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00475

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence shows the MgmtEth probe template only; it does not establish whether the supplied manuals contain a matching command topic.
- Evidence `P00472:probe` (probe_template): fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00476

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe command is supported, but no supplied manual evidence permits confirmation or dismissal of the asserted command undercoverage.
- Evidence `P00473:probe` (probe_template): fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00477

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface Serial <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; it does not establish the contents or completeness of the supplied manuals needed to verify command undercoverage.
- Evidence `P00474:probe` (probe_template): fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface Serial <R/S/I/P>

#### F00478

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; it does not establish the contents or completeness of the supplied manuals needed to verify command undercoverage for the interface view.
- Evidence `P00475:probe` (probe_template): fast-reroute {per-prefix {exclude|lfa-candidate}|per-link {exclude|lfa-candidate}} interface Serial <R/S/I/P>

#### F00479

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; no manual-topic evidence is provided to confirm that no matching command topic exists.
- Evidence `P00476:probe` (probe_template): fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00480

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; no evidence of the relevant manual corpus or its command topics is supplied.
- Evidence `P00477:probe` (probe_template): fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00481

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; it provides no supplied manual content or command-topic coverage information to verify undercoverage.
- Evidence `P00478:probe` (probe_template): fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00482

- Status: unresolved
- Probe template: `fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface Serial <R/S/I/P>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; it provides no supplied manual content or command-topic coverage information to verify undercoverage.
- Evidence `P00479:probe` (probe_template): fast-reroute {per-prefix {lfa-candidate|exclude}|per-link {lfa-candidate|exclude}} interface Serial <R/S/I/P>

#### F00483

- Status: unresolved
- Probe template: `flex-algo <128-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; it provides no supplied manual content or command-topic coverage information to verify undercoverage.
- Evidence `P00480:probe` (probe_template): flex-algo <128-255>

#### F00484

- Status: unresolved
- Probe template: `flood-reduction`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command only; it provides no supplied manual content or command-topic coverage information to verify undercoverage.
- Evidence `P00481:probe` (probe_template): flood-reduction

#### F00485

- Status: unresolved
- Probe template: `flood-reduction`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00482:probe` (probe_template): flood-reduction

#### F00486

- Status: unresolved
- Probe template: `flood-reduction`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00483:probe` (probe_template): flood-reduction

#### F00487

- Status: unresolved
- Probe template: `flood-reduction`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00484:probe` (probe_template): flood-reduction

#### F00488

- Status: unresolved
- Probe template: `flood-reduction {disable|enable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The evidence establishes only the probe template and alternatives; it provides no supplied manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00485:probe` (probe_template): flood-reduction {disable|enable}

#### F00489

- Status: unresolved
- Probe template: `flood-reduction {disable|enable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00486:probe` (probe_template): flood-reduction {disable|enable}

#### F00490

- Status: unresolved
- Probe template: `flood-reduction {disable|enable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00487:probe` (probe_template): flood-reduction {disable|enable}

#### F00491

- Status: unresolved
- Probe template: `flood-reduction {enable|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00488:probe` (probe_template): flood-reduction {enable|disable}

#### F00492

- Status: unresolved
- Probe template: `flood-reduction {enable|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual corpus or command-topic evidence to verify that no matching topic exists.
- Evidence `P00489:probe` (probe_template): flood-reduction {enable|disable}

#### F00493

- Status: unresolved
- Probe template: `flood-reduction {enable|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but provides no manual content or coverage inventory to substantiate that no matching command topic exists.
- Evidence `P00490:probe` (probe_template): flood-reduction {enable|disable}

#### F00494

- Status: unresolved
- Probe template: `hello-interval <1-65535>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but provides no manual content or coverage inventory to substantiate that no matching command topic exists.
- Evidence `P00491:probe` (probe_template): hello-interval <1-65535>

#### F00495

- Status: unresolved
- Probe template: `hello-interval <1-65535>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but provides no manual content or coverage inventory to substantiate that no matching command topic exists.
- Evidence `P00492:probe` (probe_template): hello-interval <1-65535>

#### F00496

- Status: unresolved
- Probe template: `hello-interval <1-65535>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but provides no manual content or coverage inventory to substantiate that no matching command topic exists.
- Evidence `P00493:probe` (probe_template): hello-interval <1-65535>

#### F00497

- Status: unresolved
- Probe template: `hello-interval <1-65535>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence to verify that no matching command topic exists in the router view.
- Evidence `P00494:probe` (probe_template): hello-interval <1-65535>

#### F00498

- Status: unresolved
- Probe template: `hello-interval <1-65535>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence to verify that no matching command topic exists in the sham-link view.
- Evidence `P00495:probe` (probe_template): hello-interval <1-65535>

#### F00499

- Status: unresolved
- Probe template: `hello-interval <1-65535>`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence to verify that no matching command topic exists in the virtual-link view.
- Evidence `P00496:probe` (probe_template): hello-interval <1-65535>

#### F00500

- Status: unresolved
- Probe template: `hello-interval <1-65535>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence to verify that no matching command topic exists in the VRF view.
- Evidence `P00497:probe` (probe_template): hello-interval <1-65535>

#### F00501

- Status: unresolved
- Probe template: `ignore lsa mospf`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not establish that the supplied manuals contain no matching command topic.
- Evidence `P00498:probe` (probe_template): ignore lsa mospf

#### F00502

- Status: unresolved
- Probe template: `ignore lsa mospf`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not establish that the supplied manuals contain no matching command topic for the VRF semantic view.
- Evidence `P00499:probe` (probe_template): ignore lsa mospf

#### F00503

- Status: unresolved
- Probe template: `interface GigabitEthernet 0/0/0/0`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the interface probe template. It provides no manual-command evidence supporting the claimed undercoverage.
- Evidence `P00500:probe` (probe_template): interface GigabitEthernet 0/0/0/0

#### F00504

- Status: unresolved
- Probe template: `interface GigabitEthernet <R/S/I/P/B or R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the parameterized interface probe template. It does not support a determination that no corresponding manual topic exists.
- Evidence `P00501:probe` (probe_template): interface GigabitEthernet <R/S/I/P/B or R/S/I/P>

#### F00505

- Status: unresolved
- Probe template: `interface Loopback <0-2147483647>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00502:probe` (probe_template): interface Loopback <0-2147483647>

#### F00506

- Status: unresolved
- Probe template: `interface MgmtEth 0/RP0/CPU0/0`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00503:probe` (probe_template): interface MgmtEth 0/RP0/CPU0/0

#### F00507

- Status: unresolved
- Probe template: `interface MgmtEth <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00504:probe` (probe_template): interface MgmtEth <R/S/I/P>

#### F00508

- Status: unresolved
- Probe template: `interface Serial <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00505:probe` (probe_template): interface Serial <R/S/I/P>

#### F00509

- Status: unresolved
- Probe template: `link-down fast-detect`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual-search or command-topic evidence to support the claimed absence of a match.
- Evidence `P00506:probe` (probe_template): link-down fast-detect

#### F00510

- Status: unresolved
- Probe template: `link-down fast-detect`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual-search or command-topic evidence to support the claimed absence of a match.
- Evidence `P00507:probe` (probe_template): link-down fast-detect

#### F00511

- Status: unresolved
- Probe template: `link-down fast-detect [disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual-search or command-topic evidence to support the claimed absence of a match.
- Evidence `P00508:probe` (probe_template): link-down fast-detect [disable]

#### F00512

- Status: unresolved
- Probe template: `link-down fast-detect [disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it provides no supplied manual-search or command-topic evidence to support the claimed absence of a match.
- Evidence `P00509:probe` (probe_template): link-down fast-detect [disable]

#### F00513

- Status: unresolved
- Probe template: `log adjacency changes {detail|disable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify that no matching topic exists.
- Evidence `P00510:probe` (probe_template): log adjacency changes {detail|disable}

#### F00514

- Status: unresolved
- Probe template: `log adjacency changes {disable|detail}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify that no matching topic exists.
- Evidence `P00511:probe` (probe_template): log adjacency changes {disable|detail}

#### F00515

- Status: unresolved
- Probe template: `loopback stub-network [disable|enable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify that no matching topic exists.
- Evidence `P00512:probe` (probe_template): loopback stub-network [disable|enable]

#### F00516

- Status: unresolved
- Probe template: `loopback stub-network [disable|enable]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to verify that no matching topic exists.
- Evidence `P00513:probe` (probe_template): loopback stub-network [disable|enable]

#### F00517

- Status: unresolved
- Probe template: `loopback stub-network [disable|enable]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-content evidence to verify that no matching command topic exists.
- Evidence `P00514:probe` (probe_template): loopback stub-network [disable|enable]

#### F00518

- Status: unresolved
- Probe template: `loopback stub-network [enable|disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-content evidence to verify that no matching command topic exists.
- Evidence `P00515:probe` (probe_template): loopback stub-network [enable|disable]

#### F00519

- Status: unresolved
- Probe template: `loopback stub-network [enable|disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-content evidence to verify that no matching command topic exists.
- Evidence `P00516:probe` (probe_template): loopback stub-network [enable|disable]

#### F00520

- Status: unresolved
- Probe template: `max-lsa <1-4294967294>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-content evidence to verify that no matching command topic exists.
- Evidence `P00517:probe` (probe_template): max-lsa <1-4294967294>

#### F00521

- Status: unresolved
- Probe template: `max-lsa <1-4294967294>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00518:probe` (probe_template): max-lsa <1-4294967294>

#### F00522

- Status: unresolved
- Probe template: `max-lsa <1-4294967294> {reset-time <2-71582788>|ignore-count <1-4294967294>|<1-100>|warning-only|ignore-time <1-35791394>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00519:probe` (probe_template): max-lsa <1-4294967294> {reset-time <2-71582788>|ignore-count <1-4294967294>|<1-100>|warning-only|ignore-time <1-35791394>}

#### F00523

- Status: unresolved
- Probe template: `max-lsa <1-4294967294> {warning-only|ignore-count <1-4294967294>|reset-time <2-71582788>|<1-100>|ignore-time <1-35791394>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00520:probe` (probe_template): max-lsa <1-4294967294> {warning-only|ignore-count <1-4294967294>|reset-time <2-71582788>|<1-100>|ignore-time <1-35791394>}

#### F00524

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-migration <5-86400>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00521:probe` (probe_template): max-metric router-lsa on-proc-migration <5-86400>

#### F00525

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-migration <5-86400>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00522:probe` (probe_template): max-metric router-lsa on-proc-migration <5-86400>

#### F00526

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-migration wait-for-bgp`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00523:probe` (probe_template): max-metric router-lsa on-proc-migration wait-for-bgp

#### F00527

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-migration wait-for-bgp`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00524:probe` (probe_template): max-metric router-lsa on-proc-migration wait-for-bgp

#### F00528

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-restart <5-86400>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command but provides no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00525:probe` (probe_template): max-metric router-lsa on-proc-restart <5-86400>

#### F00529

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-restart <5-86400>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00526:probe` (probe_template): max-metric router-lsa on-proc-restart <5-86400>

#### F00530

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-restart wait-for-bgp`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00527:probe` (probe_template): max-metric router-lsa on-proc-restart wait-for-bgp

#### F00531

- Status: unresolved
- Probe template: `max-metric router-lsa on-proc-restart wait-for-bgp`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00528:probe` (probe_template): max-metric router-lsa on-proc-restart wait-for-bgp

#### F00532

- Status: unresolved
- Probe template: `max-metric router-lsa on-startup <5-86400>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00529:probe` (probe_template): max-metric router-lsa on-startup <5-86400>

#### F00533

- Status: unresolved
- Probe template: `max-metric router-lsa on-startup <5-86400>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command but provides no manual evidence or coverage inventory to support that no supplied manual topic matches it.
- Evidence `P00530:probe` (probe_template): max-metric router-lsa on-startup <5-86400>

#### F00534

- Status: unresolved
- Probe template: `max-metric router-lsa on-startup wait-for-bgp`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command but does not substantiate the asserted absence of a matching manual command topic.
- Evidence `P00531:probe` (probe_template): max-metric router-lsa on-startup wait-for-bgp

#### F00535

- Status: unresolved
- Probe template: `max-metric router-lsa on-startup wait-for-bgp`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe evidence alone cannot establish command undercoverage because no manual-topic evidence is supplied.
- Evidence `P00532:probe` (probe_template): max-metric router-lsa on-startup wait-for-bgp

#### F00536

- Status: unresolved
- Probe template: `max-metric router-lsa on-switchover <5-86400>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence identifies the probe template only; it cannot support a determination that matching documentation is absent.
- Evidence `P00533:probe` (probe_template): max-metric router-lsa on-switchover <5-86400>

#### F00537

- Status: unresolved
- Probe template: `max-metric router-lsa on-switchover <5-86400>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence identifies the probe command but supplies no manual-command evidence to establish whether a matching topic is absent.
- Evidence `P00534:probe` (probe_template): max-metric router-lsa on-switchover <5-86400>

#### F00538

- Status: unresolved
- Probe template: `max-metric router-lsa on-switchover wait-for-bgp`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence identifies the probe command but supplies no manual-command evidence to establish whether a matching topic is absent.
- Evidence `P00535:probe` (probe_template): max-metric router-lsa on-switchover wait-for-bgp

#### F00539

- Status: unresolved
- Probe template: `max-metric router-lsa on-switchover wait-for-bgp`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence identifies the probe command but supplies no manual-command evidence to establish whether a matching topic is absent.
- Evidence `P00536:probe` (probe_template): max-metric router-lsa on-switchover wait-for-bgp

#### F00540

- Status: unresolved
- Probe template: `max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] external-lsa <1-16777215>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence identifies the probe command but supplies no manual-command evidence to establish whether a matching topic is absent.
- Evidence `P00537:probe` (probe_template): max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] external-lsa <1-16777215>

#### F00541

- Status: unresolved
- Probe template: `max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] external-lsa [summary-lsa|<1-16777215> include-stub|include-stub]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00538:probe` (probe_template): max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] external-lsa [summary-lsa|<1-16777215> include-stub|include-stub]

#### F00542

- Status: unresolved
- Probe template: `max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] summary-lsa [external-lsa]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00539:probe` (probe_template): max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] summary-lsa [external-lsa]

#### F00543

- Status: unresolved
- Probe template: `max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] summary-lsa {<1-16777215> [include-stub]|include-stub}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00540:probe` (probe_template): max-metric router-lsa [include-stub|on-switchover {wait-for-bgp|<5-86400>} [include-stub]|on-proc-restart {<5-86400>|wait-for-bgp} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {<5-86400>|wait-for-bgp} [include-stub]] summary-lsa {<1-16777215> [include-stub]|include-stub}

#### F00544

- Status: unresolved
- Probe template: `max-metric router-lsa [no-abr-off]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual-topic evidence sufficient to verify that no matching command topic exists.
- Evidence `P00541:probe` (probe_template): max-metric router-lsa [no-abr-off]

#### F00545

- Status: unresolved
- Probe template: `max-metric router-lsa [no-abr-off]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00542:probe` (probe_template): max-metric router-lsa [no-abr-off]

#### F00546

- Status: unresolved
- Probe template: `max-metric router-lsa [on-proc-migration {wait-for-bgp|<5-86400>}|on-proc-restart {wait-for-bgp|<5-86400>}|on-startup {wait-for-bgp|<5-86400>}|on-switchover {<5-86400>|wait-for-bgp}] include-stub`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00543:probe` (probe_template): max-metric router-lsa [on-proc-migration {wait-for-bgp|<5-86400>}|on-proc-restart {wait-for-bgp|<5-86400>}|on-startup {wait-for-bgp|<5-86400>}|on-switchover {<5-86400>|wait-for-bgp}] include-stub

#### F00547

- Status: unresolved
- Probe template: `max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] external-lsa [summary-lsa]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00544:probe` (probe_template): max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] external-lsa [summary-lsa]

#### F00548

- Status: unresolved
- Probe template: `max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] external-lsa {<1-16777215> [include-stub]|include-stub}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00545:probe` (probe_template): max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] external-lsa {<1-16777215> [include-stub]|include-stub}

#### F00549

- Status: unresolved
- Probe template: `max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] summary-lsa <1-16777215>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the Probe command template, but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00546:probe` (probe_template): max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] summary-lsa <1-16777215>

#### F00550

- Status: unresolved
- Probe template: `max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] summary-lsa [include-stub|<1-16777215> include-stub|external-lsa]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The Probe command template is evidenced, but the supplied evidence does not establish the absence of a corresponding manual command topic.
- Evidence `P00547:probe` (probe_template): max-metric router-lsa [on-proc-restart {wait-for-bgp|<5-86400>} [include-stub]|on-proc-migration {wait-for-bgp|<5-86400>} [include-stub]|on-startup {wait-for-bgp|<5-86400>} [include-stub]|on-switchover {<5-86400>|wait-for-bgp} [include-stub]|include-stub] summary-lsa [include-stub|<1-16777215> include-stub|external-lsa]

#### F00551

- Status: unresolved
- Probe template: `max-metric router-lsa [on-switchover {wait-for-bgp|<5-86400>}|on-proc-restart {<5-86400>|wait-for-bgp}|on-proc-migration {wait-for-bgp|<5-86400>}|on-startup {<5-86400>|wait-for-bgp}] include-stub`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence supports only the existence of the Probe template; it cannot support a determination that the manuals lack a matching topic.
- Evidence `P00548:probe` (probe_template): max-metric router-lsa [on-switchover {wait-for-bgp|<5-86400>}|on-proc-restart {<5-86400>|wait-for-bgp}|on-proc-migration {wait-for-bgp|<5-86400>}|on-startup {<5-86400>|wait-for-bgp}] include-stub

#### F00552

- Status: unresolved
- Probe template: `maximum interfaces <1-4294967295>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence identifies the Probe command template but contains no manual material to confirm command undercoverage.
- Evidence `P00549:probe` (probe_template): maximum interfaces <1-4294967295>

#### F00553

- Status: unresolved
- Probe template: `maximum interfaces <1-4294967295>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template, but supplies no manual evidence from which to verify that no matching command topic exists.
- Evidence `P00550:probe` (probe_template): maximum interfaces <1-4294967295>

#### F00554

- Status: unresolved
- Probe template: `maximum paths {<1-64>|per-prefix-distribution}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The probe template is evidenced, but there is no supplied manual content to substantiate the asserted absence of a matching command topic.
- Evidence `P00551:probe` (probe_template): maximum paths {<1-64>|per-prefix-distribution}

#### F00555

- Status: unresolved
- Probe template: `maximum paths {<1-64>|per-prefix-distribution}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence identifies the probe template only; it cannot establish command undercoverage without supplied manual-command evidence.
- Evidence `P00552:probe` (probe_template): maximum paths {<1-64>|per-prefix-distribution}

#### F00556

- Status: unresolved
- Probe template: `maximum redistributed-prefixes <1-4294967295> [<1-100>|warning-only]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The supplied evidence confirms the probe template but does not support a determination that the manuals lack a matching command topic.
- Evidence `P00553:probe` (probe_template): maximum redistributed-prefixes <1-4294967295> [<1-100>|warning-only]

#### F00557

- Status: unresolved
- Probe template: `maximum redistributed-prefixes <1-4294967295> [warning-only|<1-100>]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence establishes the probe command, but provides no manual content or command-topic evidence to verify that no supplied manual matches it.
- Evidence `P00554:probe` (probe_template): maximum redistributed-prefixes <1-4294967295> [warning-only|<1-100>]

#### F00558

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe template is evidenced, but the absence of a matching command topic cannot be verified without supplied manual evidence.
- Evidence `P00555:probe` (probe_template): message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}

#### F00559

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence only identifies the interface-context probe template; it does not establish manual command coverage or its absence.
- Evidence `P00556:probe` (probe_template): message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}

#### F00560

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence supports the multi-area probe template only and does not contain manuals or command topics needed to confirm undercoverage.
- Evidence `P00557:probe` (probe_template): message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}

#### F00561

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00558:probe` (probe_template): message-digest-key <1-255> md5 {clear LINE|encrypted LINE|LINE}

#### F00562

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {clear LINE|LINE|encrypted LINE}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00559:probe` (probe_template): message-digest-key <1-255> md5 {clear LINE|LINE|encrypted LINE}

#### F00563

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {clear LINE|LINE|encrypted LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00560:probe` (probe_template): message-digest-key <1-255> md5 {clear LINE|LINE|encrypted LINE}

#### F00564

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {clear LINE|LINE|encrypted LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00561:probe` (probe_template): message-digest-key <1-255> md5 {clear LINE|LINE|encrypted LINE}

#### F00565

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no manual evidence supporting or refuting the claimed absence of a matching command topic.
- Evidence `P00562:probe` (probe_template): message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}

#### F00566

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no manual evidence supporting or refuting the claimed absence of a matching command topic.
- Evidence `P00563:probe` (probe_template): message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}

#### F00567

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no manual evidence supporting or refuting the claimed absence of a matching command topic.
- Evidence `P00564:probe` (probe_template): message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}

#### F00568

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no manual evidence supporting or refuting the claimed absence of a matching command topic.
- Evidence `P00565:probe` (probe_template): message-digest-key <1-255> md5 {encrypted LINE|clear LINE|LINE}

#### F00569

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {encrypted LINE|LINE|clear LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual-command evidence to verify that no matching command topic exists.
- Evidence `P00566:probe` (probe_template): message-digest-key <1-255> md5 {encrypted LINE|LINE|clear LINE}

#### F00570

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {encrypted LINE|LINE|clear LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual-command evidence to verify that no matching command topic exists for the multi-area view.
- Evidence `P00567:probe` (probe_template): message-digest-key <1-255> md5 {encrypted LINE|LINE|clear LINE}

#### F00571

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {encrypted LINE|LINE|clear LINE}`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual-command evidence to verify that no matching command topic exists for the sham-link view.
- Evidence `P00568:probe` (probe_template): message-digest-key <1-255> md5 {encrypted LINE|LINE|clear LINE}

#### F00572

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual-command evidence to verify that no matching command topic exists for the area view.
- Evidence `P00569:probe` (probe_template): message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}

#### F00573

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists.
- Evidence `P00570:probe` (probe_template): message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}

#### F00574

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists for the multi-area view.
- Evidence `P00571:probe` (probe_template): message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}

#### F00575

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists for the virtual-link view.
- Evidence `P00572:probe` (probe_template): message-digest-key <1-255> md5 {LINE|clear LINE|encrypted LINE}

#### F00576

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists for the area view.
- Evidence `P00573:probe` (probe_template): message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}

#### F00577

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command template, but provides no supplied manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00574:probe` (probe_template): message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}

#### F00578

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command template, but does not include manuals or search results supporting the claimed absence of a matching topic for the multi-area view.
- Evidence `P00575:probe` (probe_template): message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}

#### F00579

- Status: unresolved
- Probe template: `message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command template, but cannot substantiate that supplied manuals lack a matching sham-link command topic.
- Evidence `P00576:probe` (probe_template): message-digest-key <1-255> md5 {LINE|encrypted LINE|clear LINE}

#### F00580

- Status: unresolved
- Probe template: `metric-type {delay|te-metric}`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command template, but provides no manual evidence to determine whether a matching command topic is absent.
- Evidence `P00577:probe` (probe_template): metric-type {delay|te-metric}

#### F00581

- Status: unresolved
- Probe template: `microloop avoidance disable`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00578:probe` (probe_template): microloop avoidance disable

#### F00582

- Status: unresolved
- Probe template: `microloop avoidance [protected|segment-routing|rib-update-delay <1-600000>]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The supplied evidence identifies the probe template only; it cannot substantiate the asserted absence of a matching manual command topic.
- Evidence `P00579:probe` (probe_template): microloop avoidance [protected|segment-routing|rib-update-delay <1-600000>]

#### F00583

- Status: unresolved
- Probe template: `microloop avoidance [segment-routing|protected|rib-update-delay <1-600000>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe template is evidenced, but no manuals or search results are supplied to confirm or dismiss the claimed command undercoverage.
- Evidence `P00580:probe` (probe_template): microloop avoidance [segment-routing|protected|rib-update-delay <1-600000>]

#### F00584

- Status: unresolved
- Probe template: `monitor-convergence`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence shows the probe command only and does not support a determination about whether the supplied manuals contain a matching topic.
- Evidence `P00581:probe` (probe_template): monitor-convergence

#### F00585

- Status: unresolved
- Probe template: `mpls ldp auto-config`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual-command inventory or manual-topic evidence to support or refute the claimed absence of coverage.
- Evidence `P00582:probe` (probe_template): mpls ldp auto-config

#### F00586

- Status: unresolved
- Probe template: `mpls ldp sync`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual-command inventory or manual-topic evidence to support or refute the claimed absence of coverage.
- Evidence `P00583:probe` (probe_template): mpls ldp sync

#### F00587

- Status: unresolved
- Probe template: `mpls ldp sync-igp-shortcuts`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual-command inventory or manual-topic evidence to support or refute the claimed absence of coverage.
- Evidence `P00584:probe` (probe_template): mpls ldp sync-igp-shortcuts

#### F00588

- Status: unresolved
- Probe template: `mpls ldp sync [disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe command. It provides no manual-command inventory or manual-topic evidence to support or refute the claimed absence of coverage.
- Evidence `P00585:probe` (probe_template): mpls ldp sync [disable]

#### F00589

- Status: unresolved
- Probe template: `mpls ldp sync [disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but does not provide manual content or matching results sufficient to verify that no supplied manual topic covers it.
- Evidence `P00586:probe` (probe_template): mpls ldp sync [disable]

#### F00590

- Status: unresolved
- Probe template: `mpls ldp {auto-config|sync|sync-igp-shortcuts}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but does not provide manual content or matching results sufficient to verify that no supplied manual topic covers it.
- Evidence `P00587:probe` (probe_template): mpls ldp {auto-config|sync|sync-igp-shortcuts}

#### F00591

- Status: unresolved
- Probe template: `mpls ldp {sync [disable]|sync-igp-shortcuts disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but does not provide manual content or matching results sufficient to verify that no supplied manual topic covers it.
- Evidence `P00588:probe` (probe_template): mpls ldp {sync [disable]|sync-igp-shortcuts disable}

#### F00592

- Status: unresolved
- Probe template: `mpls traffic-eng`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but does not provide manual content or matching results sufficient to verify that no supplied manual topic covers it.
- Evidence `P00589:probe` (probe_template): mpls traffic-eng

#### F00593

- Status: unresolved
- Probe template: `mpls traffic-eng router-id [preconfigure] GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the Probe command. It provides no manual content or corpus evidence to verify that no matching command topic exists.
- Evidence `P00590:probe` (probe_template): mpls traffic-eng router-id [preconfigure] GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00594

- Status: unresolved
- Probe template: `mpls traffic-eng router-id [preconfigure] MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the Probe command. It provides no manual content or corpus evidence to verify that no matching command topic exists.
- Evidence `P00591:probe` (probe_template): mpls traffic-eng router-id [preconfigure] MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00595

- Status: unresolved
- Probe template: `mpls traffic-eng router-id {Serial <R/S/I/P>|<A.B.C.D>|preconfigure Serial <R/S/I/P>|Loopback <0-2147483647>|Null <0-0>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the Probe command. It provides no manual content or corpus evidence to verify that no matching command topic exists.
- Evidence `P00592:probe` (probe_template): mpls traffic-eng router-id {Serial <R/S/I/P>|<A.B.C.D>|preconfigure Serial <R/S/I/P>|Loopback <0-2147483647>|Null <0-0>}

#### F00596

- Status: unresolved
- Probe template: `mpls traffic-eng {multicast-intact|ldp-sync-update|igp-intact|autoroute-exclude route-policy <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes only the Probe command. It provides no manual content or corpus evidence to verify that no matching command topic exists.
- Evidence `P00593:probe` (probe_template): mpls traffic-eng {multicast-intact|ldp-sync-update|igp-intact|autoroute-exclude route-policy <WORD>}

#### F00597

- Status: unresolved
- Probe template: `mtu-ignore`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "mtu-ignore". It does not provide the supplied manual corpus or demonstrate that no matching command topic exists for the area semantic view.
- Evidence `P00594:probe` (probe_template): mtu-ignore

#### F00598

- Status: unresolved
- Probe template: `mtu-ignore`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "mtu-ignore". It does not provide the supplied manual corpus or demonstrate that no matching command topic exists for the interface semantic view.
- Evidence `P00595:probe` (probe_template): mtu-ignore

#### F00599

- Status: unresolved
- Probe template: `mtu-ignore`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "mtu-ignore". It does not provide the supplied manual corpus or demonstrate that no matching command topic exists for the multi-area semantic view.
- Evidence `P00596:probe` (probe_template): mtu-ignore

#### F00600

- Status: unresolved
- Probe template: `mtu-ignore`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "mtu-ignore". It does not provide the supplied manual corpus or demonstrate that no matching command topic exists for the router semantic view.
- Evidence `P00597:probe` (probe_template): mtu-ignore

#### F00601

- Status: unresolved
- Probe template: `mtu-ignore`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence sufficient to verify that no matching manual topic exists.
- Evidence `P00598:probe` (probe_template): mtu-ignore

#### F00602

- Status: unresolved
- Probe template: `mtu-ignore {disable|enable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template but does not substantiate the asserted absence of a matching command topic in the supplied manuals.
- Evidence `P00599:probe` (probe_template): mtu-ignore {disable|enable}

#### F00603

- Status: unresolved
- Probe template: `mtu-ignore {disable|enable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence identifies the interface probe template only; it cannot establish manual undercoverage without evidence of the relevant manual topics or corpus.
- Evidence `P00600:probe` (probe_template): mtu-ignore {disable|enable}

#### F00604

- Status: unresolved
- Probe template: `mtu-ignore {disable|enable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence identifies the multi-area probe template only and is insufficient to verify the claimed absence of a matching manual command topic.
- Evidence `P00601:probe` (probe_template): mtu-ignore {disable|enable}

#### F00605

- Status: unresolved
- Probe template: `mtu-ignore {disable|enable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-topic inventory to verify that no matching manual command exists.
- Evidence `P00602:probe` (probe_template): mtu-ignore {disable|enable}

#### F00606

- Status: unresolved
- Probe template: `mtu-ignore {disable|enable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but does not substantiate the asserted absence of a matching command topic in supplied manuals for the VRF view.
- Evidence `P00603:probe` (probe_template): mtu-ignore {disable|enable}

#### F00607

- Status: unresolved
- Probe template: `mtu-ignore {enable|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template alone cannot establish command undercoverage; no manual evidence is supplied to assess whether an area-view command topic matches.
- Evidence `P00604:probe` (probe_template): mtu-ignore {enable|disable}

#### F00608

- Status: unresolved
- Probe template: `mtu-ignore {enable|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence shows only the interface-view probe template and cannot support or refute the claim that the manuals lack a matching command topic.
- Evidence `P00605:probe` (probe_template): mtu-ignore {enable|disable}

#### F00609

- Status: unresolved
- Probe template: `mtu-ignore {enable|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-topic inventory to verify that no matching topic exists.
- Evidence `P00606:probe` (probe_template): mtu-ignore {enable|disable}

#### F00610

- Status: unresolved
- Probe template: `multi-area-interface GigabitEthernet 0/0/0/0`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but does not contain manual evidence sufficient to confirm or dismiss the claimed absence of a matching command topic.
- Evidence `P00607:probe` (probe_template): multi-area-interface GigabitEthernet 0/0/0/0

#### F00611

- Status: unresolved
- Probe template: `multi-area-interface GigabitEthernet <R/S/I/P/B or R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe template is evidenced, but there is no manual content or topic listing to support a determination of command undercoverage.
- Evidence `P00608:probe` (probe_template): multi-area-interface GigabitEthernet <R/S/I/P/B or R/S/I/P>

#### F00612

- Status: unresolved
- Probe template: `multi-area-interface MgmtEth 0/RP0/CPU0/0`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The provided evidence only identifies the probe template and cannot establish whether the supplied manuals contain a matching command topic.
- Evidence `P00609:probe` (probe_template): multi-area-interface MgmtEth 0/RP0/CPU0/0

#### F00613

- Status: unresolved
- Probe template: `multi-area-interface MgmtEth <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00610:probe` (probe_template): multi-area-interface MgmtEth <R/S/I/P>

#### F00614

- Status: unresolved
- Probe template: `multi-area-interface Serial <R/S/I/P>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00611:probe` (probe_template): multi-area-interface Serial <R/S/I/P>

#### F00615

- Status: unresolved
- Probe template: `name <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00612:probe` (probe_template): name <WORD>

#### F00616

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [cost <1-65535>|database-filter all out|poll-interval <0-4294967295>]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command, but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00613:probe` (probe_template): neighbor <A.B.C.D> [cost <1-65535>|database-filter all out|poll-interval <0-4294967295>]

#### F00617

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [cost <1-65535>|database-filter all out|priority <0-255>|poll-interval <0-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template, but provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00614:probe` (probe_template): neighbor <A.B.C.D> [cost <1-65535>|database-filter all out|priority <0-255>|poll-interval <0-65535>]

#### F00618

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [cost <1-65535>|poll-interval <0-4294967295>|database-filter all out]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template, but provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00615:probe` (probe_template): neighbor <A.B.C.D> [cost <1-65535>|poll-interval <0-4294967295>|database-filter all out]

#### F00619

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [cost <1-65535>|poll-interval <0-65535>|database-filter all out|priority <0-255>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template, but provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00616:probe` (probe_template): neighbor <A.B.C.D> [cost <1-65535>|poll-interval <0-65535>|database-filter all out|priority <0-255>]

#### F00620

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [cost <1-65535>|poll-interval <0-65535>|priority <0-255>|database-filter all out]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template, but provides no supplied manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00617:probe` (probe_template): neighbor <A.B.C.D> [cost <1-65535>|poll-interval <0-65535>|priority <0-255>|database-filter all out]

#### F00621

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [cost <1-65535>|priority <0-255>|database-filter all out|poll-interval <0-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus information to establish undercoverage.
- Evidence `P00618:probe` (probe_template): neighbor <A.B.C.D> [cost <1-65535>|priority <0-255>|database-filter all out|poll-interval <0-65535>]

#### F00622

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [cost <1-65535>|priority <0-255>|poll-interval <0-65535>|database-filter all out]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus information to establish undercoverage.
- Evidence `P00619:probe` (probe_template): neighbor <A.B.C.D> [cost <1-65535>|priority <0-255>|poll-interval <0-65535>|database-filter all out]

#### F00623

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [database-filter all out|cost <1-65535>|poll-interval <0-4294967295>]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus information to establish undercoverage.
- Evidence `P00620:probe` (probe_template): neighbor <A.B.C.D> [database-filter all out|cost <1-65535>|poll-interval <0-4294967295>]

#### F00624

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [database-filter all out|poll-interval <0-4294967295>|cost <1-65535>]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus information to establish undercoverage.
- Evidence `P00621:probe` (probe_template): neighbor <A.B.C.D> [database-filter all out|poll-interval <0-4294967295>|cost <1-65535>]

#### F00625

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [database-filter all out|poll-interval <0-65535>|cost <1-65535>|priority <0-255>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence from which to verify that no matching topic exists.
- Evidence `P00622:probe` (probe_template): neighbor <A.B.C.D> [database-filter all out|poll-interval <0-65535>|cost <1-65535>|priority <0-255>]

#### F00626

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [database-filter all out|poll-interval <0-65535>|priority <0-255>|cost <1-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence shows only the probe template and cannot substantiate the asserted absence of a matching manual command topic.
- Evidence `P00623:probe` (probe_template): neighbor <A.B.C.D> [database-filter all out|poll-interval <0-65535>|priority <0-255>|cost <1-65535>]

#### F00627

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [database-filter all out|priority <0-255>|cost <1-65535>|poll-interval <0-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is evidenced, but no supplied manual content supports a determination of command undercoverage.
- Evidence `P00624:probe` (probe_template): neighbor <A.B.C.D> [database-filter all out|priority <0-255>|cost <1-65535>|poll-interval <0-65535>]

#### F00628

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [poll-interval <0-4294967295>|cost <1-65535>|database-filter all out]`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe template only; it does not provide manual-command material needed to confirm that no matching topic exists.
- Evidence `P00625:probe` (probe_template): neighbor <A.B.C.D> [poll-interval <0-4294967295>|cost <1-65535>|database-filter all out]

#### F00629

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [poll-interval <0-65535>|cost <1-65535>|priority <0-255>|database-filter all out]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command template but provides no supplied manual content or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00626:probe` (probe_template): neighbor <A.B.C.D> [poll-interval <0-65535>|cost <1-65535>|priority <0-255>|database-filter all out]

#### F00630

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [poll-interval <0-65535>|database-filter all out|cost <1-65535>|priority <0-255>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command template but provides no supplied manual content or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00627:probe` (probe_template): neighbor <A.B.C.D> [poll-interval <0-65535>|database-filter all out|cost <1-65535>|priority <0-255>]

#### F00631

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [poll-interval <0-65535>|database-filter all out|priority <0-255>|cost <1-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command template but provides no supplied manual content or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00628:probe` (probe_template): neighbor <A.B.C.D> [poll-interval <0-65535>|database-filter all out|priority <0-255>|cost <1-65535>]

#### F00632

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [poll-interval <0-65535>|priority <0-255>|cost <1-65535>|database-filter all out]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command template but provides no supplied manual content or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00629:probe` (probe_template): neighbor <A.B.C.D> [poll-interval <0-65535>|priority <0-255>|cost <1-65535>|database-filter all out]

#### F00633

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [poll-interval <0-65535>|priority <0-255>|database-filter all out|cost <1-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00630:probe` (probe_template): neighbor <A.B.C.D> [poll-interval <0-65535>|priority <0-255>|database-filter all out|cost <1-65535>]

#### F00634

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [priority <0-255>|cost <1-65535>|database-filter all out|poll-interval <0-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00631:probe` (probe_template): neighbor <A.B.C.D> [priority <0-255>|cost <1-65535>|database-filter all out|poll-interval <0-65535>]

#### F00635

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [priority <0-255>|database-filter all out|cost <1-65535>|poll-interval <0-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00632:probe` (probe_template): neighbor <A.B.C.D> [priority <0-255>|database-filter all out|cost <1-65535>|poll-interval <0-65535>]

#### F00636

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [priority <0-255>|database-filter all out|poll-interval <0-65535>|cost <1-65535>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command template but supplies no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00633:probe` (probe_template): neighbor <A.B.C.D> [priority <0-255>|database-filter all out|poll-interval <0-65535>|cost <1-65535>]

#### F00637

- Status: unresolved
- Probe template: `neighbor <A.B.C.D> [priority <0-255>|poll-interval <0-65535>|cost <1-65535>|database-filter all out]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but contains no supplied manual-command evidence from which to determine whether a matching topic exists.
- Evidence `P00634:probe` (probe_template): neighbor <A.B.C.D> [priority <0-255>|poll-interval <0-65535>|cost <1-65535>|database-filter all out]

#### F00638

- Status: unresolved
- Probe template: `network point-to-multipoint`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but does not provide manual coverage evidence to support or refute the asserted absence of a matching topic.
- Evidence `P00635:probe` (probe_template): network point-to-multipoint

#### F00639

- Status: unresolved
- Probe template: `network point-to-multipoint`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but does not include supplied manual-command material needed to assess the undercoverage claim for the interface view.
- Evidence `P00636:probe` (probe_template): network point-to-multipoint

#### F00640

- Status: unresolved
- Probe template: `network point-to-multipoint`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but lacks supplied manual-command evidence needed to determine whether a matching router-view topic exists.
- Evidence `P00637:probe` (probe_template): network point-to-multipoint

#### F00641

- Status: unresolved
- Probe template: `network point-to-multipoint`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00638:probe` (probe_template): network point-to-multipoint

#### F00642

- Status: unresolved
- Probe template: `network {broadcast|non-broadcast|point-to-multipoint non-broadcast|point-to-point}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template is evidenced, but the absence of a matching command topic cannot be verified without supplied manual evidence.
- Evidence `P00639:probe` (probe_template): network {broadcast|non-broadcast|point-to-multipoint non-broadcast|point-to-point}

#### F00643

- Status: unresolved
- Probe template: `network {broadcast|non-broadcast|point-to-multipoint non-broadcast|point-to-point}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe template only; it does not substantiate the claimed lack of matching manual coverage for the interface semantic view.
- Evidence `P00640:probe` (probe_template): network {broadcast|non-broadcast|point-to-multipoint non-broadcast|point-to-point}

#### F00644

- Status: unresolved
- Probe template: `network {broadcast|non-broadcast|point-to-point|point-to-multipoint non-broadcast}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supports that this probe template was assessed, but contains no manual-command evidence sufficient to confirm undercoverage.
- Evidence `P00641:probe` (probe_template): network {broadcast|non-broadcast|point-to-point|point-to-multipoint non-broadcast}

#### F00645

- Status: unresolved
- Probe template: `network {broadcast|non-broadcast|point-to-point|point-to-multipoint non-broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command inventory to verify that no matching command topic exists.
- Evidence `P00642:probe` (probe_template): network {broadcast|non-broadcast|point-to-point|point-to-multipoint non-broadcast}

#### F00646

- Status: unresolved
- Probe template: `network {non-broadcast|broadcast|point-to-multipoint non-broadcast|point-to-point}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command inventory to verify that no matching command topic exists.
- Evidence `P00643:probe` (probe_template): network {non-broadcast|broadcast|point-to-multipoint non-broadcast|point-to-point}

#### F00647

- Status: unresolved
- Probe template: `network {non-broadcast|broadcast|point-to-point|point-to-multipoint non-broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command inventory to verify that no matching command topic exists.
- Evidence `P00644:probe` (probe_template): network {non-broadcast|broadcast|point-to-point|point-to-multipoint non-broadcast}

#### F00648

- Status: unresolved
- Probe template: `network {non-broadcast|point-to-multipoint non-broadcast|broadcast|point-to-point}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command inventory to verify that no matching command topic exists.
- Evidence `P00645:probe` (probe_template): network {non-broadcast|point-to-multipoint non-broadcast|broadcast|point-to-point}

#### F00649

- Status: unresolved
- Probe template: `network {non-broadcast|point-to-multipoint non-broadcast|point-to-point|broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00646:probe` (probe_template): network {non-broadcast|point-to-multipoint non-broadcast|point-to-point|broadcast}

#### F00650

- Status: unresolved
- Probe template: `network {non-broadcast|point-to-point|broadcast|point-to-multipoint non-broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00647:probe` (probe_template): network {non-broadcast|point-to-point|broadcast|point-to-multipoint non-broadcast}

#### F00651

- Status: unresolved
- Probe template: `network {non-broadcast|point-to-point|point-to-multipoint non-broadcast|broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00648:probe` (probe_template): network {non-broadcast|point-to-point|point-to-multipoint non-broadcast|broadcast}

#### F00652

- Status: unresolved
- Probe template: `network {non-broadcast|point-to-point|point-to-multipoint non-broadcast|broadcast}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual-command evidence to verify that no matching command topic exists in the VRF semantic view.
- Evidence `P00649:probe` (probe_template): network {non-broadcast|point-to-point|point-to-multipoint non-broadcast|broadcast}

#### F00653

- Status: unresolved
- Probe template: `network {point-to-multipoint non-broadcast|broadcast|non-broadcast|point-to-point}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to verify that no matching manual command exists.
- Evidence `P00650:probe` (probe_template): network {point-to-multipoint non-broadcast|broadcast|non-broadcast|point-to-point}

#### F00654

- Status: unresolved
- Probe template: `network {point-to-multipoint non-broadcast|broadcast|point-to-point|non-broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but does not support the claimed absence of a matching command topic in the supplied manuals.
- Evidence `P00651:probe` (probe_template): network {point-to-multipoint non-broadcast|broadcast|point-to-point|non-broadcast}

#### F00655

- Status: unresolved
- Probe template: `network {point-to-multipoint non-broadcast|point-to-point|broadcast|non-broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: Only the probe template is supplied. No manual-command evidence is available to confirm command undercoverage.
- Evidence `P00652:probe` (probe_template): network {point-to-multipoint non-broadcast|point-to-point|broadcast|non-broadcast}

#### F00656

- Status: unresolved
- Probe template: `network {point-to-multipoint non-broadcast|point-to-point|non-broadcast|broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe template only and cannot establish whether a corresponding manual command topic is absent.
- Evidence `P00653:probe` (probe_template): network {point-to-multipoint non-broadcast|point-to-point|non-broadcast|broadcast}

#### F00657

- Status: unresolved
- Probe template: `network {point-to-point|broadcast|non-broadcast|point-to-multipoint non-broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00654:probe` (probe_template): network {point-to-point|broadcast|non-broadcast|point-to-multipoint non-broadcast}

#### F00658

- Status: unresolved
- Probe template: `network {point-to-point|broadcast|point-to-multipoint non-broadcast|non-broadcast}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00655:probe` (probe_template): network {point-to-point|broadcast|point-to-multipoint non-broadcast|non-broadcast}

#### F00659

- Status: unresolved
- Probe template: `network {point-to-point|broadcast|point-to-multipoint non-broadcast|non-broadcast}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00656:probe` (probe_template): network {point-to-point|broadcast|point-to-multipoint non-broadcast|non-broadcast}

#### F00660

- Status: unresolved
- Probe template: `network {point-to-point|non-broadcast|broadcast|point-to-multipoint non-broadcast}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to support or refute the claimed absence of a matching topic.
- Evidence `P00657:probe` (probe_template): network {point-to-point|non-broadcast|broadcast|point-to-multipoint non-broadcast}

#### F00661

- Status: unresolved
- Probe template: `network {point-to-point|non-broadcast|broadcast|point-to-multipoint non-broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence or manual corpus information to verify that no matching command topic exists.
- Evidence `P00658:probe` (probe_template): network {point-to-point|non-broadcast|broadcast|point-to-multipoint non-broadcast}

#### F00662

- Status: unresolved
- Probe template: `network {point-to-point|point-to-multipoint non-broadcast|non-broadcast|broadcast}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence or manual corpus information to verify that no matching command topic exists.
- Evidence `P00659:probe` (probe_template): network {point-to-point|point-to-multipoint non-broadcast|non-broadcast|broadcast}

#### F00663

- Status: unresolved
- Probe template: `nsf cisco [enforce global]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence or manual corpus information to verify that no matching command topic exists.
- Evidence `P00660:probe` (probe_template): nsf cisco [enforce global]

#### F00664

- Status: unresolved
- Probe template: `nsf cisco [enforce global]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence or manual corpus information to verify that no matching command topic exists.
- Evidence `P00661:probe` (probe_template): nsf cisco [enforce global]

#### F00665

- Status: unresolved
- Probe template: `nsf ietf [helper disable|strict-lsa-checking]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template, but does not provide manual-command evidence sufficient to verify that no matching command topic exists.
- Evidence `P00662:probe` (probe_template): nsf ietf [helper disable|strict-lsa-checking]

#### F00666

- Status: unresolved
- Probe template: `nsf ietf [strict-lsa-checking|helper disable]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template, but does not provide manual-command evidence sufficient to verify that no matching command topic exists.
- Evidence `P00663:probe` (probe_template): nsf ietf [strict-lsa-checking|helper disable]

#### F00667

- Status: unresolved
- Probe template: `nsf {interval <90-3600>|lifetime <90-1800>|wait-time <1-120>|flush-delay-time <1-3600>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template, but does not provide manual-command evidence sufficient to verify that no matching command topic exists.
- Evidence `P00664:probe` (probe_template): nsf {interval <90-3600>|lifetime <90-1800>|wait-time <1-120>|flush-delay-time <1-3600>}

#### F00668

- Status: unresolved
- Probe template: `nsf {interval <90-3600>|wait-time <1-120>|flush-delay-time <1-3600>|lifetime <90-1800>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template, but does not provide manual-command evidence sufficient to verify that no matching command topic exists.
- Evidence `P00665:probe` (probe_template): nsf {interval <90-3600>|wait-time <1-120>|flush-delay-time <1-3600>|lifetime <90-1800>}

#### F00669

- Status: unresolved
- Probe template: `nsr`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "nsr"; it provides no supplied manual corpus or command-coverage evidence to verify that no matching manual topic exists.
- Evidence `P00666:probe` (probe_template): nsr

#### F00670

- Status: unresolved
- Probe template: `nsr disable`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "nsr disable"; it does not substantiate the asserted absence of a corresponding command topic in the manuals.
- Evidence `P00667:probe` (probe_template): nsr disable

#### F00671

- Status: unresolved
- Probe template: `nssa`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "nssa"; no manual evidence is supplied to support or refute the claimed command undercoverage.
- Evidence `P00668:probe` (probe_template): nssa

#### F00672

- Status: unresolved
- Probe template: `nssa no-redistribution`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template "nssa no-redistribution"; it cannot establish that the supplied manuals contain no matching command topic.
- Evidence `P00669:probe` (probe_template): nssa no-redistribution

#### F00673

- Status: unresolved
- Probe template: `nssa no-summary`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent.
- Evidence `P00670:probe` (probe_template): nssa no-summary

#### F00674

- Status: unresolved
- Probe template: `nssa translate type7 always`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent.
- Evidence `P00671:probe` (probe_template): nssa translate type7 always

#### F00675

- Status: unresolved
- Probe template: `nssa [no-redistribution|no-summary] default-information-originate`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent.
- Evidence `P00672:probe` (probe_template): nssa [no-redistribution|no-summary] default-information-originate

#### F00676

- Status: unresolved
- Probe template: `nssa [no-redistribution|no-summary] default-information-originate metric <1-16777214>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe command is evidenced, but no supplied manual evidence establishes whether a matching command topic is absent.
- Evidence `P00673:probe` (probe_template): nssa [no-redistribution|no-summary] default-information-originate metric <1-16777214>

#### F00677

- Status: unresolved
- Probe template: `nssa [no-redistribution|no-summary] default-information-originate metric-type <1-2>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify the asserted absence of a matching manual command.
- Evidence `P00674:probe` (probe_template): nssa [no-redistribution|no-summary] default-information-originate metric-type <1-2>

#### F00678

- Status: unresolved
- Probe template: `nssa [no-redistribution|no-summary] default-information-originate {no-summary|metric-type <1-2> [no-summary|no-redistribution]|metric <1-16777214> {no-summary|no-redistribution}|no-redistribution}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify the asserted absence of a matching manual command.
- Evidence `P00675:probe` (probe_template): nssa [no-redistribution|no-summary] default-information-originate {no-summary|metric-type <1-2> [no-summary|no-redistribution]|metric <1-16777214> {no-summary|no-redistribution}|no-redistribution}

#### F00679

- Status: unresolved
- Probe template: `nssa [no-summary|no-redistribution] default-information-originate metric <1-16777214>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify the asserted absence of a matching manual command.
- Evidence `P00676:probe` (probe_template): nssa [no-summary|no-redistribution] default-information-originate metric <1-16777214>

#### F00680

- Status: unresolved
- Probe template: `nssa [no-summary|no-redistribution] default-information-originate metric-type <1-2>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but provides no manual corpus or command-topic evidence to verify the asserted absence of a matching manual command.
- Evidence `P00677:probe` (probe_template): nssa [no-summary|no-redistribution] default-information-originate metric-type <1-2>

#### F00681

- Status: unresolved
- Probe template: `nssa [no-summary|no-redistribution] default-information-originate [metric <1-16777214> {no-redistribution|no-summary}|no-redistribution|metric-type <1-2> {no-redistribution|no-summary}|no-summary]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template only. It does not provide manual content or search results sufficient to verify that no matching command topic exists.
- Evidence `P00678:probe` (probe_template): nssa [no-summary|no-redistribution] default-information-originate [metric <1-16777214> {no-redistribution|no-summary}|no-redistribution|metric-type <1-2> {no-redistribution|no-summary}|no-summary]

#### F00682

- Status: unresolved
- Probe template: `nssa [no-summary|no-redistribution] default-information-originate {metric <1-16777214> [no-summary|no-redistribution]|no-summary|no-redistribution|metric-type <1-2> {no-summary|no-redistribution}}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence contains only the probe template and cannot substantiate the asserted absence of a corresponding manual command topic.
- Evidence `P00679:probe` (probe_template): nssa [no-summary|no-redistribution] default-information-originate {metric <1-16777214> [no-summary|no-redistribution]|no-summary|no-redistribution|metric-type <1-2> {no-summary|no-redistribution}}

#### F00683

- Status: unresolved
- Probe template: `nssa [no-summary|no-redistribution] default-information-originate {no-redistribution|metric <1-16777214> {no-redistribution|no-summary}|metric-type <1-2> [no-redistribution|no-summary]|no-summary}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe template is evidenced, but no manual evidence is supplied to confirm or dismiss the claimed command undercoverage.
- Evidence `P00680:probe` (probe_template): nssa [no-summary|no-redistribution] default-information-originate {no-redistribution|metric <1-16777214> {no-redistribution|no-summary}|metric-type <1-2> [no-redistribution|no-summary]|no-summary}

#### F00684

- Status: unresolved
- Probe template: `packet-size <576-10000>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence shows the packet-size probe template only; it does not establish whether supplied manuals contain a matching command topic.
- Evidence `P00681:probe` (probe_template): packet-size <576-10000>

#### F00685

- Status: unresolved
- Probe template: `packet-size <576-10000>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to verify that no matching command exists.
- Evidence `P00682:probe` (probe_template): packet-size <576-10000>

#### F00686

- Status: unresolved
- Probe template: `packet-size <576-10000>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to verify that no matching command exists for the multi-area view.
- Evidence `P00683:probe` (probe_template): packet-size <576-10000>

#### F00687

- Status: unresolved
- Probe template: `packet-size <576-10000>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to verify that no matching command exists for the router view.
- Evidence `P00684:probe` (probe_template): packet-size <576-10000>

#### F00688

- Status: unresolved
- Probe template: `packet-size <576-10000>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual corpus or command-topic evidence to verify that no matching command exists for the VRF view.
- Evidence `P00685:probe` (probe_template): packet-size <576-10000>

#### F00689

- Status: unresolved
- Probe template: `passive`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template "passive"; it does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00686:probe` (probe_template): passive

#### F00690

- Status: unresolved
- Probe template: `passive`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template "passive"; it does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00687:probe` (probe_template): passive

#### F00691

- Status: unresolved
- Probe template: `passive`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template "passive"; it does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00688:probe` (probe_template): passive

#### F00692

- Status: unresolved
- Probe template: `passive`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes only the probe template "passive"; it does not provide manual content or coverage data sufficient to verify that no matching command topic exists.
- Evidence `P00689:probe` (probe_template): passive

#### F00693

- Status: unresolved
- Probe template: `passive`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00690:probe` (probe_template): passive

#### F00694

- Status: unresolved
- Probe template: `passive {disable|enable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00691:probe` (probe_template): passive {disable|enable}

#### F00695

- Status: unresolved
- Probe template: `passive {disable|enable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00692:probe` (probe_template): passive {disable|enable}

#### F00696

- Status: unresolved
- Probe template: `passive {disable|enable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence establishes only the probe template. It does not provide manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00693:probe` (probe_template): passive {disable|enable}

#### F00697

- Status: unresolved
- Probe template: `passive {disable|enable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but does not provide manual evidence or a complete manual-command inventory sufficient to verify that no matching command topic exists.
- Evidence `P00694:probe` (probe_template): passive {disable|enable}

#### F00698

- Status: unresolved
- Probe template: `passive {enable|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but does not provide manual evidence or a complete manual-command inventory sufficient to verify that no matching command topic exists.
- Evidence `P00695:probe` (probe_template): passive {enable|disable}

#### F00699

- Status: unresolved
- Probe template: `passive {enable|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but does not provide manual evidence or a complete manual-command inventory sufficient to verify that no matching command topic exists.
- Evidence `P00696:probe` (probe_template): passive {enable|disable}

#### F00700

- Status: unresolved
- Probe template: `passive {enable|disable}`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but does not provide manual evidence or a complete manual-command inventory sufficient to verify that no matching command topic exists.
- Evidence `P00697:probe` (probe_template): passive {enable|disable}

#### F00701

- Status: unresolved
- Probe template: `passive {enable|disable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00698:probe` (probe_template): passive {enable|disable}

#### F00702

- Status: unresolved
- Probe template: `prefix-list <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00699:probe` (probe_template): prefix-list <WORD>

#### F00703

- Status: unresolved
- Probe template: `prefix-metric`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00700:probe` (probe_template): prefix-metric

#### F00704

- Status: unresolved
- Probe template: `prefix-sid [algorithm <128-255>|strict-spf] absolute <16000-1048575> [n-flag-clear|explicit-null]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00701:probe` (probe_template): prefix-sid [algorithm <128-255>|strict-spf] absolute <16000-1048575> [n-flag-clear|explicit-null]

#### F00705

- Status: unresolved
- Probe template: `prefix-sid [algorithm <128-255>|strict-spf] index <0-1048575> [n-flag-clear|explicit-null]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide the supplied manual corpus or command-topic evidence needed to determine whether coverage is absent.
- Evidence `P00702:probe` (probe_template): prefix-sid [algorithm <128-255>|strict-spf] index <0-1048575> [n-flag-clear|explicit-null]

#### F00706

- Status: unresolved
- Probe template: `prefix-sid [strict-spf|algorithm <128-255>] absolute <16000-1048575> [explicit-null|n-flag-clear]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide the supplied manual corpus or command-topic evidence needed to determine whether coverage is absent.
- Evidence `P00703:probe` (probe_template): prefix-sid [strict-spf|algorithm <128-255>] absolute <16000-1048575> [explicit-null|n-flag-clear]

#### F00707

- Status: unresolved
- Probe template: `prefix-sid [strict-spf|algorithm <128-255>] index <0-1048575> [explicit-null|n-flag-clear]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide the supplied manual corpus or command-topic evidence needed to determine whether coverage is absent.
- Evidence `P00704:probe` (probe_template): prefix-sid [strict-spf|algorithm <128-255>] index <0-1048575> [explicit-null|n-flag-clear]

#### F00708

- Status: unresolved
- Probe template: `prefix-suppression`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command only; it does not provide the supplied manual corpus or command-topic evidence needed to determine whether coverage is absent.
- Evidence `P00705:probe` (probe_template): prefix-suppression

#### F00709

- Status: unresolved
- Probe template: `prefix-suppression`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe template but contains no supplied manual content or command index evidence to establish that no matching command topic exists.
- Evidence `P00706:probe` (probe_template): prefix-suppression

#### F00710

- Status: unresolved
- Probe template: `prefix-suppression`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe template but contains no supplied manual content or command index evidence to establish that no matching command topic exists.
- Evidence `P00707:probe` (probe_template): prefix-suppression

#### F00711

- Status: unresolved
- Probe template: `prefix-suppression`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe template but contains no supplied manual content or command index evidence to establish that no matching command topic exists.
- Evidence `P00708:probe` (probe_template): prefix-suppression

#### F00712

- Status: unresolved
- Probe template: `prefix-suppression secondary-address`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe template but contains no supplied manual content or command index evidence to establish that no matching command topic exists.
- Evidence `P00709:probe` (probe_template): prefix-suppression secondary-address

#### F00713

- Status: unresolved
- Probe template: `prefix-suppression secondary-address`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus from which to verify undercoverage.
- Evidence `P00710:probe` (probe_template): prefix-suppression secondary-address

#### F00714

- Status: unresolved
- Probe template: `prefix-suppression secondary-address`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus from which to verify undercoverage.
- Evidence `P00711:probe` (probe_template): prefix-suppression secondary-address

#### F00715

- Status: unresolved
- Probe template: `prefix-suppression secondary-address`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus from which to verify undercoverage.
- Evidence `P00712:probe` (probe_template): prefix-suppression secondary-address

#### F00716

- Status: unresolved
- Probe template: `prefix-suppression [secondary-address] disable`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence identifies the probe command but provides no manual-command evidence or manual corpus from which to verify undercoverage.
- Evidence `P00713:probe` (probe_template): prefix-suppression [secondary-address] disable

#### F00717

- Status: unresolved
- Probe template: `prefix-suppression [secondary-address] disable`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes only the probe template. It contains no manual coverage evidence to support or refute the claimed absence of a matching command topic.
- Evidence `P00714:probe` (probe_template): prefix-suppression [secondary-address] disable

#### F00718

- Status: unresolved
- Probe template: `priority <0-255>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes only the probe template. It contains no manual coverage evidence to support or refute the claimed absence of a matching command topic.
- Evidence `P00715:probe` (probe_template): priority <0-255>

#### F00719

- Status: unresolved
- Probe template: `priority <0-255>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes only the probe template. It contains no manual coverage evidence to support or refute the claimed absence of a matching command topic.
- Evidence `P00716:probe` (probe_template): priority <0-255>

#### F00720

- Status: unresolved
- Probe template: `priority <0-255>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.99
- Review rationale: The supplied evidence establishes only the probe template. It contains no manual coverage evidence to support or refute the claimed absence of a matching command topic.
- Evidence `P00717:probe` (probe_template): priority <0-255>

#### F00721

- Status: unresolved
- Probe template: `priority <0-255>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but contains no supplied manual coverage evidence to substantiate that no matching command topic exists.
- Evidence `P00718:probe` (probe_template): priority <0-255>

#### F00722

- Status: unresolved
- Probe template: `priority <0-255>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but contains no supplied manual coverage evidence to substantiate that no matching command topic exists for the vrf semantic view.
- Evidence `P00719:probe` (probe_template): priority <0-255>

#### F00723

- Status: unresolved
- Probe template: `protocol shutdown [host-mode|on-reload]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but contains no supplied manual coverage evidence to substantiate that no matching command topic exists for the router semantic view.
- Evidence `P00720:probe` (probe_template): protocol shutdown [host-mode|on-reload]

#### F00724

- Status: unresolved
- Probe template: `queue {limit {high|low|medium} <1000-30000>|dispatch {spf-lsa-limit|rate-limited-lsa|flush-lsa|incoming} <30-3000>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but contains no supplied manual coverage evidence to substantiate that no matching command topic exists for the router semantic view.
- Evidence `P00721:probe` (probe_template): queue {limit {high|low|medium} <1000-30000>|dispatch {spf-lsa-limit|rate-limited-lsa|flush-lsa|incoming} <30-3000>}

#### F00725

- Status: unresolved
- Probe template: `queue {limit {high|medium|low} <1000-30000>|dispatch {incoming|flush-lsa|spf-lsa-limit|rate-limited-lsa} <30-3000>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence from which to determine whether a matching command topic exists.
- Evidence `P00722:probe` (probe_template): queue {limit {high|medium|low} <1000-30000>|dispatch {incoming|flush-lsa|spf-lsa-limit|rate-limited-lsa} <30-3000>}

#### F00726

- Status: unresolved
- Probe template: `range <A.B.C.D/prefix/mask> [advertise|not-advertise]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence from which to determine whether a matching command topic exists.
- Evidence `P00723:probe` (probe_template): range <A.B.C.D/prefix/mask> [advertise|not-advertise]

#### F00727

- Status: unresolved
- Probe template: `range <A.B.C.D/prefix/mask> [not-advertise|advertise]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence from which to determine whether a matching command topic exists.
- Evidence `P00724:probe` (probe_template): range <A.B.C.D/prefix/mask> [not-advertise|advertise]

#### F00728

- Status: unresolved
- Probe template: `redistribute`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the probe template. It provides no supplied manual-command evidence from which to determine whether a matching command topic exists.
- Evidence `P00725:probe` (probe_template): redistribute

#### F00729

- Status: unresolved
- Probe template: `redistribute application <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but contains no manual-topic evidence to support or refute the claimed absence of a matching command.
- Evidence `P00726:probe` (probe_template): redistribute application <WORD>

#### F00730

- Status: unresolved
- Probe template: `redistribute application <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but contains no manual-topic evidence to support or refute the claimed absence of a matching command.
- Evidence `P00727:probe` (probe_template): redistribute application <WORD>

#### F00731

- Status: unresolved
- Probe template: `redistribute application <WORD> metric-type {1|2}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but contains no manual-topic evidence to support or refute the claimed absence of a matching command.
- Evidence `P00728:probe` (probe_template): redistribute application <WORD> metric-type {1|2}

#### F00732

- Status: unresolved
- Probe template: `redistribute application <WORD> metric-type {2|1}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe template but contains no manual-topic evidence to support or refute the claimed absence of a matching command.
- Evidence `P00729:probe` (probe_template): redistribute application <WORD> metric-type {2|1}

#### F00733

- Status: unresolved
- Probe template: `redistribute application <WORD> metric {<1-16777214>|use-rib-metric}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-index evidence to verify that no matching command topic exists.
- Evidence `P00730:probe` (probe_template): redistribute application <WORD> metric {<1-16777214>|use-rib-metric}

#### F00734

- Status: unresolved
- Probe template: `redistribute application <WORD> metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-index evidence to verify that no matching command topic exists for the VRF view.
- Evidence `P00731:probe` (probe_template): redistribute application <WORD> metric {<1-16777214>|use-rib-metric}

#### F00735

- Status: unresolved
- Probe template: `redistribute application <WORD> {tag <0-4294967295>|route-policy <WORD>|nssa-only|lsa-type summary}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-index evidence to verify the asserted absence of a matching router-view command topic.
- Evidence `P00732:probe` (probe_template): redistribute application <WORD> {tag <0-4294967295>|route-policy <WORD>|nssa-only|lsa-type summary}

#### F00736

- Status: unresolved
- Probe template: `redistribute application <WORD> {tag <0-4294967295>|route-policy <WORD>|nssa-only|lsa-type summary}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-index evidence to verify the asserted absence of a matching VRF-view command topic.
- Evidence `P00733:probe` (probe_template): redistribute application <WORD> {tag <0-4294967295>|route-policy <WORD>|nssa-only|lsa-type summary}

#### F00737

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template but provides no manual content or coverage inventory to verify that no matching command topic exists.
- Evidence `P00734:probe` (probe_template): redistribute bgp <1-65535>

#### F00738

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence establishes the probe template but does not substantiate the claimed absence of a matching command topic for the VRF view.
- Evidence `P00735:probe` (probe_template): redistribute bgp <1-65535>

#### F00739

- Status: unresolved
- Probe template: `redistribute bgp <65536-4294967295> metric-type {1|2}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The probe template is evidenced, but there is no supplied manual evidence from which to confirm or dismiss undercoverage.
- Evidence `P00736:probe` (probe_template): redistribute bgp <65536-4294967295> metric-type {1|2}

#### F00740

- Status: unresolved
- Probe template: `redistribute bgp <1-65535> metric-type {2|1}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence shows the probe template only; it cannot establish whether supplied manuals contain a corresponding router-view command topic.
- Evidence `P00737:probe` (probe_template): redistribute bgp <1-65535> metric-type {2|1}

#### F00741

- Status: unresolved
- Probe template: `redistribute bgp <1-65535> metric-type {2|1}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00738:probe` (probe_template): redistribute bgp <1-65535> metric-type {2|1}

#### F00742

- Status: unresolved
- Probe template: `redistribute bgp <65536-4294967295> metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00739:probe` (probe_template): redistribute bgp <65536-4294967295> metric {<1-16777214>|use-rib-metric}

#### F00743

- Status: unresolved
- Probe template: `redistribute bgp <1-65535> metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00740:probe` (probe_template): redistribute bgp <1-65535> metric {use-rib-metric|<1-16777214>}

#### F00744

- Status: unresolved
- Probe template: `redistribute bgp <1-65535> metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching command topic exists.
- Evidence `P00741:probe` (probe_template): redistribute bgp <1-65535> metric {use-rib-metric|<1-16777214>}

#### F00745

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00742:probe` (probe_template): redistribute bgp <1-65535>. <0-65535>

#### F00746

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists for the VRF view.
- Evidence `P00743:probe` (probe_template): redistribute bgp <1-65535>. <0-65535>

#### F00747

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535> metric-type {2|1}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template including the metric-type option. It does not support a determination that supplied manuals lack a matching command topic.
- Evidence `P00744:probe` (probe_template): redistribute bgp <1-65535>. <0-65535> metric-type {2|1}

#### F00748

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535> metric-type {2|1}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template including the metric-type option. It does not support a determination that supplied manuals lack a matching command topic for the VRF view.
- Evidence `P00745:probe` (probe_template): redistribute bgp <1-65535>. <0-65535> metric-type {2|1}

#### F00749

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535> metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The evidence establishes the probe command, but provides no manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00746:probe` (probe_template): redistribute bgp <1-65535>. <0-65535> metric {<1-16777214>|use-rib-metric}

#### F00750

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535> metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The probe template is evidenced, but the supplied evidence cannot establish the asserted absence of a corresponding manual command topic.
- Evidence `P00747:probe` (probe_template): redistribute bgp <1-65535>. <0-65535> metric {use-rib-metric|<1-16777214>}

#### F00751

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535> {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|preserve-bgp-default-info|nssa-only|preserve-med}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The supplied evidence identifies the probe template only; it does not support or refute the claimed lack of matching manual coverage.
- Evidence `P00748:probe` (probe_template): redistribute bgp <1-65535>. <0-65535> {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|preserve-bgp-default-info|nssa-only|preserve-med}

#### F00752

- Status: unresolved
- Probe template: `redistribute bgp <1-65535>. <0-65535> {tag <0-4294967295>|nssa-only|preserve-med|lsa-type summary|route-policy <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.35
- Review rationale: The probe command is present in the evidence, but no manual evidence is supplied to determine whether a matching command topic exists.
- Evidence `P00749:probe` (probe_template): redistribute bgp <1-65535>. <0-65535> {tag <0-4294967295>|nssa-only|preserve-med|lsa-type summary|route-policy <WORD>}

#### F00753

- Status: unresolved
- Probe template: `redistribute bgp <1-65535> {lsa-type summary|preserve-med|preserve-bgp-default-info|tag <0-4294967295>|route-policy <WORD>|nssa-only}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.62
- Review rationale: The evidence establishes the probe template, but provides no manual content or coverage evidence to verify that no supplied manual command matches it.
- Evidence `P00750:probe` (probe_template): redistribute bgp <1-65535> {lsa-type summary|preserve-med|preserve-bgp-default-info|tag <0-4294967295>|route-policy <WORD>|nssa-only}

#### F00754

- Status: unresolved
- Probe template: `redistribute bgp <65536-4294967295> {lsa-type summary|preserve-med|tag <0-4294967295>|nssa-only|route-policy <WORD>|preserve-bgp-default-info}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.62
- Review rationale: The evidence establishes the probe template, but provides no manual content or coverage evidence to verify that no supplied manual command matches it.
- Evidence `P00751:probe` (probe_template): redistribute bgp <65536-4294967295> {lsa-type summary|preserve-med|tag <0-4294967295>|nssa-only|route-policy <WORD>|preserve-bgp-default-info}

#### F00755

- Status: unresolved
- Probe template: `redistribute bgp <1-65535> {nssa-only|lsa-type summary|tag <0-4294967295>|preserve-med|route-policy <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.62
- Review rationale: The evidence establishes the probe template, but provides no manual content or coverage evidence to verify that no supplied manual command matches it.
- Evidence `P00752:probe` (probe_template): redistribute bgp <1-65535> {nssa-only|lsa-type summary|tag <0-4294967295>|preserve-med|route-policy <WORD>}

#### F00756

- Status: unresolved
- Probe template: `redistribute bgp <65536-4294967295> {nssa-only|tag <0-4294967295>|lsa-type summary|route-policy <WORD>|preserve-med}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.62
- Review rationale: The evidence establishes the probe template, but provides no manual content or coverage evidence to verify that no supplied manual command matches it.
- Evidence `P00753:probe` (probe_template): redistribute bgp <65536-4294967295> {nssa-only|tag <0-4294967295>|lsa-type summary|route-policy <WORD>|preserve-med}

#### F00757

- Status: unresolved
- Probe template: `redistribute connected`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify the claimed absence of a matching topic.
- Evidence `P00754:probe` (probe_template): redistribute connected

#### F00758

- Status: unresolved
- Probe template: `redistribute connected`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify the claimed absence of a matching topic for the VRF view.
- Evidence `P00755:probe` (probe_template): redistribute connected

#### F00759

- Status: unresolved
- Probe template: `redistribute connected metric-type {2|1}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-topic inventory to support or refute the undercoverage claim.
- Evidence `P00756:probe` (probe_template): redistribute connected metric-type {2|1}

#### F00760

- Status: unresolved
- Probe template: `redistribute connected metric-type {2|1}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual content or command-topic inventory to support or refute the claimed absence of a matching VRF command topic.
- Evidence `P00757:probe` (probe_template): redistribute connected metric-type {2|1}

#### F00761

- Status: unresolved
- Probe template: `redistribute connected metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00758:probe` (probe_template): redistribute connected metric {use-rib-metric|<1-16777214>}

#### F00762

- Status: unresolved
- Probe template: `redistribute connected metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual evidence to verify that no matching command topic exists for the VRF view.
- Evidence `P00759:probe` (probe_template): redistribute connected metric {use-rib-metric|<1-16777214>}

#### F00763

- Status: unresolved
- Probe template: `redistribute connected {lsa-type summary|tag <0-4294967295>|nssa-only|route-policy <WORD>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual evidence to verify that no matching command topic exists for the VRF view.
- Evidence `P00760:probe` (probe_template): redistribute connected {lsa-type summary|tag <0-4294967295>|nssa-only|route-policy <WORD>}

#### F00764

- Status: unresolved
- Probe template: `redistribute connected {tag <0-4294967295>|nssa-only|lsa-type summary|route-policy <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes the probe command template but provides no manual evidence to verify that no matching command topic exists for the router view.
- Evidence `P00761:probe` (probe_template): redistribute connected {tag <0-4294967295>|nssa-only|lsa-type summary|route-policy <WORD>}

#### F00765

- Status: unresolved
- Probe template: `redistribute dagr`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no manual-content evidence to verify that no matching command topic exists.
- Evidence `P00762:probe` (probe_template): redistribute dagr

#### F00766

- Status: unresolved
- Probe template: `redistribute dagr`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no manual-content evidence to verify that no matching command topic exists for the VRF view.
- Evidence `P00763:probe` (probe_template): redistribute dagr

#### F00767

- Status: unresolved
- Probe template: `redistribute dagr metric-type {1|2}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but does not substantiate the asserted absence of a matching manual command topic.
- Evidence `P00764:probe` (probe_template): redistribute dagr metric-type {1|2}

#### F00768

- Status: unresolved
- Probe template: `redistribute dagr metric-type {1|2}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual-content evidence to assess the claimed undercoverage in the VRF view.
- Evidence `P00765:probe` (probe_template): redistribute dagr metric-type {1|2}

#### F00769

- Status: unresolved
- Probe template: `redistribute dagr metric {<1-16777214>|use-rib-metric}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the probe template only. It does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00766:probe` (probe_template): redistribute dagr metric {<1-16777214>|use-rib-metric}

#### F00770

- Status: unresolved
- Probe template: `redistribute dagr metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The probe template is supplied, but no manual-source evidence is provided to substantiate the asserted absence of a matching topic in the VRF view.
- Evidence `P00767:probe` (probe_template): redistribute dagr metric {<1-16777214>|use-rib-metric}

#### F00771

- Status: unresolved
- Probe template: `redistribute dagr {lsa-type summary|route-policy <WORD>|nssa-only|tag <0-4294967295>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The evidence identifies the probe command but cannot establish whether the supplied manuals contain a matching command topic for the VRF semantic view.
- Evidence `P00768:probe` (probe_template): redistribute dagr {lsa-type summary|route-policy <WORD>|nssa-only|tag <0-4294967295>}

#### F00772

- Status: unresolved
- Probe template: `redistribute dagr {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: Only the probe command is evidenced. The claimed lack of a matching router-view manual topic cannot be determined from this evidence.
- Evidence `P00769:probe` (probe_template): redistribute dagr {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}

#### F00773

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00770:probe` (probe_template): redistribute eigrp <1-65535>

#### F00774

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists in the VRF view.
- Evidence `P00771:probe` (probe_template): redistribute eigrp <1-65535>

#### F00775

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> match {external|internal}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify the claimed absence of a matching command topic.
- Evidence `P00772:probe` (probe_template): redistribute eigrp <1-65535> match {external|internal}

#### F00776

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> match {internal|external}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify the claimed absence of a matching command topic in the router view.
- Evidence `P00773:probe` (probe_template): redistribute eigrp <1-65535> match {internal|external}

#### F00777

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> metric-type {1|2}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command, but provides no manual evidence to substantiate that no matching command topic exists.
- Evidence `P00774:probe` (probe_template): redistribute eigrp <1-65535> metric-type {1|2}

#### F00778

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> metric-type {2|1}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command, but provides no manual evidence to substantiate that no matching command topic exists.
- Evidence `P00775:probe` (probe_template): redistribute eigrp <1-65535> metric-type {2|1}

#### F00779

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command, but provides no manual evidence to substantiate that no matching command topic exists.
- Evidence `P00776:probe` (probe_template): redistribute eigrp <1-65535> metric {use-rib-metric|<1-16777214>}

#### F00780

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command, but provides no manual evidence to substantiate that no matching command topic exists.
- Evidence `P00777:probe` (probe_template): redistribute eigrp <1-65535> metric {use-rib-metric|<1-16777214>}

#### F00781

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists.
- Evidence `P00778:probe` (probe_template): redistribute eigrp <1-65535> {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}

#### F00782

- Status: unresolved
- Probe template: `redistribute eigrp <1-65535> {route-policy <WORD>|nssa-only|lsa-type summary|tag <0-4294967295>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists.
- Evidence `P00779:probe` (probe_template): redistribute eigrp <1-65535> {route-policy <WORD>|nssa-only|lsa-type summary|tag <0-4294967295>}

#### F00783

- Status: unresolved
- Probe template: `redistribute isis <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists.
- Evidence `P00780:probe` (probe_template): redistribute isis <WORD>

#### F00784

- Status: unresolved
- Probe template: `redistribute isis <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual-command evidence to verify that no matching topic exists.
- Evidence `P00781:probe` (probe_template): redistribute isis <WORD>

#### F00785

- Status: unresolved
- Probe template: `redistribute isis <WORD> metric-type {1|2}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to verify that no matching command topic exists.
- Evidence `P00782:probe` (probe_template): redistribute isis <WORD> metric-type {1|2}

#### F00786

- Status: unresolved
- Probe template: `redistribute isis <WORD> metric-type {1|2}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to verify that no matching command topic exists for the VRF view.
- Evidence `P00783:probe` (probe_template): redistribute isis <WORD> metric-type {1|2}

#### F00787

- Status: unresolved
- Probe template: `redistribute isis <WORD> metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to support the asserted absence of a corresponding manual topic.
- Evidence `P00784:probe` (probe_template): redistribute isis <WORD> metric {<1-16777214>|use-rib-metric}

#### F00788

- Status: unresolved
- Probe template: `redistribute isis <WORD> metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence to verify that no matching command topic exists for the router view.
- Evidence `P00785:probe` (probe_template): redistribute isis <WORD> metric {use-rib-metric|<1-16777214>}

#### F00789

- Status: unresolved
- Probe template: `redistribute isis <WORD> {level-1-2|lsa-type summary|level-2|level-1|tag <0-4294967295>|route-policy <WORD>|nssa-only}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe command template, but provides no supplied manual content or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00786:probe` (probe_template): redistribute isis <WORD> {level-1-2|lsa-type summary|level-2|level-1|tag <0-4294967295>|route-policy <WORD>|nssa-only}

#### F00790

- Status: unresolved
- Probe template: `redistribute isis <WORD> {lsa-type summary|level-1-2|level-2|level-1|route-policy <WORD>|tag <0-4294967295>|nssa-only}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The probe template is evidenced, but the supplied evidence does not include manuals or a coverage inventory sufficient to confirm undercoverage.
- Evidence `P00787:probe` (probe_template): redistribute isis <WORD> {lsa-type summary|level-1-2|level-2|level-1|route-policy <WORD>|tag <0-4294967295>|nssa-only}

#### F00791

- Status: unresolved
- Probe template: `redistribute mobile`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence supports only that the probe command is "redistribute mobile"; it cannot establish the asserted absence of a matching manual command topic.
- Evidence `P00788:probe` (probe_template): redistribute mobile

#### F00792

- Status: unresolved
- Probe template: `redistribute mobile`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The probe command is supported, but no manual evidence is supplied to substantiate that no matching topic exists for the VRF semantic view.
- Evidence `P00789:probe` (probe_template): redistribute mobile

#### F00793

- Status: unresolved
- Probe template: `redistribute mobile metric-type {1|2}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no supplied manual content or coverage comparison to support or refute the claimed absence of a matching manual topic.
- Evidence `P00790:probe` (probe_template): redistribute mobile metric-type {1|2}

#### F00794

- Status: unresolved
- Probe template: `redistribute mobile metric-type {1|2}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no supplied manual content or coverage comparison to support or refute the claimed absence of a matching manual topic in the VRF view.
- Evidence `P00791:probe` (probe_template): redistribute mobile metric-type {1|2}

#### F00795

- Status: unresolved
- Probe template: `redistribute mobile metric {<1-16777214>|use-rib-metric}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but does not include manual-command evidence sufficient to determine whether coverage is absent.
- Evidence `P00792:probe` (probe_template): redistribute mobile metric {<1-16777214>|use-rib-metric}

#### F00796

- Status: unresolved
- Probe template: `redistribute mobile metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but does not include manual-command evidence sufficient to determine whether coverage is absent in the VRF view.
- Evidence `P00793:probe` (probe_template): redistribute mobile metric {use-rib-metric|<1-16777214>}

#### F00797

- Status: unresolved
- Probe template: `redistribute mobile {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.82
- Review rationale: The supplied evidence establishes the probe command, but provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00794:probe` (probe_template): redistribute mobile {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}

#### F00798

- Status: unresolved
- Probe template: `redistribute mobile {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.82
- Review rationale: The supplied evidence establishes the probe command, but provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00795:probe` (probe_template): redistribute mobile {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}

#### F00799

- Status: unresolved
- Probe template: `redistribute ospf <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.82
- Review rationale: The supplied evidence establishes the probe command, but provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00796:probe` (probe_template): redistribute ospf <WORD>

#### F00800

- Status: unresolved
- Probe template: `redistribute ospf <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.82
- Review rationale: The supplied evidence establishes the probe command, but provides no manual-command evidence from which to verify that no matching command topic exists.
- Evidence `P00797:probe` (probe_template): redistribute ospf <WORD>

#### F00801

- Status: unresolved
- Probe template: `redistribute ospf <WORD> lsa-type summary`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence supporting or verifying the claimed absence of a matching command topic.
- Evidence `P00798:probe` (probe_template): redistribute ospf <WORD> lsa-type summary

#### F00802

- Status: unresolved
- Probe template: `redistribute ospf <WORD> lsa-type summary`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence supporting or verifying the claimed absence of a matching command topic in the VRF view.
- Evidence `P00799:probe` (probe_template): redistribute ospf <WORD> lsa-type summary

#### F00803

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric <1-16777214>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence supporting or verifying the claimed absence of a matching command topic.
- Evidence `P00800:probe` (probe_template): redistribute ospf <WORD> metric <1-16777214>

#### F00804

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric <1-16777214>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence supporting or verifying the claimed absence of a matching command topic in the VRF view.
- Evidence `P00801:probe` (probe_template): redistribute ospf <WORD> metric <1-16777214>

#### F00805

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric use-rib-metric`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual content or coverage inventory to substantiate that no matching command topic exists.
- Evidence `P00802:probe` (probe_template): redistribute ospf <WORD> metric use-rib-metric

#### F00806

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric use-rib-metric`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual content or coverage inventory to substantiate that no matching command topic exists for the VRF view.
- Evidence `P00803:probe` (probe_template): redistribute ospf <WORD> metric use-rib-metric

#### F00807

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric-type 1`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual content or coverage inventory to substantiate the asserted absence of a matching command topic.
- Evidence `P00804:probe` (probe_template): redistribute ospf <WORD> metric-type 1

#### F00808

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric-type 1`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual content or coverage inventory to substantiate the asserted absence of a matching command topic for the VRF view.
- Evidence `P00805:probe` (probe_template): redistribute ospf <WORD> metric-type 1

#### F00809

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric-type 2`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence or manual corpus information to verify that no matching topic exists.
- Evidence `P00806:probe` (probe_template): redistribute ospf <WORD> metric-type 2

#### F00810

- Status: unresolved
- Probe template: `redistribute ospf <WORD> metric-type 2`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence or manual corpus information to verify that no matching topic exists for the VRF view.
- Evidence `P00807:probe` (probe_template): redistribute ospf <WORD> metric-type 2

#### F00811

- Status: unresolved
- Probe template: `redistribute ospf <WORD> nssa-only`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence or manual corpus information to verify that no matching topic exists.
- Evidence `P00808:probe` (probe_template): redistribute ospf <WORD> nssa-only

#### F00812

- Status: unresolved
- Probe template: `redistribute ospf <WORD> nssa-only`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template but provides no manual-command evidence or manual corpus information to verify that no matching topic exists for the VRF view.
- Evidence `P00809:probe` (probe_template): redistribute ospf <WORD> nssa-only

#### F00813

- Status: unresolved
- Probe template: `redistribute ospf <WORD> route-policy <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide supplied manual content or a command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00810:probe` (probe_template): redistribute ospf <WORD> route-policy <WORD>

#### F00814

- Status: unresolved
- Probe template: `redistribute ospf <WORD> route-policy <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide supplied manual content or a command-topic inventory to verify that no matching manual topic exists for the VRF view.
- Evidence `P00811:probe` (probe_template): redistribute ospf <WORD> route-policy <WORD>

#### F00815

- Status: unresolved
- Probe template: `redistribute ospf <WORD> tag <0-4294967295>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide supplied manual content or a command-topic inventory to verify the asserted command undercoverage.
- Evidence `P00812:probe` (probe_template): redistribute ospf <WORD> tag <0-4294967295>

#### F00816

- Status: unresolved
- Probe template: `redistribute ospf <WORD> tag <0-4294967295>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template; it does not provide supplied manual content or a command-topic inventory to verify that no matching manual topic exists for the VRF view.
- Evidence `P00813:probe` (probe_template): redistribute ospf <WORD> tag <0-4294967295>

#### F00817

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no supplied manual command matches it.
- Evidence `P00814:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external

#### F00818

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external 1`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no supplied manual command matches it.
- Evidence `P00815:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external 1

#### F00819

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external 2`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no supplied manual command matches it.
- Evidence `P00816:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external 2

#### F00820

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external [2 [internal]|1 [internal]|internal|nssa-external] metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no supplied manual command matches it.
- Evidence `P00817:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external [2 [internal]|1 [internal]|internal|nssa-external] metric {use-rib-metric|<1-16777214>}

#### F00821

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external [2|1] internal`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only. It provides no supplied manual-command inventory or manual-topic evidence sufficient to verify that no matching topic exists.
- Evidence `P00818:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external [2|1] internal

#### F00822

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|2 {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|internal {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}|nssa-only}|1 {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|internal {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}|nssa-only}|internal {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}|nssa-only|nssa-external {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only. It provides no supplied manual-command inventory or manual-topic evidence sufficient to verify that no matching topic exists.
- Evidence `P00819:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|2 {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|internal {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}|nssa-only}|1 {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|internal {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}|nssa-only}|internal {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}|nssa-only|nssa-external {lsa-type summary|route-policy <WORD>|tag <0-4294967295>|nssa-only}}

#### F00823

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external {metric-type|nssa-external [metric-type]}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only. It provides no supplied manual-command inventory or manual-topic evidence sufficient to verify that no matching topic exists.
- Evidence `P00820:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match external {metric-type|nssa-external [metric-type]}

#### F00824

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template only. It provides no supplied manual-command inventory or manual-topic evidence sufficient to verify that no matching topic exists.
- Evidence `P00821:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal

#### F00825

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external 1`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual inventory or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00822:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external 1

#### F00826

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external 2`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual inventory or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00823:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external 2

#### F00827

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external nssa-external`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual inventory or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00824:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external nssa-external

#### F00828

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external [nssa-external] metric-type`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the Probe command template but provides no manual inventory or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00825:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external [nssa-external] metric-type

#### F00829

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external [nssa-external|2|1] metric {<1-16777214>|use-rib-metric}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.85
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence or manual corpus evidence to substantiate that no matching command topic exists.
- Evidence `P00826:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external [nssa-external|2|1] metric {<1-16777214>|use-rib-metric}

#### F00830

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external {nssa-external {nssa-only|lsa-type summary|route-policy <WORD>|tag <0-4294967295>}|nssa-only|lsa-type summary|route-policy <WORD>|2 {nssa-only|lsa-type summary|route-policy <WORD>|tag <0-4294967295>}|tag <0-4294967295>|1 {nssa-only|lsa-type summary|route-policy <WORD>|tag <0-4294967295>}}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.85
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence or manual corpus evidence to substantiate that no matching command topic exists.
- Evidence `P00827:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal external {nssa-external {nssa-only|lsa-type summary|route-policy <WORD>|tag <0-4294967295>}|nssa-only|lsa-type summary|route-policy <WORD>|2 {nssa-only|lsa-type summary|route-policy <WORD>|tag <0-4294967295>}|tag <0-4294967295>|1 {nssa-only|lsa-type summary|route-policy <WORD>|tag <0-4294967295>}}

#### F00831

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal metric-type {1|2}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.85
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence or manual corpus evidence to substantiate that no matching command topic exists.
- Evidence `P00828:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal metric-type {1|2}

#### F00832

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal metric {<1-16777214>|use-rib-metric}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.85
- Review rationale: The evidence establishes the probe template, but supplies no manual-command evidence or manual corpus evidence to substantiate that no matching command topic exists.
- Evidence `P00829:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal metric {<1-16777214>|use-rib-metric}

#### F00833

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external 1`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command, but provides no manual-content evidence to verify that no matching command topic exists.
- Evidence `P00830:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external 1

#### F00834

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external 2`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command, but provides no manual-content evidence to verify that no matching command topic exists.
- Evidence `P00831:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external 2

#### F00835

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external external`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command, but provides no manual-content evidence to verify that no matching command topic exists.
- Evidence `P00832:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external external

#### F00836

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external [1|external|2] metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command, but provides no manual-content evidence to verify that no matching command topic exists.
- Evidence `P00833:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external [1|external|2] metric {use-rib-metric|<1-16777214>}

#### F00837

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external [external] metric-type`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the Probe command template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00834:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external [external] metric-type

#### F00838

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external {1 {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|external {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|lsa-type summary|2 {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|nssa-only}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the Probe command template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00835:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal nssa-external {1 {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|external {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|lsa-type summary|2 {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|nssa-only}

#### F00839

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal {tag <0-4294967295>|route-policy <WORD>|nssa-only|lsa-type summary}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the Probe command template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00836:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match internal {tag <0-4294967295>|route-policy <WORD>|nssa-only|lsa-type summary}

#### F00840

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the Probe command template only; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00837:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external

#### F00841

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external 1`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command but supplies no manual-topic evidence to verify that no matching command topic exists.
- Evidence `P00838:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external 1

#### F00842

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external 2`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command but supplies no manual-topic evidence to verify that no matching command topic exists.
- Evidence `P00839:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external 2

#### F00843

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external [2|1] internal`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command but supplies no manual-topic evidence to verify that no matching command topic exists.
- Evidence `P00840:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external [2|1] internal

#### F00844

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external [internal|2 [internal]|external|1 [internal]] metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command but supplies no manual-topic evidence to verify that no matching command topic exists.
- Evidence `P00841:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external [internal|2 [internal]|external|1 [internal]] metric {use-rib-metric|<1-16777214>}

#### F00845

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external {internal {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|route-policy <WORD>|2 {internal {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|tag <0-4294967295>|external {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|1 {internal {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|nssa-only|lsa-type summary}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template only. It provides no supplied manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00842:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external {internal {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|route-policy <WORD>|2 {internal {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|tag <0-4294967295>|external {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|1 {internal {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}|nssa-only|lsa-type summary}

#### F00846

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external {metric-type|external [metric-type]}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template only. It provides no supplied manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00843:probe` (probe_template): redistribute ospf <WORD> [metric-type {1|2}|metric {<1-16777214>|use-rib-metric}|nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>] match nssa-external {metric-type|external [metric-type]}

#### F00847

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external 1`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template only. It provides no supplied manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00844:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external 1

#### F00848

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external 2`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template only. It provides no supplied manual-command evidence from which to verify that no matching manual topic exists.
- Evidence `P00845:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external 2

#### F00849

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external nssa-external`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content or command-topic coverage evidence to verify that no matching topic exists.
- Evidence `P00846:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external nssa-external

#### F00850

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external [2|1] internal`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content or command-topic coverage evidence to verify that no matching topic exists.
- Evidence `P00847:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external [2|1] internal

#### F00851

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external [internal|2 [internal]|1 [internal]|nssa-external] metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content or command-topic coverage evidence to verify that no matching topic exists.
- Evidence `P00848:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external [internal|2 [internal]|1 [internal]|nssa-external] metric {use-rib-metric|<1-16777214>}

#### F00852

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external [nssa-external] metric-type`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.94
- Review rationale: The evidence establishes the probe template only; it provides no supplied manual content or command-topic coverage evidence to verify that no matching topic exists.
- Evidence `P00849:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external [nssa-external] metric-type

#### F00853

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external {internal {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|2 {internal {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|1 {internal {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|lsa-type summary|nssa-only|nssa-external {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command template only. It provides no manual-topic evidence or manual corpus coverage information to support or refute the asserted absence of a matching command topic.
- Evidence `P00850:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match external {internal {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|2 {internal {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|1 {internal {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}|lsa-type summary|nssa-only|nssa-external {route-policy <WORD>|tag <0-4294967295>|lsa-type summary|nssa-only}}

#### F00854

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command template only. It provides no manual-topic evidence or manual corpus coverage information to support or refute the asserted absence of a matching command topic.
- Evidence `P00851:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal

#### F00855

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command template only. It provides no manual-topic evidence or manual corpus coverage information to support or refute the asserted absence of a matching command topic.
- Evidence `P00852:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external

#### F00856

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external 1`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes the Probe command template only. It provides no manual-topic evidence or manual corpus coverage information to support or refute the asserted absence of a matching command topic.
- Evidence `P00853:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external 1

#### F00857

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external 2`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command only; it does not provide manual-topic coverage or evidence sufficient to establish that no matching manual command exists.
- Evidence `P00854:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external 2

#### F00858

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external [nssa-external|2|1] metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command only; it does not provide manual-topic coverage or evidence sufficient to establish that no matching manual command exists.
- Evidence `P00855:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external [nssa-external|2|1] metric {use-rib-metric|<1-16777214>}

#### F00859

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external {metric-type|nssa-external [metric-type]}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command only; it does not provide manual-topic coverage or evidence sufficient to establish that no matching manual command exists.
- Evidence `P00856:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external {metric-type|nssa-external [metric-type]}

#### F00860

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal metric-type {1|2}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command only; it does not provide manual-topic coverage or evidence sufficient to establish that no matching manual command exists.
- Evidence `P00857:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal metric-type {1|2}

#### F00861

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external 1`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template, but supplies no manual-content evidence supporting or disproving the claimed absence of a matching command topic.
- Evidence `P00858:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external 1

#### F00862

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external 2`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template, but supplies no manual-content evidence supporting or disproving the claimed absence of a matching command topic.
- Evidence `P00859:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external 2

#### F00863

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external external`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template, but supplies no manual-content evidence supporting or disproving the claimed absence of a matching command topic.
- Evidence `P00860:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external external

#### F00864

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external [external] metric-type`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the Probe command template, but supplies no manual-content evidence supporting or disproving the claimed absence of a matching command topic.
- Evidence `P00861:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal nssa-external [external] metric-type

#### F00865

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal {route-policy <WORD>|lsa-type summary|tag <0-4294967295>|nssa-only}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe command template, but provides no manual content or coverage evidence from which to verify that no matching command topic exists.
- Evidence `P00862:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal {route-policy <WORD>|lsa-type summary|tag <0-4294967295>|nssa-only}

#### F00866

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe command template, but provides no manual content or coverage evidence from which to verify that no matching command topic exists.
- Evidence `P00863:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external

#### F00867

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external 1`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe command template, but provides no manual content or coverage evidence from which to verify that no matching command topic exists.
- Evidence `P00864:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external 1

#### F00868

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external 2`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The supplied evidence establishes the probe command template, but provides no manual content or coverage evidence from which to verify that no matching command topic exists.
- Evidence `P00865:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external 2

#### F00869

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external [2 [internal]|1 [internal]|external|internal] metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes the probe template but provides no manual-topic evidence to verify that no matching command topic exists.
- Evidence `P00866:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external [2 [internal]|1 [internal]|external|internal] metric {<1-16777214>|use-rib-metric}

#### F00870

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external [2|1] internal`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence establishes the probe template but does not substantiate the asserted absence of a corresponding manual command topic.
- Evidence `P00867:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external [2|1] internal

#### F00871

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external {2 {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only|internal {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}}|tag <0-4294967295>|1 {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only|internal {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}}|lsa-type summary|route-policy <WORD>|external {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}|nssa-only|internal {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe template is evidenced, but no supplied manual evidence supports or refutes the claimed command undercoverage.
- Evidence `P00868:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external {2 {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only|internal {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}}|tag <0-4294967295>|1 {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only|internal {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}}|lsa-type summary|route-policy <WORD>|external {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}|nssa-only|internal {tag <0-4294967295>|lsa-type summary|route-policy <WORD>|nssa-only}}

#### F00872

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external {external [metric-type]|metric-type}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence contains only the probe template and cannot establish whether supplied manuals contain a matching command topic.
- Evidence `P00869:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match nssa-external {external [metric-type]|metric-type}

#### F00873

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [route-policy <WORD>|metric-type {2|1}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external {tag <0-4294967295>|nssa-external {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}|2 {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}|1 {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}|nssa-only|route-policy <WORD>|lsa-type summary}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence documents the probe template only. It contains no manual-topic inventory or manual evidence sufficient to establish that no matching command topic exists.
- Evidence `P00870:probe` (probe_template): redistribute ospf <WORD> [route-policy <WORD>|metric-type {2|1}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}|tag <0-4294967295>] match internal external {tag <0-4294967295>|nssa-external {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}|2 {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}|1 {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}|nssa-only|route-policy <WORD>|lsa-type summary}

#### F00874

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [tag <0-4294967295>|route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}] match internal metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence documents the probe template only. It contains no manual-topic inventory or manual evidence sufficient to establish that no matching command topic exists.
- Evidence `P00871:probe` (probe_template): redistribute ospf <WORD> [tag <0-4294967295>|route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}] match internal metric {use-rib-metric|<1-16777214>}

#### F00875

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [tag <0-4294967295>|route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}] match internal nssa-external [2|1|external] metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence documents the probe template only. It contains no manual-topic inventory or manual evidence sufficient to establish that no matching command topic exists.
- Evidence `P00872:probe` (probe_template): redistribute ospf <WORD> [tag <0-4294967295>|route-policy <WORD>|metric-type {1|2}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}] match internal nssa-external [2|1|external] metric {<1-16777214>|use-rib-metric}

#### F00876

- Status: unresolved
- Probe template: `redistribute ospf <WORD> [tag <0-4294967295>|route-policy <WORD>|metric-type {2|1}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}] match internal nssa-external {2 {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}|tag <0-4294967295>|lsa-type summary|1 {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}|nssa-only|route-policy <WORD>|external {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence documents the probe template only. It contains no manual-topic inventory or manual evidence sufficient to establish that no matching command topic exists.
- Evidence `P00873:probe` (probe_template): redistribute ospf <WORD> [tag <0-4294967295>|route-policy <WORD>|metric-type {2|1}|lsa-type summary|nssa-only|metric {<1-16777214>|use-rib-metric}] match internal nssa-external {2 {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}|tag <0-4294967295>|lsa-type summary|1 {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}|nssa-only|route-policy <WORD>|external {tag <0-4294967295>|lsa-type summary|nssa-only|route-policy <WORD>}}

#### F00877

- Status: unresolved
- Probe template: `redistribute rip`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but provides no supplied manual inventory or command-topic evidence to substantiate that no matching manual topic exists.
- Evidence `P00874:probe` (probe_template): redistribute rip

#### F00878

- Status: unresolved
- Probe template: `redistribute rip`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence establishes the probe command but does not support the claimed absence of a matching command topic in the supplied manuals for the VRF view.
- Evidence `P00875:probe` (probe_template): redistribute rip

#### F00879

- Status: unresolved
- Probe template: `redistribute rip metric-type {2|1}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The probe template is evidenced, but no manual-search results or manual command evidence is supplied to confirm command undercoverage.
- Evidence `P00876:probe` (probe_template): redistribute rip metric-type {2|1}

#### F00880

- Status: unresolved
- Probe template: `redistribute rip metric-type {2|1}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.97
- Review rationale: The evidence only identifies the probe template and cannot establish that the supplied manuals lack a matching VRF command topic.
- Evidence `P00877:probe` (probe_template): redistribute rip metric-type {2|1}

#### F00881

- Status: unresolved
- Probe template: `redistribute rip metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command template but provides no supplied manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00878:probe` (probe_template): redistribute rip metric {use-rib-metric|<1-16777214>}

#### F00882

- Status: unresolved
- Probe template: `redistribute rip metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command template but does not support the asserted absence of a matching manual topic in the VRF semantic view.
- Evidence `P00879:probe` (probe_template): redistribute rip metric {use-rib-metric|<1-16777214>}

#### F00883

- Status: unresolved
- Probe template: `redistribute rip {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence contains only the probe template and cannot establish manual undercoverage or absence of a corresponding command topic.
- Evidence `P00880:probe` (probe_template): redistribute rip {route-policy <WORD>|tag <0-4294967295>|nssa-only|lsa-type summary}

#### F00884

- Status: unresolved
- Probe template: `redistribute rip {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The probe template is supported, but no manual evidence is supplied from which to confirm that the router semantic view lacks a matching command topic.
- Evidence `P00881:probe` (probe_template): redistribute rip {tag <0-4294967295>|nssa-only|route-policy <WORD>|lsa-type summary}

#### F00885

- Status: unresolved
- Probe template: `redistribute static`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to verify that no matching manual command exists for the router view.
- Evidence `P00882:probe` (probe_template): redistribute static

#### F00886

- Status: unresolved
- Probe template: `redistribute static`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to verify that no matching manual command exists for the vrf view.
- Evidence `P00883:probe` (probe_template): redistribute static

#### F00887

- Status: unresolved
- Probe template: `redistribute static metric-type {2|1}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to verify that no matching manual command exists for the router view.
- Evidence `P00884:probe` (probe_template): redistribute static metric-type {2|1}

#### F00888

- Status: unresolved
- Probe template: `redistribute static metric-type {2|1}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence to verify that no matching manual command exists for the vrf view.
- Evidence `P00885:probe` (probe_template): redistribute static metric-type {2|1}

#### F00889

- Status: unresolved
- Probe template: `redistribute static metric {use-rib-metric|<1-16777214>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00886:probe` (probe_template): redistribute static metric {use-rib-metric|<1-16777214>}

#### F00890

- Status: unresolved
- Probe template: `redistribute static metric {use-rib-metric|<1-16777214>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no supplied manual evidence from which to verify that no matching command topic exists in the VRF view.
- Evidence `P00887:probe` (probe_template): redistribute static metric {use-rib-metric|<1-16777214>}

#### F00891

- Status: unresolved
- Probe template: `redistribute static {nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no supplied manual evidence from which to verify that no matching command topic exists in the VRF view.
- Evidence `P00888:probe` (probe_template): redistribute static {nssa-only|route-policy <WORD>|lsa-type summary|tag <0-4294967295>}

#### F00892

- Status: unresolved
- Probe template: `redistribute static {route-policy <WORD>|nssa-only|tag <0-4294967295>|lsa-type summary}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence establishes the probe command, but provides no supplied manual evidence from which to verify that no matching command topic exists in the router view.
- Evidence `P00889:probe` (probe_template): redistribute static {route-policy <WORD>|nssa-only|tag <0-4294967295>|lsa-type summary}

#### F00893

- Status: unresolved
- Probe template: `redistribute subscriber`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00890:probe` (probe_template): redistribute subscriber

#### F00894

- Status: unresolved
- Probe template: `redistribute subscriber`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00891:probe` (probe_template): redistribute subscriber

#### F00895

- Status: unresolved
- Probe template: `redistribute subscriber metric-type {1|2}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command template but provides no supplied manual content or command-topic inventory to verify the claimed undercoverage.
- Evidence `P00892:probe` (probe_template): redistribute subscriber metric-type {1|2}

#### F00896

- Status: unresolved
- Probe template: `redistribute subscriber metric-type {2|1}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command template but provides no supplied manual content or command-topic inventory to verify the claimed undercoverage.
- Evidence `P00893:probe` (probe_template): redistribute subscriber metric-type {2|1}

#### F00897

- Status: unresolved
- Probe template: `redistribute subscriber metric {<1-16777214>|use-rib-metric}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe command template, but provides no manual content or coverage evidence to verify that no matching command topic exists.
- Evidence `P00894:probe` (probe_template): redistribute subscriber metric {<1-16777214>|use-rib-metric}

#### F00898

- Status: unresolved
- Probe template: `redistribute subscriber metric {<1-16777214>|use-rib-metric}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe command template, but provides no manual content or coverage evidence to verify that no matching command topic exists in the VRF view.
- Evidence `P00895:probe` (probe_template): redistribute subscriber metric {<1-16777214>|use-rib-metric}

#### F00899

- Status: unresolved
- Probe template: `redistribute subscriber {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe command template, but provides no manual content or coverage evidence to verify the asserted lack of a matching command topic in the VRF view.
- Evidence `P00896:probe` (probe_template): redistribute subscriber {nssa-only|lsa-type summary|tag <0-4294967295>|route-policy <WORD>}

#### F00900

- Status: unresolved
- Probe template: `redistribute subscriber {tag <0-4294967295>|route-policy <WORD>|lsa-type summary|nssa-only}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.93
- Review rationale: The evidence establishes the probe command template, but provides no manual content or coverage evidence to verify the asserted lack of a matching command topic in the router view.
- Evidence `P00897:probe` (probe_template): redistribute subscriber {tag <0-4294967295>|route-policy <WORD>|lsa-type summary|nssa-only}

#### F00901

- Status: unresolved
- Probe template: `retransmit-interval <1-65535>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but does not establish that the supplied manuals contain no matching command topic for the area semantic view.
- Evidence `P00898:probe` (probe_template): retransmit-interval <1-65535>

#### F00902

- Status: unresolved
- Probe template: `retransmit-interval <1-65535>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but does not establish that the supplied manuals contain no matching command topic for the interface semantic view.
- Evidence `P00899:probe` (probe_template): retransmit-interval <1-65535>

#### F00903

- Status: unresolved
- Probe template: `retransmit-interval <1-65535>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but does not establish that the supplied manuals contain no matching command topic for the multi-area semantic view.
- Evidence `P00900:probe` (probe_template): retransmit-interval <1-65535>

#### F00904

- Status: unresolved
- Probe template: `retransmit-interval <1-65535>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe template but does not establish that the supplied manuals contain no matching command topic for the router semantic view.
- Evidence `P00901:probe` (probe_template): retransmit-interval <1-65535>

#### F00905

- Status: unresolved
- Probe template: `retransmit-interval <1-65535>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00902:probe` (probe_template): retransmit-interval <1-65535>

#### F00906

- Status: unresolved
- Probe template: `retransmit-interval <1-65535>`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00903:probe` (probe_template): retransmit-interval <1-65535>

#### F00907

- Status: unresolved
- Probe template: `retransmit-interval <1-65535>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00904:probe` (probe_template): retransmit-interval <1-65535>

#### F00908

- Status: unresolved
- Probe template: `route-policy <WORD> {in|out}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00905:probe` (probe_template): route-policy <WORD> {in|out}

#### F00909

- Status: unresolved
- Probe template: `router ospf <WORD>`
- Probe view: global
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template; it provides no manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00906:probe` (probe_template): router ospf <WORD>

#### F00910

- Status: unresolved
- Probe template: `router ospf <WORD> affinity-map`
- Probe view: global
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template; it provides no manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00907:probe` (probe_template): router ospf <WORD> affinity-map

#### F00911

- Status: unresolved
- Probe template: `router ospf <WORD> affinity-map <WORD> bit-position <0-255>`
- Probe view: global
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template; it provides no manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00908:probe` (probe_template): router ospf <WORD> affinity-map <WORD> bit-position <0-255>

#### F00912

- Status: unresolved
- Probe template: `router-id <A.B.C.D>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template; it provides no manual coverage evidence to verify that no matching command topic exists.
- Evidence `P00909:probe` (probe_template): router-id <A.B.C.D>

#### F00913

- Status: unresolved
- Probe template: `router-id <A.B.C.D>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00910:probe` (probe_template): router-id <A.B.C.D>

#### F00914

- Status: unresolved
- Probe template: `security ttl [disable|hops <1-254>]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00911:probe` (probe_template): security ttl [disable|hops <1-254>]

#### F00915

- Status: unresolved
- Probe template: `security ttl [disable|hops <1-254>]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00912:probe` (probe_template): security ttl [disable|hops <1-254>]

#### F00916

- Status: unresolved
- Probe template: `security ttl [hops <1-254>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence from which to verify that no matching command topic exists.
- Evidence `P00913:probe` (probe_template): security ttl [hops <1-254>]

#### F00917

- Status: unresolved
- Probe template: `security ttl [hops <1-254>]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00914:probe` (probe_template): security ttl [hops <1-254>]

#### F00918

- Status: unresolved
- Probe template: `security ttl [hops <1-254>|disable]`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00915:probe` (probe_template): security ttl [hops <1-254>|disable]

#### F00919

- Status: unresolved
- Probe template: `security ttl [hops <1-254>|disable]`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00916:probe` (probe_template): security ttl [hops <1-254>|disable]

#### F00920

- Status: unresolved
- Probe template: `segment-routing forwarding {disable|mpls}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the Probe command template. It provides no manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00917:probe` (probe_template): segment-routing forwarding {disable|mpls}

#### F00921

- Status: unresolved
- Probe template: `segment-routing forwarding {mpls|disable}`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes the probe command template but provides no supplied manual evidence to verify that no matching command topic exists.
- Evidence `P00918:probe` (probe_template): segment-routing forwarding {mpls|disable}

#### F00922

- Status: unresolved
- Probe template: `segment-routing prefix-sid-map {receive disable|advertise-local}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The probe template is evidenced, but the absence of a matching topic in supplied manuals cannot be determined without manual evidence.
- Evidence `P00919:probe` (probe_template): segment-routing prefix-sid-map {receive disable|advertise-local}

#### F00923

- Status: unresolved
- Probe template: `segment-routing sr-prefer [prefix-list <WORD>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence only identifies the probe command template and does not support or refute the claimed lack of manual coverage.
- Evidence `P00920:probe` (probe_template): segment-routing sr-prefer [prefix-list <WORD>]

#### F00924

- Status: unresolved
- Probe template: `segment-routing {forwarding {disable|mpls}|disable|mpls|protected-adjacency-sid-delay <30-3600>|global-block <16000-1048575> <16000-1048575>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The supplied evidence confirms the probe template only; it contains no manual-topic evidence sufficient to establish command undercoverage.
- Evidence `P00921:probe` (probe_template): segment-routing {forwarding {disable|mpls}|disable|mpls|protected-adjacency-sid-delay <30-3600>|global-block <16000-1048575> <16000-1048575>}

#### F00925

- Status: unresolved
- Probe template: `segment-routing {forwarding {disable|mpls}|disable|mpls}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supplies the probe template but provides no manual content or command-topic inventory to substantiate that no matching command exists.
- Evidence `P00922:probe` (probe_template): segment-routing {forwarding {disable|mpls}|disable|mpls}

#### F00926

- Status: unresolved
- Probe template: `segment-routing {forwarding {mpls|disable}|mpls|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supplies the probe template but provides no manual content or command-topic inventory to substantiate that no matching command exists.
- Evidence `P00923:probe` (probe_template): segment-routing {forwarding {mpls|disable}|mpls|disable}

#### F00927

- Status: unresolved
- Probe template: `sham-link <A.B.C.D> <A.B.C.D>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supplies the probe template but provides no manual content or command-topic inventory to substantiate that no matching command exists.
- Evidence `P00924:probe` (probe_template): sham-link <A.B.C.D> <A.B.C.D>

#### F00928

- Status: unresolved
- Probe template: `snmp {trap rate-limit <2-60> <0-300>|context <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence supplies the probe template but provides no manual content or command-topic inventory to substantiate that no matching command exists.
- Evidence `P00925:probe` (probe_template): snmp {trap rate-limit <2-60> <0-300>|context <WORD>}

#### F00929

- Status: unresolved
- Probe template: `snmp {trap|context <WORD>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but provides no supplied manual evidence or corpus coverage information to support the claimed absence of a matching command topic.
- Evidence `P00926:probe` (probe_template): snmp {trap|context <WORD>}

#### F00930

- Status: unresolved
- Probe template: `spf prefix-priority route-policy <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but does not support the assertion that no supplied manual command topic matches it.
- Evidence `P00927:probe` (probe_template): spf prefix-priority route-policy <WORD>

#### F00931

- Status: unresolved
- Probe template: `spf prefix-priority route-policy <WORD>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but contains no manual-command evidence sufficient to verify undercoverage for the VRF semantic view.
- Evidence `P00928:probe` (probe_template): spf prefix-priority route-policy <WORD>

#### F00932

- Status: unresolved
- Probe template: `srlg`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe command but does not establish that the supplied manuals lack a matching command topic.
- Evidence `P00929:probe` (probe_template): srlg

#### F00933

- Status: unresolved
- Probe template: `srlg exclude-any`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes only the probe template; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00930:probe` (probe_template): srlg exclude-any

#### F00934

- Status: unresolved
- Probe template: `srlg exclude-any <WORD>`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes only the probe template; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00931:probe` (probe_template): srlg exclude-any <WORD>

#### F00935

- Status: unresolved
- Probe template: `stub`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes only the probe template; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00932:probe` (probe_template): stub

#### F00936

- Status: unresolved
- Probe template: `stub no-summary`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.92
- Review rationale: The supplied evidence establishes only the probe template; it does not provide manual coverage evidence sufficient to verify that no matching command topic exists.
- Evidence `P00933:probe` (probe_template): stub no-summary

#### F00937

- Status: unresolved
- Probe template: `summary-in`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the probe template but does not provide manual-search results or documentation inventory sufficient to verify that no matching command topic exists.
- Evidence `P00934:probe` (probe_template): summary-in

#### F00938

- Status: unresolved
- Probe template: `summary-in`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the probe template but does not provide manual-search results or documentation inventory sufficient to verify that no matching command topic exists.
- Evidence `P00935:probe` (probe_template): summary-in

#### F00939

- Status: unresolved
- Probe template: `summary-in`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the probe template but does not provide manual-search results or documentation inventory sufficient to verify that no matching command topic exists.
- Evidence `P00936:probe` (probe_template): summary-in

#### F00940

- Status: unresolved
- Probe template: `summary-in {disable|enable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The evidence identifies the probe template but does not provide manual-search results or documentation inventory sufficient to verify that no matching command topic exists.
- Evidence `P00937:probe` (probe_template): summary-in {disable|enable}

#### F00941

- Status: unresolved
- Probe template: `summary-in {disable|enable}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00938:probe` (probe_template): summary-in {disable|enable}

#### F00942

- Status: unresolved
- Probe template: `summary-in {disable|enable}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual evidence sufficient to verify that no matching command topic exists for the VRF view.
- Evidence `P00939:probe` (probe_template): summary-in {disable|enable}

#### F00943

- Status: unresolved
- Probe template: `summary-in {enable|disable}`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual evidence sufficient to verify that no matching command topic exists for the area view.
- Evidence `P00940:probe` (probe_template): summary-in {enable|disable}

#### F00944

- Status: unresolved
- Probe template: `summary-prefix <A.B.C.D/prefix/mask> [not-advertise|tag <0-4294967295>]`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual evidence sufficient to verify that no matching command topic exists.
- Evidence `P00941:probe` (probe_template): summary-prefix <A.B.C.D/prefix/mask> [not-advertise|tag <0-4294967295>]

#### F00945

- Status: unresolved
- Probe template: `summary-prefix <A.B.C.D/prefix/mask> [tag <0-4294967295>|not-advertise]`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe command template. It provides no supplied manual content or coverage inventory that can substantiate the claimed absence of a matching command topic.
- Evidence `P00942:probe` (probe_template): summary-prefix <A.B.C.D/prefix/mask> [tag <0-4294967295>|not-advertise]

#### F00946

- Status: unresolved
- Probe template: `te-metric flex-algo <1-2147483647>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The probe template alone does not establish that no supplied manual command topic matches it. No manual evidence is provided.
- Evidence `P00943:probe` (probe_template): te-metric flex-algo <1-2147483647>

#### F00947

- Status: unresolved
- Probe template: `te-metric flex-algo <1-2147483647>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence identifies the probe template but does not provide manual-command evidence sufficient to verify undercoverage for the multi-area semantic view.
- Evidence `P00944:probe` (probe_template): te-metric flex-algo <1-2147483647>

#### F00948

- Status: unresolved
- Probe template: `timers lsa {min-arrival <0-600000>|group-pacing <10-1800>|refresh <1800-2700>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence contains only the probe template and cannot support a determination that the manuals lack a matching command topic.
- Evidence `P00945:probe` (probe_template): timers lsa {min-arrival <0-600000>|group-pacing <10-1800>|refresh <1800-2700>}

#### F00949

- Status: unresolved
- Probe template: `timers lsa {min-arrival <0-600000>|refresh <1800-2700>|group-pacing <10-1800>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00946:probe` (probe_template): timers lsa {min-arrival <0-600000>|refresh <1800-2700>|group-pacing <10-1800>}

#### F00950

- Status: unresolved
- Probe template: `timers pacing flood <5-100>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00947:probe` (probe_template): timers pacing flood <5-100>

#### F00951

- Status: unresolved
- Probe template: `timers throttle {lsa all <0-600000> <1-600000> <1-600000>|spf <1-600000> <1-600000>|fast-reroute <50-600000>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00948:probe` (probe_template): timers throttle {lsa all <0-600000> <1-600000> <1-600000>|spf <1-600000> <1-600000>|fast-reroute <50-600000>}

#### F00952

- Status: unresolved
- Probe template: `timers throttle {spf <1-600000> <1-600000>|fast-reroute <50-600000>|lsa all <0-600000> <1-600000> <1-600000>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe command but provides no supplied manual corpus or command-topic evidence to verify that no matching manual topic exists.
- Evidence `P00949:probe` (probe_template): timers throttle {spf <1-600000> <1-600000>|fast-reroute <50-600000>|lsa all <0-600000> <1-600000> <1-600000>}

#### F00953

- Status: unresolved
- Probe template: `timers {pacing flood <5-100>|graceful-shutdown {initial delay|retain routes} <0-90>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence establishes the probe template but supplies no manual content or command-topic inventory to verify that no matching manual topic exists.
- Evidence `P00950:probe` (probe_template): timers {pacing flood <5-100>|graceful-shutdown {initial delay|retain routes} <0-90>}

#### F00954

- Status: unresolved
- Probe template: `trace size <WORD> {0|1024|512|16384|4096|2048|32768|65536|256|8192}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The probe template is evidenced, but there is no supplied manual evidence from which to confirm or dismiss the asserted coverage gap.
- Evidence `P00951:probe` (probe_template): trace size <WORD> {0|1024|512|16384|4096|2048|32768|65536|256|8192}

#### F00955

- Status: unresolved
- Probe template: `track-external-routes`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The supplied evidence identifies the probe command only; it cannot establish whether the supplied manuals contain a corresponding command topic.
- Evidence `P00952:probe` (probe_template): track-external-routes

#### F00956

- Status: unresolved
- Probe template: `track-ip-frr`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.90
- Review rationale: The evidence supports the existence of the probe template, but no manual text or topic listing is supplied to assess the undercoverage assertion.
- Evidence `P00953:probe` (probe_template): track-ip-frr

#### F00957

- Status: unresolved
- Probe template: `track-summary-routes`
- Probe view: unknown
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template but provides no supplied manual coverage evidence to support or refute the claimed absence of a matching command topic.
- Evidence `P00954:probe` (probe_template): track-summary-routes

#### F00958

- Status: unresolved
- Probe template: `transmit-delay <1-65535>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template and area semantic view only; it does not establish that supplied manuals lack a matching command topic.
- Evidence `P00955:probe` (probe_template): transmit-delay <1-65535>

#### F00959

- Status: unresolved
- Probe template: `transmit-delay <1-65535>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template and interface semantic view only; no manual-topic evidence is supplied to decide the undercoverage claim.
- Evidence `P00956:probe` (probe_template): transmit-delay <1-65535>

#### F00960

- Status: unresolved
- Probe template: `transmit-delay <1-65535>`
- Probe view: multi-area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes the probe template and multi-area semantic view only; it cannot support a determination about absence of matching manual coverage.
- Evidence `P00957:probe` (probe_template): transmit-delay <1-65535>

#### F00961

- Status: unresolved
- Probe template: `transmit-delay <1-65535>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence sufficient to verify that no matching router command exists.
- Evidence `P00958:probe` (probe_template): transmit-delay <1-65535>

#### F00962

- Status: unresolved
- Probe template: `transmit-delay <1-65535>`
- Probe view: sham-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence sufficient to verify that no matching sham-link command exists.
- Evidence `P00959:probe` (probe_template): transmit-delay <1-65535>

#### F00963

- Status: unresolved
- Probe template: `transmit-delay <1-65535>`
- Probe view: virtual-link
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence sufficient to verify that no matching virtual-link command exists.
- Evidence `P00960:probe` (probe_template): transmit-delay <1-65535>

#### F00964

- Status: unresolved
- Probe template: `transmit-delay <1-65535>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The supplied evidence establishes only the probe template. It provides no manual inventory or command-topic evidence sufficient to verify that no matching VRF command exists.
- Evidence `P00961:probe` (probe_template): transmit-delay <1-65535>

#### F00965

- Status: unresolved
- Probe template: `ucmp`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template, not whether supplied manuals contain a matching command topic.
- Evidence `P00962:probe` (probe_template): ucmp

#### F00966

- Status: unresolved
- Probe template: `ucmp`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template, not whether supplied manuals contain a matching command topic.
- Evidence `P00963:probe` (probe_template): ucmp

#### F00967

- Status: unresolved
- Probe template: `ucmp exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template, not whether supplied manuals contain a matching command topic.
- Evidence `P00964:probe` (probe_template): ucmp exclude interface GigabitEthernet {0/0/0/0|<R/S/I/P/B or R/S/I/P>}

#### F00968

- Status: unresolved
- Probe template: `ucmp exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the probe template, not whether supplied manuals contain a matching command topic.
- Evidence `P00965:probe` (probe_template): ucmp exclude interface GigabitEthernet {<R/S/I/P/B or R/S/I/P>|0/0/0/0}

#### F00969

- Status: unresolved
- Probe template: `ucmp exclude interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00966:probe` (probe_template): ucmp exclude interface MgmtEth {0/RP0/CPU0/0|<R/S/I/P>}

#### F00970

- Status: unresolved
- Probe template: `ucmp exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00967:probe` (probe_template): ucmp exclude interface MgmtEth {<R/S/I/P>|0/RP0/CPU0/0}

#### F00971

- Status: unresolved
- Probe template: `ucmp exclude interface Serial <R/S/I/P>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00968:probe` (probe_template): ucmp exclude interface Serial <R/S/I/P>

#### F00972

- Status: unresolved
- Probe template: `ucmp exclude interface Serial <R/S/I/P>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.96
- Review rationale: The supplied evidence identifies the probe command but provides no manual evidence to verify that no matching command topic exists.
- Evidence `P00969:probe` (probe_template): ucmp exclude interface Serial <R/S/I/P>

#### F00973

- Status: unresolved
- Probe template: `ucmp {prefix-list <WORD>|delay-interval <1-5000>|variance <101-10000>}`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the Probe command template. It provides no manual content or coverage inventory to support the claim that no supplied manual topic matches it.
- Evidence `P00970:probe` (probe_template): ucmp {prefix-list <WORD>|delay-interval <1-5000>|variance <101-10000>}

#### F00974

- Status: unresolved
- Probe template: `ucmp {variance <101-10000>|delay-interval <1-5000>|prefix-list <WORD>}`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence establishes only the Probe command template. It does not substantiate the asserted absence of a matching command topic in the supplied manuals.
- Evidence `P00971:probe` (probe_template): ucmp {variance <101-10000>|delay-interval <1-5000>|prefix-list <WORD>}

#### F00975

- Status: unresolved
- Probe template: `virtual-link <A.B.C.D>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The Probe template is evidenced, but no manual evidence is supplied from which to determine whether a matching topic is absent.
- Evidence `P00972:probe` (probe_template): virtual-link <A.B.C.D>

#### F00976

- Status: unresolved
- Probe template: `vrf <WORD>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.95
- Review rationale: The evidence shows the Probe command template only; it cannot confirm or dismiss the claimed lack of matching manual coverage.
- Evidence `P00973:probe` (probe_template): vrf <WORD>

#### F00977

- Status: unresolved
- Probe template: `weight <1-16777214>`
- Probe view: area
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual content or command-topic inventory to determine whether a matching manual topic exists for the area view.
- Evidence `P00974:probe` (probe_template): weight <1-16777214>

#### F00978

- Status: unresolved
- Probe template: `weight <1-16777214>`
- Probe view: interface
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual content or command-topic inventory to determine whether a matching manual topic exists for the interface view.
- Evidence `P00975:probe` (probe_template): weight <1-16777214>

#### F00979

- Status: unresolved
- Probe template: `weight <1-16777214>`
- Probe view: router
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual content or command-topic inventory to determine whether a matching manual topic exists for the router view.
- Evidence `P00976:probe` (probe_template): weight <1-16777214>

#### F00980

- Status: unresolved
- Probe template: `weight <1-16777214>`
- Probe view: vrf
- Probe groups: N/A
- Manual commands: N/A
- Manual blocks: N/A
- URLs: N/A
- Reason: No command topic in the supplied manuals matches this Probe command.
- LLM conclusion: unresolved
- Confidence: 0.98
- Review rationale: The evidence establishes only the Probe command template. It provides no supplied manual content or command-topic inventory to determine whether a matching manual topic exists for the VRF view.
- Evidence `P00977:probe` (probe_template): weight <1-16777214>
