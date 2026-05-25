---
title: Post-Launch Operations
description: Post-Launch Operations page in the Web3 Security Resources 2026 hub.
---

# Post-Launch Operations

- Review privileged transactions weekly.
- Monitor TVL, reserves, oracle freshness, liquidity, and bridge accounting.
- Track governance proposals from creation to execution.
- Review dependency, frontend, DNS, and hosting changes.
- Keep a live asset and privilege inventory.
- Rehearse incident response quarterly.
- Rotate stale access and remove inactive contributors.
- Review bug bounty reports and duplicate patterns.
- Run postmortems for incidents, near misses, and severe false alarms.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Drift is reviewed | Recurring scans for contracts, frontends, DNS, certificates, dependencies, and privileged transactions. | Security lead | Material changes generate an owner and review record. | Alerts exist but no one is accountable for triage. |
| Bounty intake is operational | Public policy, triage rotation, severity rubric, safe harbor, and payment path. | Security lead | Reports can be handled within SLA without exposing sensitive details. | Researchers report through social channels because official intake is unclear. |
| Risk exceptions expire | Accepted-risk register with expiry dates and reapproval workflow. | Protocol founder | Temporary launch exceptions do not become permanent unowned risk. | Accepted risks are never re-reviewed after usage grows. |
