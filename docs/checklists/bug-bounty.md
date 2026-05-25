---
title: Bug Bounty Readiness
description: Bug Bounty Readiness page in the Web3 Security Resources 2026 hub.
---

# Bug Bounty Readiness

- Scope includes contracts, frontends, APIs, apps, and infra where relevant.
- Out-of-scope items are precise and defensible.
- Severity rubric maps impact to payout.
- Safe harbor language is published.
- Disclosure channel is monitored.
- Triage owners and response SLAs are defined.
- Duplicate handling is documented.
- Known issues are listed privately for triage.
- Emergency escalation path is available for critical reports.
- Reports can be fixed and verified without leaking reporter data.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Scope is precise | In-scope contracts, chains, frontends, domains, APIs, and excluded assets. | Security lead | Researchers can tell whether a report belongs in the program. | Critical off-chain or frontend paths are excluded by accident. |
| Severity is calibrated | Rubric tied to funds at risk, governance impact, user deception, and operational compromise. | Security lead | Triage decisions are consistent and explainable. | Frontend, oracle, or governance impact is undervalued. |
| Safe testing rules are clear | Allowed PoC rules, fork guidance, rate limits, and user harm boundaries. | Legal and security | Researchers can prove impact without touching user funds or secrets. | Testing guidance is vague and creates conflict during real reports. |
