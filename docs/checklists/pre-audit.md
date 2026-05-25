---
title: Pre-Audit Readiness
description: Pre-Audit Readiness page in the Web3 Security Resources 2026 hub.
---

# Pre-Audit Readiness

## Scope

- Code freeze date is defined.
- In-scope repositories, commits, contracts, deployments, and chains are listed.
- Out-of-scope components and trusted dependencies are explicit.
- Protocol documentation explains assets, roles, invariants, and emergency powers.
- Architecture diagram shows contracts, oracles, bridges, frontends, APIs, and governance.

## Code and Tests

- Unit tests cover expected and failing paths.
- Fuzz or invariant tests cover accounting, permissions, and core state machines.
- Static analysis has been run and triaged.
- Dependencies are pinned and licenses are acceptable.
- Upgradeable contracts have storage-layout checks.
- Deployment scripts are tested on a fork or testnet.

## Security Context

- Threat model is current.
- Privileged roles and multisigs are documented.
- Known issues and risk acceptances are listed.
- Prior audit reports and fix status are linked.
- Monitoring and incident plans exist for critical flows.

## Auditor Package

- Build and test instructions work from a clean clone.
- Environment variables are documented without secrets.
- Diagrams and protocol docs match the code.
- Contact path for questions is defined.
- Expected report format and severity model are agreed.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Scope is complete | Repository commit, deployment plan, threat model, diagrams, and out-of-scope list. | Security lead | Auditors can identify every component that moves funds, changes state, or influences users. | Scope omits frontend, keeper, oracle, bridge, upgrade, or admin tooling. |
| Tests prove invariants | Unit, integration, fuzz, fork, and scenario tests linked to protocol invariants. | Engineering lead | Critical invariants have automated tests and limitations are documented. | Coverage exists but does not encode solvency, accounting, authorization, or liquidation invariants. |
| Known risks are accepted explicitly | Risk register with severity, mitigation, owner, expiry, and launch decision. | Security lead | Open risks are visible before audit starts. | Risks are spread across chat, issues, and audit comments. |
