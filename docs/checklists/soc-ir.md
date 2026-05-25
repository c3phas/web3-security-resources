---
title: SOC and Incident Response
description: SOC and Incident Response page in the Web3 Security Resources 2026 hub.
---

# SOC and Incident Response

## Detection

- Alerts cover privileged actions, upgrades, pause events, oracle drift, bridge flows, and outflows.
- Frontend, DNS, TLS, registrar, and hosting drift are monitored.
- Alerts route to humans with clear severity and ownership.
- False positives are reviewed and tuned.

## Response

- Incident commander, technical lead, comms lead, and legal contact are defined.
- Private response channel and backup comms exist.
- Evidence collection steps are documented.
- Emergency actions are rehearsed.
- External contacts include SEAL 911, exchanges, bridges, stablecoin issuers, infra providers, and registrar.

## Recovery

- Fix verification is required before resuming normal operations.
- Postmortem identifies root cause, detection gaps, and control gaps.
- Monitoring and checklists are updated after each incident.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Alert sources are mapped | List of on-chain, frontend, domain, wallet, support, and partner signals. | Security lead | Every material alert source has owner, severity, and response expectation. | Alerts reach a chat channel but do not create a case. |
| Evidence is preserved | Snapshot rules for transactions, traces, DNS, HTML, scripts, screenshots, logs, and reports. | Incident commander | Incident timelines can be reconstructed without relying on memory. | Evidence is overwritten during emergency deploys. |
| Remediation closes the loop | Root cause, containment, permanent fix, monitoring update, and risk register update. | Security lead | The same incident class has a harder path next time. | Postmortem produces tasks but no monitoring or control change. |
