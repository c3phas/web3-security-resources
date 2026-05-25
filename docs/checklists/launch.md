---
title: Launch Readiness
description: Launch Readiness page in the Web3 Security Resources 2026 hub.
---

# Launch Readiness

## Deployment

- Deployment commit, compiler versions, build settings, and addresses are recorded.
- Constructor and initializer arguments are reviewed.
- Source code is verified where possible.
- Deployment scripts are reproducible.
- Ownership transfer steps are rehearsed.
- Proxy implementations and admins are correct.

## Controls

- Admin roles are assigned to expected multisigs or governance.
- Timelocks are configured and tested.
- Emergency pause or rate-limit controls are documented.
- Oracle, bridge, and dependency assumptions are monitored.
- Launch parameters match audited assumptions.

## Monitoring

- Alerts exist for privileged actions, upgrades, oracle drift, reserve changes, and abnormal outflows.
- Frontend asset drift, DNS, TLS, and registrar changes are monitored.
- Incident response contacts and signer availability are confirmed.
- Public communication templates are prepared.

## Final Gate

- External audit fixes are verified.
- Known risks are accepted by the right owners.
- Bug bounty or disclosure channel is live.
- Rollback or mitigation options are understood.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Deployment artifacts are frozen | Commit hash, compiler settings, verified addresses, constructor args, salts, and chain IDs. | Engineering lead | A third party can reproduce what is about to be deployed. | Last-minute deployment scripts differ from audited scripts. |
| Public trust paths are monitored | Domain, DNS, TLS, frontend, wallet modal, RPC, and phishing baseline. | Security lead | Launch-critical user paths have baseline evidence and drift alerts. | Only contracts are monitored while frontend remains operational risk. |
| Emergency actions are rehearsed | Pause, upgrade, signer replacement, comms, and rollback drill logs. | Protocol founder | The team can execute emergency actions without improvising. | Controls exist but signers or comms owners have never practiced them. |
